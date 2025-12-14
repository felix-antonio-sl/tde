import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


@dataclass
class AuditResult:
    koda_path: str
    sources: list[str]
    segments_total: int
    segments_missing: int
    missing_ratio: float
    missing_examples: list[str]


def iter_files(paths: list[Path], extensions: tuple[str, ...]) -> Iterable[Path]:
    for base in paths:
        if base.is_file() and base.suffix.lower() in extensions:
            yield base
            continue
        if not base.exists():
            continue
        for p in base.rglob("*"):
            if p.is_file() and p.suffix.lower() in extensions:
                yield p


def strip_frontmatter(md: str) -> str:
    lines = md.splitlines()
    if not lines or lines[0].strip() != "---":
        return md
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return "\n".join(lines[i + 1 :])
    return md


def remove_bibliography(md: str) -> str:
    lines = md.splitlines()
    out: list[str] = []
    for line in lines:
        if re.match(r"^\[¶\]\(#", line):
            if re.search(r"bibliograf", line, flags=re.IGNORECASE):
                return "\n".join(out)
            if re.search(r"referencias", line, flags=re.IGNORECASE):
                return "\n".join(out)
            if re.search(r"glosario", line, flags=re.IGNORECASE):
                return "\n".join(out)
            if re.search(r"anexo", line, flags=re.IGNORECASE):
                return "\n".join(out)
        out.append(line)
    return "\n".join(out)


def remove_fat_boilerplate(md: str) -> str:
    fat_patterns = [
        r"\ban[oó]tese\b",
        r"\bt[oó]mese\s+raz[oó]n\b",
        r"\bpubl[ií]quese\b",
        r"\bcomun[ií]quese\b",
    ]

    out: list[str] = []
    for line in md.splitlines():
        if any(re.search(p, line, flags=re.IGNORECASE) for p in fat_patterns):
            continue
        if re.search(r"Presidente\s+de\s+la\s+Rep[uú]blica", line, flags=re.IGNORECASE):
            continue
        out.append(line)

    return "\n".join(out)


def normalize_text(text: str) -> str:
    text = re.sub(r"data:[^\s]+base64,[A-Za-z0-9+/=]+", " ", text, flags=re.IGNORECASE)
    text = re.sub(r"[A-Za-z0-9+/=]{200,}", " ", text)
    text = re.sub(r"https?://\S+", " ", text)
    text = re.sub(r"\bwww\.[^\s]+", " ", text)
    text = text.replace("\u00a0", " ")
    text = re.sub(r"[`*_>#\[\]\(\)\{\}|]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip().lower()


def tokenize(text: str) -> list[str]:
    text = normalize_text(text)
    return re.findall(r"[a-záéíóúñ0-9]+", text, flags=re.IGNORECASE)


def extract_markdown_section_by_anchor(md: str, anchor: str) -> str:
    anchor = anchor.strip()
    if not anchor:
        return md

    anchor = anchor.lstrip("#")
    target = f"(#{anchor})"
    lines = md.splitlines()

    start = None
    for i, line in enumerate(lines):
        if target in line:
            start = i
            break

    if start is None:
        return md

    end = len(lines)
    for j in range(start + 1, len(lines)):
        if re.match(r"^\[¶\]\(#", lines[j]):
            end = j
            break
        if re.match(r"^\s*#", lines[j]):
            end = j
            break

    return "\n".join(lines[start:end]).strip()


def parse_sources_from_koda(yaml_text: str) -> list[str]:
    if not re.search(r"source_corpus:\s*['\"]?wikiguias_corpus['\"]?", yaml_text, flags=re.IGNORECASE):
        return []

    m = re.search(r"source_file:\s*['\"]([^'\"]+)['\"]", yaml_text)
    if m:
        return [m.group(1).strip()]

    sources: list[str] = []
    in_list = False
    list_indent = 0
    for line in yaml_text.splitlines():
        if re.match(r"^\s*source_files:\s*$", line):
            in_list = True
            list_indent = len(line) - len(line.lstrip())
            continue

        if in_list:
            if not line.strip():
                continue
            indent = len(line) - len(line.lstrip())
            if indent <= list_indent:
                in_list = False
                continue
            m2 = re.match(r"^\s*-\s*['\"]([^'\"]+)['\"]\s*$", line)
            if m2:
                sources.append(m2.group(1).strip())

    return sources


def extract_koda_text(yaml_text: str) -> str:
    values: list[str] = []
    lines = yaml_text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]

        m_list_single = re.match(r"^\s*-\s*(['\"])(.*)\1\s*$", line)
        if m_list_single:
            values.append(m_list_single.group(2).strip())
            i += 1
            continue

        m_list_start = re.match(r"^\s*-\s*(['\"])(.*)$", line)
        if m_list_start:
            quote = m_list_start.group(1)
            rest = m_list_start.group(2)
            if rest.rstrip().endswith(quote):
                values.append(rest.rstrip()[:-1].strip())
                i += 1
                continue

            parts: list[str] = [rest.strip()]
            i += 1
            while i < len(lines):
                nxt = lines[i]
                stripped = nxt.strip()
                if stripped.rstrip().endswith(quote):
                    parts.append(stripped.rstrip()[:-1].strip())
                    i += 1
                    break
                parts.append(stripped)
                i += 1
            values.append(" ".join(p for p in parts if p).strip())
            continue

        m_kv = re.match(r"^\s*[^#\s][^:]*:\s*(.+)$", line)
        if not m_kv:
            i += 1
            continue

        val = m_kv.group(1).strip()
        val = re.split(r"\s+#", val, maxsplit=1)[0].strip()

        if val in {"|", "|-", ">", ">-"}:
            base_indent = len(line) - len(line.lstrip())
            block: list[str] = []
            i += 1
            while i < len(lines):
                nxt = lines[i]
                if not nxt.strip():
                    block.append("")
                    i += 1
                    continue
                indent = len(nxt) - len(nxt.lstrip())
                if indent <= base_indent:
                    break
                block.append(nxt.strip())
                i += 1
            values.append("\n".join(block).strip())
            continue

        if not val:
            i += 1
            continue

        if (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
            values.append(val[1:-1])
            i += 1
            continue

        m_quoted_start = re.match(r"^(['\"])(.*)$", val)
        if m_quoted_start:
            quote = m_quoted_start.group(1)
            rest = m_quoted_start.group(2)
            if rest.rstrip().endswith(quote):
                values.append(rest.rstrip()[:-1].strip())
                i += 1
                continue

            parts: list[str] = [rest.strip()]
            base_indent = len(line) - len(line.lstrip())
            i += 1
            while i < len(lines):
                nxt = lines[i]
                if not nxt.strip():
                    i += 1
                    continue
                indent = len(nxt) - len(nxt.lstrip())
                if indent <= base_indent:
                    break
                stripped = nxt.strip()
                if stripped.rstrip().endswith(quote):
                    parts.append(stripped.rstrip()[:-1].strip())
                    i += 1
                    break
                parts.append(stripped)
                i += 1
            values.append(" ".join(p for p in parts if p).strip())
            continue

        if val in {"[]", "{}"}:
            i += 1
            continue

        if re.fullmatch(r"[0-9.\-]+", val):
            i += 1
            continue

        if val.startswith("[") and val.endswith("]"):
            i += 1
            continue

        values.append(val)
        i += 1

    return "\n".join(v for v in values if v)


def segment_markdown(md: str) -> list[str]:
    md = strip_frontmatter(md)
    md = remove_bibliography(md)
    md = remove_fat_boilerplate(md)

    segments: list[str] = []
    buf: list[str] = []

    def flush() -> None:
        nonlocal buf
        text = "\n".join(buf).strip()
        if text:
            segments.append(text)
        buf = []

    for raw in md.splitlines():
        line = raw.rstrip()
        if not line.strip():
            flush()
            continue
        if line.lstrip().startswith(">"):
            flush()
            continue
        if re.match(r"^\s*!\[.*\]\(.*\)\s*$", line):
            flush()
            continue

        if line.lstrip().startswith("|"):
            flush()
            if re.match(r"^\s*\|\s*---", line):
                continue
            table_line = line.strip()
            if " * " in table_line:
                normalized = table_line.strip("|").strip()
                parts = [p.strip() for p in normalized.split(" * ") if p.strip()]
                segments.extend(parts)
            else:
                segments.append(table_line)
            continue

        if re.match(r"^\s*#", line):
            flush()
            segments.append(line.strip())
            continue

        if re.match(r"^\[¶\]\(#", line):
            flush()
            segments.append(line.strip())
            continue

        buf.append(line)

    flush()

    return segments


def coverage(segment_tokens: set[str], koda_tokens: set[str]) -> float:
    if not segment_tokens:
        return 0.0
    return len(segment_tokens & koda_tokens) / len(segment_tokens)


def audit_one(koda_path: Path, sources_root: Path, min_tokens: int, coverage_threshold: float, max_examples: int) -> AuditResult | None:
    text = koda_path.read_text(encoding="utf-8")
    sources = parse_sources_from_koda(text)
    if not sources:
        return None

    koda_text = extract_koda_text(text)
    koda_tokens = set(tokenize(koda_text))

    seg_total = 0
    seg_missing = 0
    missing_examples: list[str] = []

    for src_spec in sources:
        if "#" in src_spec:
            src_rel, anchor = src_spec.split("#", 1)
        else:
            src_rel, anchor = src_spec, ""

        src_path = (sources_root / src_rel).resolve()
        if not src_path.exists():
            continue
        md = src_path.read_text(encoding="utf-8")
        if anchor:
            md = extract_markdown_section_by_anchor(md, anchor)
        for seg in segment_markdown(md):
            seg_tokens = set(tokenize(seg))
            if len(seg_tokens) < min_tokens:
                continue
            seg_total += 1
            c = coverage(seg_tokens, koda_tokens)
            if c < coverage_threshold:
                seg_missing += 1
                if len(missing_examples) < max_examples:
                    missing_examples.append(seg[:220].replace("\n", " "))

    if seg_total == 0:
        return AuditResult(
            koda_path=str(koda_path),
            sources=sources,
            segments_total=0,
            segments_missing=0,
            missing_ratio=0.0,
            missing_examples=[],
        )

    return AuditResult(
        koda_path=str(koda_path),
        sources=sources,
        segments_total=seg_total,
        segments_missing=seg_missing,
        missing_ratio=seg_missing / seg_total,
        missing_examples=missing_examples,
    )


def main() -> int:
    parser = argparse.ArgumentParser(prog="meat_diff_audit")
    parser.add_argument("--repo-root", type=str, default=str(Path(__file__).resolve().parents[1]))
    parser.add_argument("--koda-dir", action="append", default=["knowledge/core", "knowledge/domains/tde"])
    parser.add_argument("--sources-root", type=str, default="sources/wikiguias_corpus")
    parser.add_argument("--include", type=str, default="")
    parser.add_argument("--exclude", type=str, default="")
    parser.add_argument("--min-tokens", type=int, default=8)
    parser.add_argument("--coverage-threshold", type=float, default=0.40)
    parser.add_argument("--limit", type=int, default=30)
    parser.add_argument("--examples", type=int, default=0)
    parser.add_argument("--max-example-chars", type=int, default=160)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    koda_dirs = [repo_root / p for p in args.koda_dir]
    sources_root = (repo_root / args.sources_root).resolve()

    include_re = re.compile(args.include) if args.include else None
    exclude_re = re.compile(args.exclude) if args.exclude else None

    results: list[AuditResult] = []
    for p in iter_files(koda_dirs, (".yml", ".yaml")):
        p_str = str(p)
        if include_re and not include_re.search(p_str):
            continue
        if exclude_re and exclude_re.search(p_str):
            continue
        r = audit_one(p, sources_root, args.min_tokens, args.coverage_threshold, max_examples=5)
        if r is not None:
            results.append(r)

    results.sort(key=lambda r: r.missing_ratio, reverse=True)
    results = results[: max(args.limit, 0)]

    if args.json:
        print(
            json.dumps(
                [
                    {
                        "koda_path": r.koda_path,
                        "sources": r.sources,
                        "segments_total": r.segments_total,
                        "segments_missing": r.segments_missing,
                        "missing_ratio": r.missing_ratio,
                        "missing_examples": r.missing_examples,
                    }
                    for r in results
                ],
                ensure_ascii=False,
                indent=2,
            )
        )
        return 0

    for r in results:
        print(
            f"missing_ratio={r.missing_ratio:.2f}  missing={r.segments_missing:4d}/{r.segments_total:4d}  sources={len(r.sources):2d}  {r.koda_path}"
        )
        if args.examples > 0:
            for ex in r.missing_examples[: args.examples]:
                ex = ex[: args.max_example_chars].replace("\n", " ")
                print(f"  - {ex}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
