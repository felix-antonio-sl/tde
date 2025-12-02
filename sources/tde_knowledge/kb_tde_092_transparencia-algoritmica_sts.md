# Guide: Algorithmic Transparency Recommendations (CPLT)

ID: GUIDE-TA-MASTER-01
Version: 1.0.0
Status: Draft
Human-Creator: FS
Model-Collaborator: IA-GEMINI
Creation-Date: 2025-10-03
Modification-Date: 2025-10-03
Source: contexto minimo/legal/transparencia_algoritmos.md

---
**BEGIN_LLM_INSTRUCTIONS**

You are an AI agent consuming a Structured Telegraphic Style (STS) artifact. Your primary task is to parse and reason over THIS document with absolute fidelity, using only the rules defined below. This artifact is a self-contained source of truth.

1. **Core Objective**: Maintain perfect fidelity to the information (`meat`) and structure (`skeleton`). Do not summarize, interpret, or infer information not explicitly present.
2. **Lexicon Mode & Expansion**: This document uses an **Abbreviated Lexicon**. You MUST treat the following keywords as valid and expand them according to this mapping:
    - `Cpt:` -> `Concept:`
    - `Ctx:` -> `Context:`
    - `Def:` -> `Definition:`
    - `Ex:` -> `Example:`
    - `Fnd:` -> `Foundation:`
    - `ID:` -> `ID:`
    - `Nat:` -> `Nature:`
    - `Proc:` -> `Process:`
    - `Prohib:` -> `Prohibition:`
    - `Purp:` -> `Purpose:`
    - `Rec:` -> `Recommendation:`
    - `Ref:` -> `Reference:`
    - `Req:` -> `Requirement:`
    - `Res:` -> `Result:`
    - `Src:` -> `Source:`
    - `Warn:` -> `Warning:`
3. **Reference (`Ref:`) Policy**: `Ref:` is for internal cross-references only. It MUST point to an `ID:` that exists within THIS document.
4. **Language Invariance Policy**: The `Keywords` are a fixed control vocabulary in English. All `EssentialData` MUST be preserved in its original language (Spanish).

**END_LLM_INSTRUCTIONS**
---

## 1. Acronyms and Abbreviations

ID: GUIDE-TA-ACRONYMS-01

- Def: CPLT. Ctx: Consejo para la Transparencia.
- Def: Guía. Ctx: This guide for adopting CPLT Recommendations on Algorithmic Transparency.
- Def: IA. Ctx: Inteligencia artificial.
- Def: Ley de Transparencia. Ctx: Ley N°20.285.
- Def: Oficio Circular N°711. Ctx: Circular from Segpres and Ministry of Science on AI use in the public sector (11-Dec-2023).
- Def: Principio de Divisibilidad. Ctx: Principle from Art. 11, Ley de Transparencia. Req: If an act has public and secret info, provide access to the public part.
- Def: Recomendaciones. Ctx: The CPLT Recommendations on Algorithmic Transparency.
- Def: SDA. Ctx: Sistemas de decisiones automatizadas y semiautomatizadas.
- Def: Transparencia proactiva. Ctx: Publication of relevant info not mandated by active transparency law, based on principles of relevance, openness, etc.

## 2. Nature of the CPLT Recommendations

ID: GUIDE-TA-NATURE-01
Purp: To clarify the scope and legal standing of the CPLT recommendations on algorithmic transparency.

### 2.1. Definition and Structure

ID: GUIDE-TA-NATURE-DEFINITION-01

- Def: The Recommendations are a set of best practices for public institutions.
- Purp: To advance transparency and publicity of the SDA they use.
- Cpt: Structure.
  - Cpt: Part 1. Def: General transparency recommendations for SDA.
  - Cpt: Part 2. Def: Specific proactive transparency recommendations.

### 2.2. Relation to Existing Obligations

ID: GUIDE-TA-NATURE-OBLIGATIONS-01

- Cpt: Current transparency obligations for SDA.
  - Fnd: Yes, they exist.
  - Ctx: Information about SDA is subject to transparency laws if it falls under the definition of public information.
  - Ex-1: A request for access to technical manuals or bidding documents for an SDA.
  - Ex-2: Information on a contracted third-party SDA must be published under active transparency rules (Art. 7, Ley de Transparencia).

### 2.3. Relation to Other Instruments

ID: GUIDE-TA-NATURE-INSTRUMENTS-01

- Cpt: Relation to other legal norms.
  - Nat: The Recommendations are best practices.
  - Prohib: They do not replace or substitute existing legal obligations regarding SDA.
- Cpt: Relation to other specific SDA/IA instruments.
  - Prohib: They do not replace other norms or recommendations on SDA/IA concerning transparency or other fundamental rights (e.g., intellectual property, data protection).
  - Req: In case of conflict, binding regulations must be prioritized.
- Cpt: Difference from CPLT general instructions.
  - Ctx: General instructions (e.g., on Active Transparency) are mandatory for obligated subjects.
  - Ctx: The Recommendations are voluntary best practices.

### 2.4. Progressive Adoption

ID: GUIDE-TA-NATURE-ADOPTION-01

- Cpt: Adoption can be progressive.
  - Fnd: Yes.
  - Ctx: As best practices, organizations can adopt them flexibly or gradually.
  - Ex: Based on technological maturity or to avoid conflict with other applicable regulations.
  - Ex: For proactive transparency, organizations can start by publishing some SDA and leave others for a later stage.
- Warn: This flexibility is restricted in some specific aspects.
  - Ex: The specific information required to be proactively published about SDA in the respective sub-items is not flexible.

## 3. Relevant Concepts

ID: GUIDE-TA-CONCEPTS-01
Purp: Define key terms for understanding the Recommendations.

### 3.1. Algorithms

ID: GUIDE-TA-CONCEPTS-ALGORITHMS-01

- Def: A set of instructions for a computer to perform a task.
- Ctx: Used by organizations to make decisions and allocate resources based on data sets.
- Cpt: Transparency and accountability.
  - Nat: A core principle of algorithmic systems and data ethics.
  - Def: The quality of systems being explainable and providing minimum information about themselves.

### 3.2. Automated or Semi-Automated Decision System (SDA)

ID: GUIDE-TA-CONCEPTS-SDA-01

- Def: Any technology, system, or process that, using a computer system, helps, assists, supports, or replaces decision-making by an individual in an obligated entity.
- Ctx: These decisions are then formalized in an administrative act or an act with legal effects.
- Cpt: Scope includes AI systems.
  - Fnd: Yes.
  - Ctx: AI systems used to support, assist, or make decisions in the public sphere are covered by the SDA concept.
- Cpt: Scope beyond AI systems.
  - Ctx: Recommendations are not limited to a specific technology like AI.
  - Req: Covers any technology that cumulatively:
    - 1. Uses a computer system.
    - 2. Helps, assists, supports, or replaces decision-making in the institution.
  - Ex: Sequential systems, predictive systems, machine learning, decision automation/support systems.
- Cpt: What is NOT an SDA.
  - Ex: Mere storage of databases is not considered an SDA.
  - Just: It does not help, support, assist, or replace decision-making.

### 3.3. Training and Testing Phases

ID: GUIDE-TA-CONCEPTS-PHASES-01

- Def: Stages within the development of an SDA.
- Cpt: Training Phase.
  - Def: Stage where the parameters of an SDA model are adjusted for implementation.
  - Ctx: Uses training and validation data.
- Cpt: Testing Phase.
  - Def: Stage where the results learned by the SDA are evaluated for correctness.
  - Ctx: Uses a separate set of test data.
- Cpt: Applicability to non-production SDA.
  - Prohib: The Recommendations do not apply to SDA in non-production stages.
  - Ex: Systems in development, design, test environments, pilots, "sandboxes", or under simulated use.

### 3.4. Training, Validation, and Test Data

ID: GUIDE-TA-CONCEPTS-DATASETS-01

- Def: Data used during the development of an SDA.
- Cpt: Training Data.
  - Def: Subset of data used to prepare a model by adjusting its parameters.
  - Purp: To identify patterns, probabilities, and extract information.
- Cpt: Validation Data.
  - Def: Subset of data used to evaluate the training process.
  - Purp: Allows for initial performance assessment and adjustments.
- Cpt: Test Data.
  - Def: Subset of data, independent of the model, used to evaluate the final results.
  - Purp: To verify correct functioning.
- Cpt: Importance of data.
  - Ctx: Data used in training determines the system's behavior.
  - Obj: The goal is for the operational system to detect learned patterns in new cases to predict, classify, or solve problems.
- Cpt: Mention in Recommendations.
  - Fnd: Yes.
  - Ctx: Proactive transparency recommendations suggest publishing relevant information about the training, validation, and test datasets used.

### 3.5. Personal and Sensitive Data

ID: GUIDE-TA-CONCEPTS-PERSONAL-DATA-01

- Cpt: Personal Data.
  - Def: Any information linked or referred to an identified or identifiable natural person.
- Cpt: Sensitive Data.
  - Def: Personal data referring to physical or moral characteristics, private life, or intimacy.
  - Ex: Ethnic origin, political affiliation, socioeconomic status, religious beliefs, health data, biometric data, sexual orientation.
- Cpt: Other data categories.
  - Ex: Data of children/adolescents, data for historical/statistical/scientific purposes, geolocation data.
- Cpt: Mention in Recommendations.
  - Fnd: Yes, in several sections.
  - Ex-1: As an element to be protected in third-party SDA contracts.
  - Ex-2: As a factor for secrecy/reservation clauses in information access requests.
  - Ex-3: In proactive transparency, requiring publication of info on SDAs that profile individuals.
  - Ex-4: In proactive transparency, requiring info on channels for claims, including the right to object to automated decisions.

### 3.6. Profiling or Labeling of Individuals

ID: GUIDE-TA-CONCEPTS-PROFILING-01

- Def: Automated processing of personal data to evaluate, analyze, or predict aspects of a person.
- Ctx: Aspects include professional performance, economic situation, health, preferences, behavior, location.
- Fnd: Definition aligned with Law N°19.628.
- Ex-1: Determining frequent diseases in an elderly population to create preventive health programs.
- Ex-2: A system to predict no-shows for medical appointments in hospitals.
- Ex-3: A predictive model for medical leave claims to improve institutional response capacity.

### 3.7. Bias in SDA Context

ID: GUIDE-TA-CONCEPTS-BIAS-01

- Def: Obtaining erroneous results that may be unfair, discriminatory, arbitrary, or unduly affect fundamental rights.
- Ctx: Bias can be introduced at any stage of SDA development and operation.
- Ex: Historical bias, representation bias, measurement bias, methodological bias.
- Cpt: How bias is generated.
  - Ex-1: At the objective-setting stage for the SDA.
  - Ex-2: In the data used (outdated, erroneous, not representative).
  - Ex-3: During the training process (misuse of model, validation errors).
- Cpt: Real-world example.
  - Ex: The Risk Indication System (SyRI) in the Netherlands.
  - Purp: To detect fraud in social security.
  - Res: In Feb 2020, a court ruled it violated the right to private life due to lack of transparency and bias.

### 3.8. Black Box Systems

ID: GUIDE-TA-CONCEPTS-BLACKBOX-01

- Def: Inherently opaque technological systems whose internal functioning or underlying logic is not adequately understood, or whose results cannot be explained.
- Rec: The Recommendations suggest that obligated subjects should favor SDAs that allow for a higher level of transparency and explainability.

## 4. General Transparency Recommendations: Practical Aspects

ID: GUIDE-TA-GENERAL-REC-01
Purp: To provide practical guidance for implementing general transparency principles in the use of SDAs.

### 4.1. Use of Plain Language

ID: GUIDE-TA-GENERAL-REC-LANGUAGE-01

- Req: Information about SDAs must be delivered concisely, intelligibly, and using clear, understandable language.
- Just: SDAs are complex and can be hard to understand.
- Cpt: Benefits of plain language.
  - Res-1: Strengthens public trust in institutions.
  - Res-2: Reduces citizen inquiries, leading to more efficient use of resources.
  - Res-3: Empowers citizens to exercise their rights and fulfill their duties.
- Cpt: Methods for explaining technical information.
  - Rec: Use tools like videos, graphics, plain text, Q&A formats, transparency sheets (model cards).
  - Src: "Guía de lenguaje claro" by Laboratorio de Gobierno (2019), Gobierno de Chile.

### 4.2. Transparency in SDA Contracting and Development

ID: GUIDE-TA-GENERAL-REC-CONTRACTING-01

- Req: Entities must publish information on SDA contracting and development "according to general application rules."
- Ctx: In the context of the Transparency Law, this implies compliance with active transparency obligations (Article 7).
- Fnd: Obligations specified in the CPLT's General Instruction on Active Transparency.
- Cpt: Specific obligations.
  - Req-1: Mandatory publication of information on acquisitions and contracts.
  - Req-2: Mandatory publication of acts and resolutions affecting third parties.
- Cpt: Example application.
  - Ex: Laura Eniax system, a virtual assistant for waiting list management at Hospital del Salvador.
  - Ctx: Contracted from ENIAX SpA.
  - Proc: The hospital's active transparency site links to the public procurement portal, where the tender (ID 1057489-93-LE23) is available.
- Rec: Establish special conditions for transparency and data protection in third-party SDA contracts.
- Src-1: "Directiva de Contratación Pública N°44" (ChileCompra, 7-Dec-2023) on acquiring data science and AI projects.
- Src-2: "Guía de Formulación ética de proyectos de ciencias de datos" (Gobierno Digital & UAI, Aug-2022).

### 4.3. Right of Access to Information and Secrecy Clauses

ID: GUIDE-TA-GENERAL-REC-ACCESS-01

- Cpt: CPLT's role.
  - Fnd: Per Article 33 of the Transparency Law.
  - Def: To resolve claims regarding the right of access to public information, including requests related to SDAs.
- Cpt: Considerations for responding to SDA-related requests.
  - Rec: Obligated subjects should consider the intrinsic characteristics and technical complexity of SDAs.
  - Purp: To provide timely and relevant information and to properly assess and justify any applicable secrecy clauses.
- Cpt: Denial of access.
  - Fnd: Yes, it is possible. The right of access is not absolute.
  - Ctx: Article 21 of the Transparency Law lists secrecy or reservation clauses that can be invoked.
- Cpt: CPLT criterion for secrecy.
  - Req: The harm to the legally protected interests must be present or probable and sufficiently specific.
  - Warn: Harm is not presumed; it must be proven.
- Cpt: Specific aspects to consider when invoking secrecy for SDA information.
  - Cpt: Harm to inspection/sanction functions.
    - Ctx: Revealing info could harm the due fulfillment of the body's functions.
    - Ex: CPLT decision C12867-23 against the IRS. Rejected access to algorithmic parameters for tax audit selection. Just: Harm to inspection functions and state economic interests (Art. 21, N°1 & N°4).
  - Cpt: Harm to security.
    - Ctx: Affecting security of IT systems, SDAs, or cybersecurity (Law N°21.663).
    - Ex: Cybersecurity risk matrices, business continuity plans, and mitigation plans are reserved under Law N°21.663.
  - Cpt: Harm to personal data protection.
    - Fnd: Law N°19.628.
    - Ex: CPLT decision C7529-20. Denied access to the "Puntaje Alerta Niñez" instrument to protect children's data.
  - Cpt: Harm to third-party intellectual property rights.
    - Fnd: Art. 21, N°2 of the Transparency Law.
- Cpt: Technical complexity as a cause for secrecy.
  - Prohib: No. Technical complexity or opacity is not a legally recognized cause for reservation.

### 4.4. Black Box or Similar Systems

ID: GUIDE-TA-GENERAL-REC-BLACKBOX-01

- Ctx: Some SDAs use opaque technologies (e.g., Deep Learning), making information disclosure difficult.
- Rec: When there is a real technical impossibility to provide information.
  - Proc-1: Provide a detailed explanation of this circumstance.
  - Proc-2: Offer additional, clear, and exhaustive information about the system and its operation.
- Cpt: Required explanation.
  - Prohib: Simply stating a technical difficulty or the presence of a black box system is insufficient.
  - Req: The body should explain both the nature of the system and other available aspects of its operation.
  - Ex: Answer questions like: Why was the SDA implemented? Since when is it used? What is its objective? What type of system is it? Does it make or support decisions?
- Src: ChileCompra's "Directiva de Contratación Pública N°44".
  - Cpt: Identifies "black box" models as a risk in acquiring AI/data science projects.
  - Rec: Acquiring bodies must take precautions to understand how decisions are made to be able to explain them to citizens.

### 4.5. Transparency in Public-Facing Tools

ID: GUIDE-TA-GENERAL-REC-PUBLIC-TOOLS-01

- Rec: Adopt measures to let people know when they are communicating or interacting with virtual assistants, chatbots, or similar systems.
- Ex-1: "Asistente virtual" from Servicio Electoral. Clearly identifies itself as a virtual assistant.
- Ex-2: Laura Eniax from Hospital del Salvador. Communicates with patients via various channels.
- Ex-3: RENCAT from Municipalidad de Renca. A chatbot that explicitly states it is an AI system.
- Fnd: This recommendation aligns with Oficio Circular N°711, which recommends communicating the use of AI tools in citizen interactions.

## 5. Specific Proactive Transparency Recommendations

ID: GUIDE-TA-SPECIFIC-REC-01
Purp: For organizations to publish specific information about SDAs that affect fundamental rights or access to services and benefits on their active transparency websites.

### 5.1. Scope: Which SDAs to Publish

ID: GUIDE-TA-SPECIFIC-REC-SCOPE-01

- Req: Publish SDAs that have effects on:
  - 1. The fundamental rights of people, OR
  - 2. Their access to services, social programs, subsidies, funds, and other benefits.
- Ex: Systems for decisions on granting public services, conducting an audit, or a sanctioning procedure.
- Cpt: Internal SDAs.
  - Prohib: SDAs for purely internal use should not be published.
  - Cond: If an SDA has both internal and external effects (on citizens), it must be published.
- Fnd: Aligns with Oficio Circular N° 711, which recommends making information available about AI tools used for decision-making that could affect fundamental rights.
- Cpt: Examples of SDAs subject to proactive publication.
  - Ex-1: School Admission System (SAE) from the Ministry of Education.
  - Ex-2: Socioeconomic qualification calculation system for social benefits, from the Undersecretariat of Social Evaluation.
  - Ex-3: Salmon Farming Center monitoring system, from the Superintendence of the Environment.

### 5.2. Publication Objective

ID: GUIDE-TA-SPECIFIC-REC-OBJECTIVE-01

- Purp: To inform citizens about three aspects (sub-items):
  - A) The SDAs being used in the organization.
  - B) The administrative procedures, services, etc., where SDAs are used.
  - C) Specifications of the SDAs (objective, functioning, data categories).

### 5.3. Publication Location

ID: GUIDE-TA-SPECIFIC-REC-LOCATION-01

- Req: On the organization's active transparency website.
- Ctx: Under a new item named "Transparencia algorítmica", within the "Transparencia Proactiva" section.

### 5.4. Specific Information to Publish

ID: GUIDE-TA-SPECIFIC-REC-INFO-01

- Ctx: The "Transparencia algorítmica" item comprises three sub-items.
- Req: In each sub-item, the name and internal identifier of the SDA must always be indicated.
- Cpt: Common Fields

  |Field|Description|Value Type|
  |-|-|-|
  |**1. Nombre del SDA**|Name or denomination of the SDA.|Free|
  |**2. Identificador interno del SDA**|Internal ID of the SDA. Must be unique. If none exists, one must be created.|Free|

#### 5.4.1. Sub-item 1: Automated or Semi-Automated Decision Systems

ID: GUIDE-TA-SPECIFIC-REC-SUBITEM1-01

- Purp: Publish the SDAs used by the institution.

|Aspect|Sub-aspect|Description|Value Type|
|-|-|-|-|
|**1. Identificación del SDA**|**1.1 Nombre del SDA**|Example: "Calculadora Índice de Vulnerabilidad".|Libre|
||**1.2 Identificador interno del SDA**|Ref: GUIDE-TA-SPECIFIC-REC-INFO-01. Example: "SDA-CIV1".|Libre|
||**1.3 Versión del SDA**|SDA software version. Example: "1.0 2022/03".|Libre|
||**1.4 Fecha de versión del SDA**|Version date. Example: "01-03-2022".|dd-mm-aaaa|
|**2. Canal de consultas o reclamación**|**2.1 Existencia de canal...**|If a specific channel for the SDA exists. If only general channels (OIRS) exist, indicate "No".|Sí/No, aplican las reglas generales del organismo|
||**2.2 Forma de acceder al canal...**|If "Sí", provide access details (phone, email, link).|Libre|
||**2.3 Vinculación del canal... con derecho de oposición a decisiones automatizadas.**|In relation to Art. 8 bis of Law N°19.628.|Sí/No|
|**3. Propiedad del SDA**|**3.1 Titularidad de derechos...**|Is the org the owner or a licensee?|Titularidad del organismo o del Estado/Licenciado|
||**3.2 Nombre del tercero proveedor...**|If licensed, provide the supplier's name. Otherwise, "No aplica".|Libre|
||**3.3 RUT del tercero proveedor...**|Supplier's tax ID (for legal entities).|Libre|
|**4. Enlace adicional**|**4.1 Enlace con más información...**|Link to a website with more info about the SDA.|Libre|

#### 5.4.2. Sub-item 2: Services, Formalities, or Procedures Using SDAs

ID: GUIDE-TA-SPECIFIC-REC-SUBITEM2-01

- Purp: Detail where the SDAs are used.

|Aspect|Sub-aspect|Description|Value Type|
|-|-|-|-|
|**1. Servicio, trámite... en que se utiliza el SDA**|**1.1 Nombre del SDA**|Ref: GUIDE-TA-SPECIFIC-REC-INFO-01.|Libre|
||**1.2 Identificador interno del SDA**|Ref: GUIDE-TA-SPECIFIC-REC-INFO-01.|Libre|
||**1.3 Nombre del servicio, trámite...**|Must be consistent with info published under Art. 7, literal h) of Transparency Law.|Libre|
|**2. Descripción del servicio... o enlace a Chileatiende**|**2.1 Descripción del servicio...**|Must be consistent with info published under Art. 7, literal h).|Libre|
||**2.2. Enlace a Chileatiende**|Must be consistent with info published under Art. 7, literal h).|Libre|
|**3. Unidad que utiliza el SDA**|**3.1 Nombre unidad, oficina...**|The unit that uses the SDA (not the IT/dev unit). Must be consistent with info published under Art. 7, literal a).|Libre|
|**4. Enlace adicional**|**4.1 Enlace institucional...**|A different link than the Chileatiende one.|Libre|
|**5. Individualizar el acto... que estableció el servicio...**|**5.1 Tipo de acto**|Example: Decreto.|Libre|
||**5.2 Denominación del acto**||Libre|
||**5.3 Número del acto**||Libre|
||**5.4 Fecha del acto**||Libre|
||**5.5 Enlace al texto íntegro del acto**||Libre|

#### 5.4.3. Sub-item 3: SDA Specifications

ID: GUIDE-TA-SPECIFIC-REC-SUBITEM3-01

- Purp: Provide info on the general functioning of SDAs.

|Aspect|Sub-aspect|Description|Value Type|
|-|-|-|-|
|**1. Objetivo del SDA**|**1.1 Nombre del SDA**|Ref: GUIDE-TA-SPECIFIC-REC-INFO-01.|Libre|
||**1.2 Identificador interno del SDA**|Ref: GUIDE-TA-SPECIFIC-REC-INFO-01.|Libre|
||**1.3 Propósito del SDA...**|Why does the org use the SDA? How does it assist/replace decisions?|Libre|
|**2. Funcionamiento del SDA**|**2.1 Funcionamiento o lógica del SDA...**|How does the SDA work/achieve results? How is it incorporated into decision-making? Related to Art. 14 ter of Law N°19.628.|Libre|
||**2.2 SDA categoriza, clasifica o elabora perfiles...**|Does the SDA categorize, classify, or profile individuals?|Sí/No|
||**2.3 ...Categorías**|If "Sí", list the categories or profiles.|Libre|
||**2.4 ...Motivos**|If "Sí", explain why the categories are relevant.|Libre|
||**2.5 ...Metodología**|If "Sí", explain the method for assigning categories.|Libre|
||**2.6 ...Efecto variables**|If "Sí", explain the effect of main variables in category assignment.|Libre|
||**2.7 Consecuencias previstas...**|Foreseen consequences of data processing for the data subject. Related to Art. 14 ter of Law N°19.628.|Libre|
||**2.8 Circunstancias... para decisión negativa.**|Factors leading to a negative decision (e.g., rejection of a subsidy).|Libre|
||**2.9 Método o modelo del SDA utilizado.**||Libre|
|**3. Categorías de datos...**|**3.1 Utilización de datos personales.**|Does the SDA use personal data?|Sí/No|
||**3.2 Utilización de datos personales sensibles.**|Does the SDA use sensitive personal data?|Sí/No|
||**3.3 Categorías o clases de datos...**|If "Sí" to 3.1 or 3.2, list the categories of data used.|Libre|
||**3.4 Evaluaciones de impacto en protección de datos...**|Info/links to data protection impact assessments (risks, mitigation). Related to Art. 15 ter of Law N°19.628.|Libre|
||**3.5 Otras evaluaciones de impacto**|Info/links to other impact assessments (e.g., human rights).|Libre|
||**3.6 Conjuntos de datos de entrenamiento...**|Info about training, validation, and test datasets and their sources.|Libre|
||**3.7 Política de privacidad...**|Link to the privacy policy. Related to Art. 14 ter of Law N°19.628.|Libre|

### 5.5. Other Considerations for Proactive Publication

ID: GUIDE-TA-SPECIFIC-REC-OTHER-01

- Cpt: Information subject to secrecy/reservation clauses.
  - Rec-1: Evaluate if publication is possible with less detail to avoid harm.
  - Rec-2: If not possible, apply the Principle of Divisibility and state it explicitly.
- Cpt: Update frequency.
  - Rec: Monthly, within the first ten working days of each month (same as active transparency rules).
- Cpt: Enabling the "Transparencia Algorítmica" item in the Transparency Portal.
  - Proc: Send an email request to <contacto@cplt.cl>.
- Cpt: Publication templates.
  - Fnd: Yes, they are available.

## 6. Summary Scheme for Application of Recommendations

ID: GUIDE-TA-SUMMARY-SCHEME-01
Purp: A flowchart to determine how to apply the CPLT recommendations.

- Proc: Decision-Flow.
  - 1. Cpt: Initial State Check.
    - Cond: "¿En qué estado se encuentra el SDA en el organismo?"
    - Path-A: "El SDA está en desarrollo, operando en entorno de prueba, piloto, uso simulado o similar."
      - Res: "Las Recomendaciones no le resultan aplicables."
    - Path-B: "El SDA se encuentra en funcionamiento en el organismo."
      - Act: Proceed to step 2.
  - 2. Cpt: SDA Type Check.
    - Cond: "¿A qué tipo o clase de SDA corresponde?"
    - Path-A: "SDA externo."
      - Act: Proceed to step 3.
    - Path-B: "SDA que tiene características como externo e interno."
      - Act: Proceed to step 3.
    - Path-C: "SDA interno, pues no tiene vinculación con la ciudadanía."
      - Res: "Aplican sólo las recomendaciones generales. No aplica la publicación proactiva de información sobre el SDA (recomendaciones específicas)."
  - 3. Cpt: Impact Check.
    - Cond: "¿El SDA tiene efectos en los dd.ff de las personas o en su acceso a servicios, programas, subsidios, fondos u otros beneficios?"
    - Path-A: "Sí, tiene dichos efectos."
      - Act: Proceed to Final Result.
    - Path-B: "No tiene dichos efectos."
      - Res: "Aplican sólo las recomendaciones generales. No aplica la publicación proactiva de información sobre el SDA (recomendaciones específicas)."
  - 4. Cpt: Final Result.
    - Res: "Aplican las Recomendaciones en su integridad: las recomendaciones generales y específicas correspondientes a la publicación proactiva de información sobre el SDA."
