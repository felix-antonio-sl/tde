# Herramientas de Diagnóstico y Datos

Este último grupo contiene herramientas y datos para diagnosticar el estado actual de la digitalización y gestionar la información de proyectos.

## GUIA-CPAT: CATÁLOGO PROCEDIMIENTOS ADM. Y TRAMITACIONES

ID: KB-066-TDE-GUIA-CPAT
Version: 1.0.0
Status: Draft
Human-Creator: STSador
Human-Editor: STSador
Model-Collaborator: IA-GEMINI
Creation-Date: 2025-07-06
Modification-Date: 2025-07-06
Source: kb_066_tde_guia_cpat.md
Ctx: Guía para el uso de la plataforma Catálogo de Procedimientos Administrativos y Tramitaciones (CPAT) en el marco de la Ley de Transformación Digital del Estado.

---

BEGIN_LLM_INSTRUCTIONS

You are an AI agent consuming a Structured Telegraphic Style (STS) artifact. Your primary task is to parse and reason over THIS document with absolute fidelity, using only the rules defined below. This artifact is a self-contained source of truth.

1. **Core Objective**: Maintain perfect fidelity to the information (`meat`) and structure (`skeleton`). Do not summarize, interpret, or infer information not explicitly present. Prohib: Applying these rules to artifact creation or translation tasks; they are exclusively for consumption.

2. **Conceptual Metaphors**:
    - `meat`: Essential information, data, and facts. Must be preserved with zero loss.
    - `skeleton`: Logical structure (headers, IDs, lists, tables). This is also `meat` and must be preserved.
    - `fat`: Non-essential verbiage (filler words, rhetoric, stylistic prose). Must be ignored during reasoning as it has no informational value.

3. **Lexicon Mode & Expansion**: This document uses an **Abbreviated Lexicon**. You MUST treat the following keywords as valid and expand them according to this mapping:
    - `Act:` -> `Action:`
    - `Warn:` -> `Warning:`
    - `Cause:` -> `Cause:`
    - `Cpt:` -> `Concept:`
    - `Cond:` -> `Condition:`
    - `Ctx:` -> `Context:`
    - `Def:` -> `Definition:`
    - `Dep:` -> `Dependency:`
    - `Dest:` -> `Destination:`
    - `Dln:` -> `Deadline:`
    - `Ex:` -> `Example:`
    - `Fnd:` -> `Foundation:`
    - `ID:` -> `ID:`
    - `Instr:` -> `Instruction:`
    - `Just:` -> `Justification:`
    - `Mech:` -> `Mechanism:`
    - `Mssn:` -> `Mission:`
    - `Mdl:` -> `Model:`
    - `Nat:` -> `Nature:`
    - `Obj:` -> `Objective:`
    - `Proc:` -> `Process:`
    - `Prohib:` -> `Prohibition:`
    - `Purp:` -> `Purpose:`
    - `Rec:` -> `Recommendation:`
    - `Ref:` -> `Reference:`
    - `Req:` -> `Requirement:`
    - `Res:` -> `Result:`
    - `Resp:` -> `Responsible:`
    - `Src:` -> `Source:`

4. **Reference (`Ref:`) Policy**:
    - `Ref:` is used for **internal cross-references only**.
    - It MUST point to an `ID:` that exists within THIS document.
    - You MUST NOT interpret a `Ref:` as a link to an external document or resource. Mentions of other documents are purely contextual (`Ctx:`).

5. **Language Invariance Policy**:
    - The `Keywords` in the lexicon are a fixed control vocabulary in English.
    - All `EssentialData` (the content following a `Keyword:`) MUST be preserved in its original language. Do not translate it.

END_LLM_INSTRUCTIONS

---

### 1. Propósito de la Guía

ID: KB-066-PROPOSITO-01
Purp: Apoyar a instituciones en uso de plataforma Catálogo de Procedimientos Administrativos y Tramitaciones (CPAT).
Ctx: Fase de preparación de la Ley de Transformación Digital del Estado (Ley N° 21.180).
Obj: Facilitar la identificación y caracterización de procedimientos administrativos y otras tramitaciones.
Dest: Equipos institucionales vinculados a implementación Ley N° 21.180; Coordinador/a de Transformación Digital.

### 2. Contexto: Transformación Digital del Estado (TDE)

ID: KB-066-CONTEXTO-TDE-01
Fnd: Ley N° 21.180 sobre Transformación Digital del Estado.
Mssn: Repensar cumplimiento de mandato y entrega de servicios.
Obj: Poner foco en necesidades de las personas por sobre necesidades burocráticas.
Mech: Rediseño de procesos usando tecnología, datos e innovación para simplificar acceso.
Req: Todos los procedimientos administrativos deben contar con soporte electrónico.
Req: Servicios del Estado deben ser preferentemente digitales.
Resp: Secretaría de Gobierno Digital (SegDig), dependiente de Subsecretaría de Hacienda.

- Cpt: Funciones de SegDig.
  - Resp: Proponer Estrategia de Gobierno Digital.
  - Resp: Coordinar implementación de la estrategia.
  - Resp: Asesorar intersectorialmente en uso estratégico de tecnologías digitales, datos e información.
  - Resp: Desarrollar y operar plataformas y servicios compartidos.
- Cpt: Objetivos de la Digitalización.
  - Res: Otorgar mayor certeza, seguridad y celeridad.
  - Res: Permitir desarrollo de políticas públicas y gobierno basado en datos.
  - Res: Aumentar transparencia de procesos y actuaciones del Estado.
- Cpt: Implementación.
  - Nat: Gradual.
  - Cond: Conforme a grupos del DFL Nº1 MinSegPres y plazos de Ley N°21.464.
  - Cpt: Fase Inicial (Preparación).
    - Obj: Que instituciones identifiquen los procedimientos administrativos derivados de su mandato.
    - Res: Planificar tránsito a soporte electrónico.
    - Res: Establecer línea base y diagnóstico.

#### 2.1. Tabla Resumen de Implementación TDE

ID: KB-066-CONTEXTO-TDE-TABLA-01
Src: Cuadro resumen DFL Nº1 MinSegPres y Ley N°21.464.

| Año | 2022 | 2023 | 2024 | 2025 | 2026 | 2027 |
|---|---|---|---|---|---|---|
| **GRUPO A** | Cpt: Preparación | Cpt: Comunicaciones Oficiales | Cpt: Ingreso electrónico de solicitudes | Cpt: Interoperabilidad | Cpt: Notificaciones electrónicas | Cpt: Expedientes electrónicos |
| **GRUPO B**| Cpt: Preparación | Cpt: Preparación | Cpt: Comunicaciones Oficiales | Cpt: Ingreso electrónico de solicitudes | Cpt: Interoperabilidad | Cpt: Digitalización de solicitudes en papel |

### 3. Conceptos Clave

ID: KB-066-CONCEPTOS-CLAVE-01
Fnd: Ley N° 19.880, Bases de los Procedimientos Administrativos.
Ctx: Ley 21.180 modifica Ley 19.880 para establecer que procedimientos deben expresarse por medios electrónicos.

#### 3.1. Acto Administrativo

ID: KB-066-CONCEPTO-ACTO-ADM-01
Src: Art. 3°, Ley N°19.880.
Def: "Decisiones escritas que adopte la Administración".
Def: "Decisiones formales que emitan los órganos de la Administración del Estado en las cuales se contienen declaraciones de voluntad, realizadas en el ejercicio de una potestad pública".
Cpt: Formas Típicas.

- Cpt: Decreto Supremo.
  - Def: Orden escrita dictada por Pdte. de la República o Ministro ("Por orden del Pdte.") sobre asuntos de competencia propia.
- Cpt: Resolución.
  - Def: Acto análogo dictado por autoridades adm. con poder de decisión.
- Cpt: Dictamen.
  - Def: Declaraciones de juicio, constancia o conocimiento realizadas por órganos Adm. en ejercicio de sus competencias.
Ctx: Jurisprudencia Corte Suprema (5 de agosto de 2020, rol N° 8857-2019) indica que oficios ordinarios e incluso correos electrónicos pueden ser considerados actos administrativos.

#### 3.2. Procedimiento Administrativo

ID: KB-066-CONCEPTO-PROC-ADM-01
Src: Art. 18, Ley N°19.880.
Def: "Sucesión de actos trámite vinculados entre sí, emanados de la Administración y, en su caso, de particulares interesados, que tiene por finalidad producir un acto administrativo terminal".
Req: Todo procedimiento debe constar en un expediente electrónico.
Cpt: Contenido del Expediente Electrónico.

- Req: Documentos de interesados, terceros, otros órganos (con fecha/hora de recepción, en orden).
- Req: Actuaciones, documentos, resoluciones del órgano adm. (con fecha/hora de envío, en orden).
- Req: Notificaciones y comunicaciones.
Cpt: Formato de Ingreso.
- Req: Documentos electrónicos o formatos/medios electrónicos a través de plataformas institucionales.

#### 3.3. Etapas del Procedimiento Administrativo

ID: KB-066-ETAPAS-PROC-ADM-01
Src: Art. 18 y ss., Ley N°19.880.
Mdl: Inicio, Instrucción, Finalización.

##### 3.3.1. Inicio

ID: KB-066-ETAPA-INICIO-01
Src: Art. 28 y ss., Ley N°19.880.
Cpt: Modalidades.

- Cpt: De oficio. Def: Por iniciativa del propio órgano.
- Cpt: A solicitud de parte. Def: Por solicitud de persona interesada.
Cpt: Causas de Inicio de Oficio.
- Cause: Orden superior.
- Cause: Petición de otro órgano de la Administración.
- Cause: Por denuncia.
Cpt: Requisitos de Solicitud de Parte.
- Req: Nombre y apellidos del interesado/apoderado.
- Req: Medio electrónico para notificaciones.
- Req: Hechos, razones y peticiones.
- Req: Lugar y fecha.
- Req: Firma o acreditación de voluntad.
- Req: Órgano al que se dirige.
- Req: Autorización para remitir datos sensibles en poder de otros órganos.

##### 3.3.2. Instrucción

ID: KB-066-ETAPA-INSTRUCCION-01
Src: Art. 34 y ss., Ley N°19.880.
Def: Actos necesarios para la determinación, conocimiento y comprobación de los datos para pronunciar el acto final.
Ctx: Se realizan de oficio, pero interesados pueden proponer actuaciones.

##### 3.3.3. Finalización

ID: KB-066-ETAPA-FINALIZACION-01
Src: Art. 40 y ss., Ley N°19.880.
Def: Conclusión del procedimiento mediante un acto terminal.
Cpt: Finalización Normal.

- Def: Resolución final que decide sobre las cuestiones planteadas.
Cpt: Finalización Anormal.
- Cause: Renuncia y desistimiento (Art. 42).
- Cause: Abandono por inactividad del interesado > 30 días (Art. 43).

#### 3.4. Procedimiento Administrativo Electrónico y Normas Técnicas

ID: KB-066-PROC-ADM-ELEC-01
Req: Cumplir con 6 Normas Técnicas para dar cumplimiento a la Ley TDE.

##### 3.4.1. Definiciones de Normas Técnicas (NT)

ID: KB-066-NORMAS-TECNICAS-01
Purp: Definir estándares para la implementación de la TDE.

- Cpt: NT de Autenticación.
  - ID: KB-066-NORMA-AUTENTICACION-01
  - Purp: Establecer cómo implementar/integrar mecanismos oficiales de autenticación en plataformas.
- Cpt: NT de Interoperabilidad.
  - ID: KB-066-NORMA-INTEROP-01
  - Purp: Definir estándares, protocolos y herramientas para interoperar datos, documentos y expedientes electrónicos.
- Cpt: NT de Calidad de Plataformas.
  - ID: KB-066-NORMA-CALIDAD-PLATAFORMAS-01
  - Purp: Describir cómo mitigar obsolescencia, mantener continuidad, medir SLAs, aumentar resiliencia y brindar soporte en plataformas.
- Cpt: NT de Documentos y Expedientes Electrónicos.
  - ID: KB-066-NORMA-DOCS-EXPEDIENTES-01
  - Purp: Definir estándares, formatos y metadatos para administrar documentos y expedientes electrónicos.
- Cpt: NT de Notificaciones.
  - ID: KB-066-NORMA-NOTIFICACIONES-01
  - Purp: Detallar funcionamiento de Plataforma de Notificaciones y cómo practicar notificaciones electrónicas.
- Cpt: NT de Seguridad.
  - ID: KB-066-NORMA-SEGURIDAD-01
  - Purp: Definir estándares y directrices de seguridad de la información y ciberseguridad.

### 4. Plataforma CPAT

ID: KB-066-PLATAFORMA-CPAT-01
Cpt: URL. Def: <https://cpat.gob.cl/>
Cpt: Rol de CPAT.

- Def: Herramienta de apoyo a implementación Ley 21.180.
- Ctx: Especialmente en fase de preparación.
- Purp: Aportar visión integral del universo y características de los procedimientos a transitar a soporte electrónico.

#### 4.1. Funcionamiento

ID: KB-066-CPAT-FUNCIONAMIENTO-01
Nat: Herramienta viva, dinámica y colaborativa.
Cpt: Características.

- Mech: Instancias periódicas para que instituciones actualicen su información.
- Mech: Perfiles de acceso con ClaveÚnica para trabajo conjunto.
- Mech: Nómina inicial validada por Autoridad Institucional.
- Mech: Cambios futuros validados por Coordinador/a de TDE.
Cpt: Perfiles de Usuario.
- Cpt: Perfil-Coordinador-TDE. Cond: Máximo 1 por institución.
- Cpt: Perfil-Autoridad-Institucional. Cond: Máximo 1 por institución.
- Cpt: Perfil-Editor. Cond: Sin límite.
- Cpt: Perfil-Invitado-Institucional. Cond: Sin límite.

#### 4.2. Módulos de la Plataforma

ID: KB-066-CPAT-MODULOS-01
Cpt: Lista de Módulos.

- Cpt: Módulo-Inicio. Cpt: Instrucciones de uso y cifras relevantes.
- Cpt: Módulo-Equipo-Trabajo. Cpt: Gestión de usuarios por perfil CTD.
- Cpt: Módulo-Registro. Cpt: Informar y caracterizar procedimientos y tramitaciones.
- Cpt: Módulo-Transacciones. Cpt: Informar demanda mensualizada por canal.
- Cpt: Módulo-Reportes. Cpt: Descargar reportes de la información institucional.
- Cpt: Módulo-Recursos-Informativos. Cpt: Documentos de interés del proyecto CPAT.
- Cpt: Módulo-Ayuda. Cpt: Preguntas frecuentes.

#### 4.3. Contenido y Estructura de Registros

ID: KB-066-CPAT-CONTENIDO-01
Purp: Individualizar y caracterizar registros.

##### 4.3.1. Tipos de Registro

ID: KB-066-CPAT-TIPOS-REGISTRO-01
Fnd: Distinción basada en concepto de procedimiento administrativo de Ley N°19.880.

- Cpt: Tipo A - Proc. Adm. Función Común. Ex: Compras públicas, gestión de personas, presupuesto, auditorías.
- Cpt: Tipo B - Proc. Adm. Función Específica. Ex: Propios del quehacer misional de la institución.
- Cpt: Tipo C - Otras Tramitaciones. Ex: No clasifican como procedimiento administrativo.

##### 4.3.2. Caracterización de Registros (Formulario SFD)

ID: KB-066-CPAT-CARACTERIZACION-01
Purp: Describir cada registro a través de un formulario con múltiples secciones.

BEGIN_EMBEDDED_BLOCK:: GUIDE-SFD-STS-MASTER-01 FORM-CPAT-REGISTRO-01

## Formulario de Caracterización de Registros CPAT

ID: FORM-CPAT-REGISTRO-01
Version: 1.0.0
Status: Published
Ref-SFD-Guide: GUIDE-SFD-STS-MASTER-01

#### Sección: Identificación

ID: FORM-CPAT-S1-IDENTIFICACION-01

##### Nombre del Registro

ID: FORM-CPAT-S1-NOMBRE-01
Field-Label: "Nombre"
Field-Type: Text

##### Descripción

ID: FORM-CPAT-S1-DESCRIPCION-01
Field-Label: "Descripción"
Field-Type: Text

##### Área Responsable

ID: FORM-CPAT-S1-AREA-RESP-01
Field-Label: "Área responsable"
Field-Type: Select
Field-Constraint: "Req: mandatory."

##### Cargo del Responsable

ID: FORM-CPAT-S1-CARGO-RESP-01
Field-Label: "Cargo del o la responsable"
Field-Type: Text

##### Acto de Inicio

ID: FORM-CPAT-S1-ACTO-INICIO-01
Field-Label: "Acto de inicio"
Field-Type: Text

##### Acto de Término

ID: FORM-CPAT-S1-ACTO-TERMINO-01
Field-Label: "Acto de término"
Field-Type: Text

##### Producto Institucional Relacionado

ID: FORM-CPAT-S1-PRODUCTO-REL-01
Field-Label: "Producto institucional relacionado"
Field-Type: Select
Field-Constraint: "Req: mandatory."

#### Sección: Marco Normativo

ID: FORM-CPAT-S2-NORMATIVO-01

##### Número Ley

ID: FORM-CPAT-S2-NUM-LEY-01
Field-Label: "Número Ley"
Field-Type: Text

##### URL de la Ley

ID: FORM-CPAT-S2-URL-LEY-01
Field-Label: "URL de la Ley"
Field-Type: Text
Field-Constraint: "Format: url."

##### Otras Fuentes Normativas

ID: FORM-CPAT-S2-OTRAS-FUENTES-01
Field-Label: "Otras fuentes normativas"
Field-Type: Select
Field-Constraint: "Req: mandatory."

#### Sección: Usuarios

ID: FORM-CPAT-S3-USUARIOS-01

##### Pago Asociado

ID: FORM-CPAT-S3-PAGO-01
Field-Label: "Pago asociado"
Field-Type: Select
Field-Constraint: "Req: mandatory."

##### Tipo de Usuario/a

ID: FORM-CPAT-S3-TIPO-USUARIO-01
Field-Label: "Tipo de usuario/a"
Field-Type: Select
Field-Constraint: "Req: mandatory."

##### Segmento de Usuarios/as

ID: FORM-CPAT-S3-SEGMENTO-USUARIO-01
Field-Label: "Segmento de usuarios/as"
Field-Type: Select
Field-Constraint: "Req: mandatory."

##### Relación con Programa Social

ID: FORM-CPAT-S3-PROG-SOCIAL-01
Field-Label: "Relación con programa social"
Field-Type: Select
Field-Constraint: "Req: mandatory."

##### Disponibilidad para Realización

ID: FORM-CPAT-S3-DISPONIBILIDAD-01
Field-Label: "Disponibilidad para su realización"
Field-Type: Select
Field-Constraint: "Req: mandatory."

#### Sección: Soporte Electrónico

ID: FORM-CPAT-S4-SOPORTE-ELEC-01

##### Nivel de Digitalización

ID: FORM-CPAT-S4-NIVEL-DIG-01
Field-Label: "Nivel de digitalización"
Field-Type: Select
Field-Constraint: "Req: mandatory."

##### Fecha de Digitalización

ID: FORM-CPAT-S4-FECHA-DIG-01
Field-Label: "Fecha de digitalización"
Field-Type: Select
Field-Constraint: "Req: mandatory."

##### Canal(es) Transaccional(es)

ID: FORM-CPAT-S4-CANALES-TRANS-01
Field-Label: "Canal(es) transaccional(es)"
Field-Type: Checkbox-Group
Field-Constraint: "Min-Selections: 1."

##### Tipo de Expediente

ID: FORM-CPAT-S4-TIPO-EXPE-01
Field-Label: "Tipo de expediente"
Field-Type: Select
Field-Constraint: "Req: mandatory."

##### Acceso al Expediente por Interesados

ID: FORM-CPAT-S4-ACCESO-EXPE-01
Field-Label: "Acceso al expediente electrónico por interesados/as"
Field-Type: Select
Field-Constraint: "Req: mandatory."

##### URL

ID: FORM-CPAT-S4-URL-PROC-01
Field-Label: "URL"
Field-Type: Text
Field-Constraint: "Format: url."

##### Ficha ChileAtiende Relacionada

ID: FORM-CPAT-S4-FICHA-CHILEATIENDE-01
Field-Label: "Ficha ChileAtiende relacionada"
Field-Type: Select
Field-Constraint: "Req: mandatory."

##### Número de Plataformas Electrónicas

ID: FORM-CPAT-S4-NUM-PLATAFORMAS-01
Field-Label: "Número de plataformas electrónicas"
Field-Type: Number
Field-Constraint: "Min-Val: 0."

##### Alcance de las Plataformas

ID: FORM-CPAT-S4-ALCANCE-PLATAFORMAS-01
Field-Label: "Alcance de las plataformas"
Field-Type: Select
Field-Constraint: "Req: mandatory."

##### Plataforma o Sistema Utilizado

ID: FORM-CPAT-S4-SISTEMA-UTILIZADO-01
Field-Label: "Plataforma o sistema utilizado"
Field-Type: Checkbox-Group

#### Sección: Identidad Digital

ID: FORM-CPAT-S5-IDENTIDAD-DIGITAL-01

##### Mecanismo de Autenticación (Usuarios)

ID: FORM-CPAT-S5-AUTH-USER-01
Field-Label: "Mecanismo de autenticación para usuarios"
Field-Type: Checkbox-Group

##### Mecanismo de Autenticación (Funcionarios)

ID: FORM-CPAT-S5-AUTH-FUNC-01
Field-Label: "Mecanismo de autenticación para funcionarios"
Field-Type: Select
Field-Constraint: "Req: mandatory."

##### Firma Electrónica Avanzada

ID: FORM-CPAT-S5-FIRMA-AVANZADA-01
Field-Label: "Firma electrónica Avanzada"
Field-Type: Select
Field-Constraint: "Req: mandatory."

#### Sección: Notificaciones

ID: FORM-CPAT-S6-NOTIFICACIONES-01

##### Notificación Practicada

ID: FORM-CPAT-S6-NOTIF-PRACTICADA-01
Field-Label: "Notificación(es) practicada(s)"
Field-Type: Select
Field-Constraint: "Req: mandatory."

##### Etapa de Notificación

ID: FORM-CPAT-S6-ETAPA-NOTIF-01
Field-Label: "Etapa de notificación"
Field-Type: Checkbox-Group
Field-Logic: "Cond: (Ref: FORM-CPAT-S6-NOTIF-PRACTICADA-01.Value != 'No') -> Visibility: show."

##### Medio Utilizado para Notificar

ID: FORM-CPAT-S6-MEDIO-NOTIF-01
Field-Label: "Medio utilizado para notificar"
Field-Type: Select
Field-Constraint: "Req: mandatory."
Field-Logic: "Cond: (Ref: FORM-CPAT-S6-NOTIF-PRACTICADA-01.Value != 'No') -> Visibility: show."

#### Sección: Datos, Documentos e Interoperabilidad

ID: FORM-CPAT-S7-DATOS-INTEROP-01

##### Pregunta Habilitante (Requiere Datos)

ID: FORM-CPAT-S7-REQ-DATOS-01
Field-Label: "Pregunta habilitante sobre requerir datos de otros órganos"
Field-Type: Select
Field-Constraint: "Req: mandatory."

##### Medio para Obtener Dato/Documento

ID: FORM-CPAT-S7-MEDIO-OBTENER-DATO-01
Field-Label: "Medio utilizado para obtener dato/documento"
Field-Type: Select
Field-Constraint: "Req: mandatory."
Field-Logic: "Cond: (Ref: FORM-CPAT-S7-REQ-DATOS-01.Value == 'Sí') -> Visibility: show."

##### Medio para Interoperar

ID: FORM-CPAT-S7-MEDIO-INTEROP-01
Field-Label: "Medio utilizado para interoperar"
Field-Type: Select
Field-Constraint: "Req: mandatory."
Field-Logic: "Cond: (Ref: FORM-CPAT-S7-MEDIO-OBTENER-DATO-01.Value == 'Hay interoperabilidad electrónica con la institución') -> Visibility: show."

##### Institución con la que Interopera

ID: FORM-CPAT-S7-INST-INTEROP-01
Field-Label: "Institución con la que se interopera"
Field-Type: Select
Field-Constraint: "Req: mandatory."
Field-Logic: "Cond: (Ref: FORM-CPAT-S7-MEDIO-OBTENER-DATO-01.Value == 'Hay interoperabilidad electrónica con la institución') -> Visibility: show."

##### Nombre del Dato o Set de Datos

ID: FORM-CPAT-S7-NOMBRE-DATO-01
Field-Label: "Nombre del dato o set de datos"
Field-Type: Text
Field-Logic: "Cond: (Ref: FORM-CPAT-S7-MEDIO-OBTENER-DATO-01.Value == 'Hay interoperabilidad electrónica con la institución') -> Visibility: show."

##### Documento(s) Notarial(es)

ID: FORM-CPAT-S7-DOC-NOTARIAL-01
Field-Label: "Documento(s) notarial(es)"
Field-Type: Select
Field-Constraint: "Req: mandatory."

##### Medio para Comunicaciones Oficiales

ID: FORM-CPAT-S7-MEDIO-COM-OFICIAL-01
Field-Label: "Medio para comunicaciones oficiales"
Field-Type: Select
Field-Constraint: "Req: mandatory."

END_EMBEDDED_BLOCK:: FORM-CPAT-REGISTRO-01

##### 4.3.3. Transacciones

ID: KB-066-CPAT-TRANSACCIONES-01
Purp: Recopilar información de demanda.
Def: Procedimiento administrativo o tramitación finalizado en un mes y canal determinados.
Cpt: Lógica Contable.

- Instr: Se contabiliza en el mes en que finaliza, no cuando inicia.
- Ctx: Finalización ocurre con el acto administrativo terminal. Ref: KB-066-CONCEPTO-ACTO-ADM-01.
Cpt: Canales Transaccionales.
- Cpt: Digital. Ex: email, RRSS, apps, etc.
- Cpt: Presencial. Ex: sucursales, correo postal, tótems, etc.
- Cpt: Telefónico. Ex: mesa de ayuda, SMS, etc.
Cpt: Valores a Informar.
- Req: Números enteros (desde 0).
- Req: "sin información" (cuando no se puede determinar).

### 5. Guía de Implementación CPAT

ID: KB-066-IMPLEMENTACION-CPAT-01

#### 5.1. Cálculo del Nivel de Soporte Electrónico

ID: KB-066-IMPL-CALCULO-SOPORTE-01
Obj: Visualizar y monitorear el grado de avance hacia el soporte electrónico.
Fnd: Ley 19.880 y las seis Normas Técnicas. Ref: KB-066-NORMAS-TECNICAS-01.
Warn: Implementación integral de la Ley TDE considera aspectos adicionales no consultados en CPAT.

##### 5.1.1. Criterio 1: Autenticación

ID: KB-066-CALCULO-CRITERIO-AUTENTICACION-01
Ref: KB-066-NORMA-AUTENTICACION-01.
Req: Utilizar mecanismos oficiales de autenticación para acceso de interesados.
Cpt: Mecanismos Oficiales.

- Cpt: ClaveÚnica. Dest: Personas naturales.
- Cpt: Clave Tributaria. Dest: Personas jurídicas.
Cpt: Mapeo a CPAT.
- Ref: FORM-CPAT-S5-AUTH-USER-01.
- Cond: Cumplimiento si la selección es "Utiliza ClaveÚnica" o "Utiliza Clave Tributaria".

##### 5.1.2. Criterio 2: Interoperabilidad

ID: KB-066-CALCULO-CRITERIO-INTEROP-01
Ref: KB-066-NORMA-INTEROP-01.
Fnd: Medios electrónicos deben ser capaces de interactuar y operar entre sí (Principio de Interoperabilidad).
Fnd: Órganos del Estado deben cooperar en utilización de medios electrónicos (Principio de Cooperación).
Def: Intercambiar datos/docs/expedientes entre dos órganos a través de la Red de Interoperabilidad del Estado.
Cpt: Mapeo a CPAT.

- Ref: FORM-CPAT-S7-DATOS-INTEROP-01.
- Cond: Cumplimiento si se cumple la siguiente secuencia lógica:
  - Cond-1: (Ref: FORM-CPAT-S7-REQ-DATOS-01) es "Sí".
  - Cond-2: (Ref: FORM-CPAT-S7-MEDIO-OBTENER-DATO-01) es "Hay interoperabilidad electrónica con la institución".
  - Cond-3: (Ref: FORM-CPAT-S7-MEDIO-INTEROP-01) es "Utiliza la Red de Interoperabilidad del Estado o utiliza su estándar".

##### 5.1.3. Criterio 3: Notificaciones

ID: KB-066-CALCULO-CRITERIO-NOTIFICACIONES-01
Ref: KB-066-NORMA-NOTIFICACIONES-01.
Req: Notificaciones se practicarán por medios electrónicos usando la Plataforma de Notificaciones (Art. 46, Ley 19.880).
Cpt: Mapeo a CPAT.

- Ref: FORM-CPAT-S6-NOTIFICACIONES-01.
- Cond: Cumplimiento si se cumple la siguiente secuencia lógica:
  - Cond-1: (Ref: FORM-CPAT-S6-NOTIF-PRACTICADA-01) es "Sí".
  - Cond-2: (Ref: FORM-CPAT-S6-MEDIO-NOTIF-01) es "Notificación electrónica".

##### 5.1.4. Criterio 4: Plataformas

ID: KB-066-CALCULO-CRITERIO-PLATAFORMAS-01
Ref: KB-066-NORMA-CALIDAD-PLATAFORMAS-01.
Req: Órganos obligados a disponer y usar plataformas electrónicas para llevar expedientes (Art. 19, Ley 19.880).
Def: Software, datos e infraestructura que sustenta procesos o procedimientos.
Cpt: Mapeo a CPAT.

- Ref: FORM-CPAT-S4-SOPORTE-ELEC-01.
- Cond: Cumplimiento si se cumplen TODAS las siguientes condiciones:
  - Cond-1: (Ref: FORM-CPAT-S4-NIVEL-DIG-01) es "Nivel 4" o "Nivel 5".
  - Cond-2: (Ref: FORM-CPAT-S4-NUM-PLATAFORMAS-01) > 0.
  - Cond-3: (Ref: FORM-CPAT-S4-ALCANCE-PLATAFORMAS-01) es "Las plataformas electrónicas soportan todas las etapas...".

##### 5.1.5. Criterio 5: Expediente Electrónico

ID: KB-066-CALCULO-CRITERIO-EXPEDIENTE-01
Ref: KB-066-NORMA-DOCS-EXPEDIENTES-01.
Req: Todo procedimiento debe constar en expediente electrónico (Art. 18, Ley 19.880).
Def: Unidad documental con ID único, estructurada (índices, docs, metadatos), generada en plataforma electrónica.
Cpt: Mapeo a CPAT.

- Ref: FORM-CPAT-S4-SOPORTE-ELEC-01.
- Cond: Cumplimiento si se cumple la siguiente secuencia lógica:
  - Cond-1: (Ref: FORM-CPAT-S4-TIPO-EXPE-01) es "Expediente con documentos en formato electrónico".
  - Cond-2: (Ref: FORM-CPAT-S4-ACCESO-EXPE-01) es "Sí, los(as) interesados(as) tienen acceso...".

##### 5.1.6. Criterio 6: Comunicaciones Oficiales

ID: KB-066-CALCULO-CRITERIO-COM-OFICIALES-01
Ref: KB-066-NORMA-DOCS-EXPEDIENTES-01.
Req: Toda comunicación entre órganos será por medios electrónicos (Art. 9, Ley 19.880).
Req: Comunicaciones oficiales se registrarán en plataforma destinada (DocDigital) (Art. 19, Ley 19.880).
Def: Mensaje entre órganos, suscrito por autoridad, emitido/recibido por medio electrónico formal.
Cpt: Mapeo a CPAT.

- Ref: FORM-CPAT-S7-MEDIO-COM-OFICIAL-01.
- Cond: Cumplimiento si la selección es "Sí, realiza envíos por medio de la plataforma DocDigital" o "Sí, realiza envíos por medios electrónicos propios y DocDigital".

#### 5.2. Primeros Pasos

ID: KB-066-IMPL-PRIMEROS-PASOS-01
Purp: Buenas prácticas para iniciar el trabajo de identificación de procedimientos, previo al uso de la plataforma CPAT.

- Rec: Conformar equipo de trabajo representativo del quehacer institucional.
- Rec: Revisar el marco normativo aplicable a la institución.
- Rec: Utilizar insumos como Formulario A1 y productos estratégicos.
- Rec: Usar levantamientos de procesos existentes como insumo.

#### 5.3. Hoja de Ruta

ID: KB-066-IMPL-HOJA-DE-RUTA-01

- Cpt: Etapa 1A (Grupo A). Dln: Jun22-Dic23. Act: Gobierno central informa procedimientos.
- Cpt: Etapa 1B (Grupos B-C). Dln: Jun22-Dic23. Act: Gobiernos regionales y municipalidades informan procedimientos.
- Cpt: Etapa 2 (Estandarización). Dln: Desde 2025. Act: Gobierno Digital identifica procedimientos comunes.
- Cpt: Etapa 3 (Mejora Continua). Act: Instituciones revisan y ajustan su nómina según estándar.
- Cpt: Transversal (Seguimiento). Act: Actualización continua del avance en digitalización en el CPAT.

### 6. Recursos de Apoyo

ID: KB-066-RECURSOS-APOYO-01

- Cpt: Recurso. Ref: Manual de usuarios/as de la Plataforma CPAT.
- Cpt: Recurso. Ref: Plantilla guía del CPAT.
- Cpt: Recurso. Ref: Consolidado de procedimientos administrativos y tramitaciones.

## Artefacto: Sobre CPAT (Ñuble)

ID: TDE-CPAT-CONSOLIDADO-01
Version: 1.0.0
Status: Draft
Human-Creator: FS
Human-Editor: FS
Model-Collaborator: IA-GEMINI
Creation-Date: 2025-10-06
Modification-Date: 2025-10-06
Source: plan-td-gore-nuble/01_entidades_de_valor/ev-000-conocimiento/staging/cpat.md
Ctx: Análisis de madurez de trámites digitales (CPAT) para GORE Ñuble y municipalidades, orientado a la Transformación Digital Estatal (TDE) y preparación para IA responsable.

---

### 0. Resumen ejecutivo

ID: TDE-CPAT-RESUMEN-01

#### 0.1. Lo esencial

ID: TDE-CPAT-RESUMEN-ESENCIAL-01

- Cpt: Dominan los objetos *Solicitud/Permiso* y *Certificado/Constancia* (especialmente en municipios).
- Cpt: Objetos secundarios dominantes son *Pago/Arancel* e *Inscripción/Registro*.
- Cpt: Existe una concentración de niveles 0–1 en las categorías dominantes.
- Res: Oportunidad de salto a Nivel 3 (formulario + expediente + notificación) con retornos rápidos.
- Cpt: Brecha existente entre la disponibilidad de una URL informativa y un canal transaccional completo.
- Cpt: Autenticación heterogénea con baja adopción de ClaveÚnica y uso extendido de mecanismos propios.
- Rec: Urge estandarizar la autenticación.
- Cpt: GORE Ñuble muestra un núcleo avanzado de Nivel 5 (≈21%), pero convive con un 50% en Nivel 0.
- Rec: Foco en cerrar la asimetría de madurez en GORE Ñuble.
- Cpt: Municipios tienen ≈3,7% de trámites en Nivel 5 y más de la mitad en Nivel 0–1.
- Cpt: Existen buenas prácticas puntuales (p. ej., Ninhue) que deben escalarse.

#### 0.2. Qué hacer ahora

ID: TDE-CPAT-RESUMEN-ACCIONES-01

- Act: Priorizar top 30–50 trámites de alto volumen/urgencia social en *Solicitud/Permiso* y *Certificado/Constancia* (Nivel 0–1).
- Obj: Llevar los trámites priorizados a Nivel 3.
- Act: Estandarizar autenticación (ClaveÚnica por defecto donde aplique).
- Act: Crear plan de eliminación/migración de mecanismos de autenticación propios.
- Act: Cerrar la brecha URL→Canal, convirtiendo páginas informativas en flujos completos con expediente y notificación.
- Act: Crear inventario de automatizaciones/IA.
- Act: Elaborar matriz de riesgos para IA/automatización.
- Act: Definir política de transparencia/explicabilidad con revisión humana.
- Act: Implementar un tablero regional con KPIs de madurez, uso y calidad del servicio. Ref: TDE-CPAT-KPIS-01.

---

### 1. Alcance, fuentes y método

ID: TDE-CPAT-METODOLOGIA-01

#### 1.1. Fuentes y Cobertura

ID: TDE-CPAT-METODOLOGIA-FUENTES-01

- Ctx: Período de análisis 2024–2025.
- Src: Catálogos CPAT (GOREs y Municipalidades).
- Src: Codebook propio de tipologías y reglas.
- Src: Extracciones y tablas de datos (asignación, distribuciones, cruces, ejemplos).
- Cpt: Cobertura GORE Ñuble.
- Cpt: Cobertura 15/21 municipalidades con registros CPAT 2024.
- Warn: 6 comunas sin datos en el corte de información.

#### 1.2. Método de clasificación

ID: TDE-CPAT-METODOLOGIA-CLASIFICACION-01

- Def: Dimensión A – Objeto. Mech: Regex y señales semánticas sobre “Nombre del registro”.
- Def: Dimensión B – Tipo CPAT. Mech: Clasificación por función común/específica.
- Def: Dimensión C – Nivel (0–5). Mech: Normalizado a “Nivel X”.
- Def: Dimensión D – Autenticación. Mech: Clasificación en ClaveÚnica/Tributaria/Propia/Sin.
- Def: Dimensión E – Canal transaccional. Mech: Clasificación Sí/No.
- Def: Dimensión F – URL de inicio. Mech: Clasificación Sí/No.
- Def: Dimensiones complementarias. Cpt: Disponibilidad y Pago asociado.

#### 1.3. Criterios y Reglas Transversales

ID: TDE-CPAT-METODOLOGIA-REGLAS-01

- Cpt: Regla de propósito dominante.
- Cpt: Regla de distinción *Certificados* vs *Solicitudes*.
- Cpt: Regla de distinción *Inscripción* vs *Permiso*.
- Cpt: Regla de agrupación *Transparencia/Relación ciudadana*.
- Cpt: Regla de agrupación *Compras*.
- Cpt: Regla de agrupación *Orientación*.
- Cpt: Proceso de manejo de ambigüedad mediante revisión manual.

---

### 2. Resultados consolidados

ID: TDE-CPAT-RESULTADOS-01

#### 2.1. GORE Ñuble

ID: TDE-CPAT-RESULTADOS-GORE-01

- Cpt: Universo de 42 registros aproximadamente.
- Cpt: 29 registros de función común.
- Cpt: 12 registros de función específica.
- Cpt: 1 registro de otra función.
- Cpt: Madurez Nivel 0: ~50%.
- Cpt: Madurez Nivel 5: ~21% (núcleo avanzado).
- Cpt: Resto de registros distribuidos en niveles 1-4.
- Cpt: ~50% de los registros tiene URL de inicio.
- Cpt: ≈29% de los registros tiene canal digital declarado.
- Ex: Ejemplos de Nivel 5 son Acceso a la Información (Ley 20.285), Audiencias (Ley 20.730), declaraciones de intereses/patrimonio, y procesos de compras.
- Res: Coexistencia de islas avanzadas con rezago estructural.
- Rec: Paquetizar mejoras para migrar a Nivel 3 los trámites de función común en Nivel 0.
- Rec: Asegurar canal transaccional donde ya existe URL informativa.

#### 2.2. Municipalidades de Ñuble

ID: TDE-CPAT-RESULTADOS-MUNIS-01

- Cpt: Universo de ≈2.642 registros (15 comunas).
- Cpt: Estado mayoritario de registros es "Completado".
- Cpt: Madurez Nivel 0–1 concentra la mayoría de los registros.
- Cpt: Madurez Nivel 5: ≈3,7%.
- Cpt: Uso de ClaveÚnica: ~9–10%.
- Cpt: Uso de mecanismo propio de autenticación: ~17%.
- Cpt: Uso de autenticación Tributaria es marginal.
- Cpt: ~54% de los registros tiene URL de inicio.
- Cpt: Existe heterogeneidad entre comunas.
- Ex: Ninhue presenta un alto % de Nivel 5 y mayor uso de ClaveÚnica.
- Ex: San Fabián, Cobquecura, Coelemu, Quillón, San Nicolás presentan alto % de Nivel 0.
- Res: Gran potencial de estandarización y aprovechamiento de buenas prácticas locales.

#### 2.3. Patrones transversales

ID: TDE-CPAT-RESULTADOS-PATRONES-01

- Cpt: Objetos *Solicitud/Permiso* y *Certificado/Constancia* concentran niveles bajos.
- Rec: Son candidatos ideales para digitalizar con formularios electrónicos, expediente y notificaciones.
- Cpt: Uso de mecanismo propio de autenticación está extendido.
- Cpt: ClaveÚnica está subutilizada.
- Cpt: Muchas URLs son informativas y no tienen un flujo transaccional completo.
- Rec: Priorizar el cierre de esta brecha (URL vs. Canal).
- Cpt: Existen oportunidades para implementar pago en línea y conciliación automatizada donde hay cobro.

---

### 3. Tipología CPAT — síntesis operativa

ID: TDE-CPAT-TIPOLOGIA-01

#### 3.1. Objeto del registro (clasificación principal)

ID: TDE-CPAT-TIPOLOGIA-OBJETO-01

1. Def: Solicitud/Permiso
2. Def: Certificado/Constancia
3. Def: Pago/Arancel
4. Def: Beneficio/Subsidio/Postulación
5. Def: Inscripción/Registro
6. Def: Reclamo/Denuncia/Transparencia
7. Def: Compras/Licitaciones
8. Def: Atención/Orientación
9. Def: Otro/No clasificado (requiere revisión manual)

#### 3.2. Otras dimensiones y reglas

ID: TDE-CPAT-TIPOLOGIA-REGLAS-01

- Cpt: Dimensión clave: Tipo CPAT.
- Cpt: Dimensión clave: Nivel (0–5).
- Cpt: Dimensión clave: Autenticación.
- Cpt: Dimensión clave: Canal.
- Cpt: Dimensión clave: URL.
- Cpt: Dimensión clave: Disponibilidad.
- Cpt: Dimensión clave: Pago asociado.
- Cpt: Regla de clasificación: propósito dominante.
- Cpt: Regla de clasificación: evidencia de canal para validar nivel.
- Cpt: Regla de clasificación: uso de ClaveÚnica por defecto cuando corresponda.
- Cpt: Regla de clasificación: higiene de enlaces.

---

### 4. Implicancias para TDE con foco en IA responsable

ID: TDE-CPAT-IMPLICANCIAS-IA-01

- Cpt: 1. Mapa de riesgo (IA/automatización).
  - Instr: Identificar alto riesgo sobre trámites Nivel ≥3 (decisiones que afectan derechos, subsidios, elegibilidad, priorización de proyectos).
  - Req: Exigir revisión humana.
  - Req: Exigir explicabilidad razonable.
  - Req: Exigir bitácoras de decisión.
  - Req: Exigir gobernanza de datos.
- Cpt: 2. Datos y calidad.
  - Req: Establecer diccionarios de datos.
  - Req: Definir reglas de negocio.
  - Req: Asegurar linaje de datos.
  - Req: Realizar pruebas de sesgo cuando exista modelamiento.
  - Req: Definir políticas de retención, auditoría y protección de datos.
- Cpt: 3. Transparencia al usuario.
  - Req: Rotulado de IA cuando aplique.
  - Req: Explicación simple de criterios.
  - Req: Disponer de un canal de apelación.
- Cpt: 4. Contratación pública.
  - Req: Incluir cláusulas de IA responsable (matriz de riesgos, métricas, documentación técnica, pruebas, auditorías, plan de contingencia).
- Cpt: 5. Ciberseguridad.
  - Req: Establecer controles mínimos.
  - Req: Gestionar incidentes para automatizaciones/IA.
  - Req: Definir proceso de reporte de incidentes.
- Cpt: 6. Personas y cambio.
  - Req: Realizar capacitación focalizada (datos, jurídico, compras TI, TI, atención ciudadana).

---

### 5. Hoja de ruta priorizada (12 meses)

ID: TDE-CPAT-ROADMAP-01

#### 5.1. 0–90 días (habilitadores + quick wins)

ID: TDE-CPAT-ROADMAP-90D-01

- Act: Realizar inventario de sistemas automatizados/IA (GORE + municipios con mayor rezago).
- Act: Elaborar matriz de riesgos (GORE + municipios con mayor rezago).
- Act: Realizar limpieza y normalización de URLs.
- Act: Crear checklist de transparencia por trámite.
- Act: Estandarizar autenticación (ClaveÚnica por defecto).
- Act: Crear planes de migración desde mecanismos de autenticación propios.
- Act: Crear plantillas de formulario, expediente y notificación para casos *Solicitud/Permiso*, *Certificado* y *Pago*.

#### 5.2. 90–180 días (aceleración)

ID: TDE-CPAT-ROADMAP-180D-01

- Act: Migrar top 30–50 trámites de alto impacto a Nivel 3 (de punta a punta).
- Act: Implementar tablero regional con KPIs. Ref: TDE-CPAT-KPIS-01.
- Act: Realizar pilotos de explicabilidad y revisión humana en decisiones automatizadas.

#### 5.3. 180–365 días (consolidación)

ID: TDE-CPAT-ROADMAP-365D-01

- Act: Escalar a Nivel 4–5 un grupo de 10–15 trámites estratégicos.
- Ctx: Foco en interoperabilidad (validaciones automáticas, pagos, notificaciones, conciliación).
- Act: Realizar auditorías internas de IA.
- Act: Realizar pruebas de sesgo donde corresponda.
- Act: Operar de forma continua la gestión de incidentes (automatización/IA).
- Act: Asegurar resguardo legal de la operación de automatización/IA.

---

### 6. KPIs y tablero regional

ID: TDE-CPAT-KPIS-01

#### 6.1. Cobertura y madurez

ID: TDE-CPAT-KPIS-MADUREZ-01

- Cpt: % de trámites con URL válida (vigente).
- Cpt: % con canal transaccional.
- Cpt: % con ClaveÚnica.
- Cpt: Distribución por Nivel 0–5 y variación trimestral.

#### 6.2. Uso y calidad

ID: TDE-CPAT-KPIS-USO-01

- Cpt: Tiempo de ciclo (p50/p90) por objeto.
- Cpt: Tasa de reingreso / retrabajo.
- Cpt: Tasa de reclamos y SLA de respuesta.
- Cpt: Satisfacción NPS/CSAT.

#### 6.3. IA responsable

ID: TDE-CPAT-KPIS-IA-01

- Cpt: % trámites con rotulado (si aplica).
- Cpt: % con revisión humana documentada.
- Cpt: Incidentes reportados/gestionados.
- Cpt: Auditorías realizadas y hallazgos cerrados.

#### 6.4. Fórmula de priorización sugerida

ID: TDE-CPAT-KPIS-FORMULA-01

- Mdl: $\text{Score} = 0{,}35\times\text{Impacto} + 0{,}30\times\text{Factibilidad} + 0{,}20\times\text{Riesgo} + 0{,}15\times\text{Urgencia estacional}$
- Def: Impacto. Cpt: volumen, criticidad social, ingresos/costos evitados.
- Def: Factibilidad. Cpt: disponibilidad de datos, procesos, equipo.
- Def: Riesgo. Cpt: cumplimiento/tecnológico reputacional (priorizar reducción de riesgo).
- Def: Urgencia. Cpt: ventanas/picos (p. ej., permisos estacionales).

---

### 7. Recomendaciones tácticas por actor

ID: TDE-CPAT-RECOMENDACIONES-01

#### 7.1. GORE Ñuble

ID: TDE-CPAT-RECOMENDACIONES-GORE-01

- Rec: Subir a Nivel 3 los trámites de función común en Nivel 0.
- Rec: Asegurar canal transaccional donde ya existe URL informativa.
- Rec: Estandarizar ClaveÚnica y expediente/seguimiento.
- Rec: Publicar un repositorio único de URLs de inicio con control de versiones.

#### 7.2. Municipios con alto rezago

ID: TDE-CPAT-RECOMENDACIONES-REZAGO-01
Ctx: Ejemplos de municipios: San Fabián, Cobquecura, Coelemu, Quillón, San Nicolás.

- Rec: Implementar programa intensivo de paquete mínimo (formulario estándar + ClaveÚnica + expediente).
- Rec: Proveer apoyo técnico para cerrar la brecha URL→Canal.

#### 7.3. Municipios con buen desempeño

ID: TDE-CPAT-RECOMENDACIONES-AVANZADOS-01
Ctx: Ejemplos de municipios: Ninhue, Ñiquén.

- Rec: Fomentar mentoría cruzada.
- Rec: Promover la reutilización de plantillas.
- Rec: Crear un catálogo de buenas prácticas para escalar soluciones.

---

### 8. Arquitectura de solución (estado objetivo)

ID: TDE-CPAT-ARQUITECTURA-01

#### 8.1. Capa de experiencia

ID: TDE-CPAT-ARQUITECTURA-EXP-01

- Cpt: Formularios web accesibles, multicanal.
- Cpt: Validaciones in situ y autocompletado en formularios.
- Cpt: Sistema de notificación y seguimiento (folio/expediente).

#### 8.2. Capa de identidad y firma

ID: TDE-CPAT-ARQUITECTURA-ID-01

- Cpt: ClaveÚnica como estándar de autenticación.
- Cpt: Firma electrónica simple/avanzada según caso de uso.

#### 8.3. Capa de procesos (BPM/Case)

ID: TDE-CPAT-ARQUITECTURA-PROC-01

- Cpt: Motor de flujos, reglas y SLAs.
- Cpt: Bitácora y trazabilidad de procesos.
- Cpt: Integraciones a pagos, correo/notificación y repositorios documentales.

#### 8.4. Capa de datos

ID: TDE-CPAT-ARQUITECTURA-DATA-01

- Cpt: Catálogo de datos y diccionarios.
- Cpt: Control de calidad y linaje de datos.
- Cpt: Tablero de KPIs y evidencia para auditorías.

#### 8.5. Capa de interoperabilidad

ID: TDE-CPAT-ARQUITECTURA-INTEROP-01

- Cpt: Servicios de consulta/validación con terceros públicos.
- Cpt: Conciliación de pagos.
- Cpt: Servicios de reportabilidad.

#### 8.6. Capa de IA (opcional/según riesgo)

ID: TDE-CPAT-ARQUITECTURA-IA-01

- Cpt: Asistentes para orientación y clasificación (bajo riesgo).
- Cpt: Apoyo a decisión con revisión humana y explicabilidad (alto riesgo).
- Cpt: Controles de IA (rotulado, pruebas, auditorías, gestión de sesgo e incidentes).

---

### 9. Playbook de implementación (patrones reutilizables)

ID: TDE-CPAT-PLAYBOOK-01

- Cpt: 1. Certificados/Constancias (L0–1→L3)
  - Proc: Formulario + validación automática de requisitos + generación de PDF con folio + notificación.
  - Cond: Si hay cobro, integrar pago en línea y conciliación.
- Cpt: 2. Solicitudes/Permisos
  - Proc: Formulario estructurado + expediente + revisión con checklist + resolución digital.
  - Proc: Integraciones a catastro/registro si aplica.
- Cpt: 3. Pagos/Aranceles
  - Proc: Portal de pagos + cálculo automático + conciliación + comprobante.
- Cpt: 4. Inscripciones/Registros
  - Proc: Alta/actualización con validaciones + API de consulta/constancia.
- Cpt: 5. Reclamos/Transparencia
  - Proc: Flujo con SLAs, hitos y comunicación; trazabilidad completa y métricas públicas.

---

### 10. Gestión del cambio y gobernanza

ID: TDE-CPAT-GOBERNANZA-01

#### 10.1. Modelo de gobernanza

ID: TDE-CPAT-GOBERNANZA-MODELO-01

- Cpt: Comité TDE (estratégico).
  - Resp: Prioriza cartera y aprueba estándares.
- Cpt: Oficina de Producto Digital (operativo).
  - Resp: Fabrica y opera los flujos comunes.
- Cpt: Data Governance.
  - Resp: Define políticas, diccionarios, calidad y acceso a datos.
- Cpt: Oficial de IA Responsable.
  - Resp: Mantiene inventario, riesgos, auditorías y reportes de IA.

#### 10.2. RACI resumido

ID: TDE-CPAT-GOBERNANZA-RACI-01

- Resp: R (responsable): Oficina de Producto / equipos municipales.
- Resp: A (aprobador): Comité TDE.
- Resp: C (consultado): Jurídico, Compras, Ciberseguridad, Datos.
- Resp: I (informado): Direcciones/Unidades dueñas del trámite.

---

### 11. Riesgos y mitigaciones

ID: TDE-CPAT-RIESGOS-01

- Cpt: R1: Subdeclaración/obsolescencia de niveles o URLs.
  - Rec: Validación periódica, pruebas de extremo a extremo, monitoreo de enlaces.
- Cpt: R2: Sobreuso de mecanismos propios de autenticación.
  - Rec: Plan de migración a ClaveÚnica y desactivación progresiva.
- Cpt: R3: Dependencias externas (pagos/interoperabilidad).
  - Rec: Acuerdos y SLAs, colas de degradación.
- Cpt: R4: Automatizaciones de alto riesgo sin salvaguardas.
  - Rec: Revisión humana, explicabilidad, auditorías, gestión de incidentes.
- Cpt: R5: Variabilidad municipal de capacidades.
  - Rec: Plantillas reutilizables, mentoring y acompañamiento regional.

---

### 12. Próximos pasos accionables (checklist)

ID: TDE-CPAT-NEXT-STEPS-01

- [ ] Act: Validar dataset 2024 vs. 2025 y completar 6 comunas faltantes.
- [ ] Act: Publicar catálogo único de URLs con control de versiones.
- [ ] Act: Acordar lista priorizada (30–50) de trámites L0–1 → L3.
- [ ] Act: Aprobar estándares (ClaveÚnica, expediente, notificación, métricas).
- [ ] Act: Levantar inventario IA/automatizaciones y clasificar riesgos.
- [ ] Act: Montar tablero KPIs y rutina trimestral de seguimiento.

---

### Apéndice A — Codebook resumido (uso práctico)

ID: TDE-CPAT-APENDICE-A-01

#### A.1 Definiciones y señales (Objeto)

ID: TDE-CPAT-APENDICE-A1-01

- Def: Solicitud/Permiso. Cpt: “solicitud”, “permiso”, “autorización”, “licencia”, “prórroga”.
- Def: Certificado/Constancia. Cpt: “certificado”, “constancia”, “acreditación”, “fe de”.
- Def: Pago/Arancel. Cpt: “pago”, “arancel”, “derecho”, “cancelación”.
- Def: Beneficio/Subsidio/Postulación. Cpt: “postulación”, “subsidio”, “beneficio”, “bono”, “beca”, “aporte”.
- Def: Inscripción/Registro. Cpt: “inscripción”, “registro”, “empadronamiento”, “matrícula”, “actualización”.
- Def: Reclamo/Denuncia/Transparencia. Cpt: “reclamo”, “denuncia”, “OIRS/SIAC”, “transparencia”, “acceso a la información”, “audiencia”, “lobby”.
- Def: Compras/Licitaciones. Cpt: “licitación”, “contratación”, “convenio marco”, “proveedor”, “Mercado Público”.
- Def: Atención/Orientación. Cpt: “orientación”, “información”, “asesoría”, “guía”.

#### A.2 Reglas transversales

ID: TDE-CPAT-APENDICE-A2-01

- Cpt: Propósito dominante.
- Cpt: Certificados vs. solicitudes.
- Cpt: Inscripción vs. permiso.
- Cpt: Transparencia/relación ciudadana.
- Cpt: Compras.
- Cpt: Orientación.
- Cpt: Ambigüedad (revisión manual).

#### A.3 Normalización de nivel

ID: TDE-CPAT-APENDICE-A3-01

- Def: Nivel 0. Cpt: sólo presencial.
- Def: Nivel 1. Cpt: información en línea sin transacción.
- Def: Nivel 2. Cpt: descarga/envío no estandarizado.
- Def: Nivel 3. Cpt: flujo en línea de punta a punta.
- Def: Nivel 4. Cpt: interoperabilidad/pagos/validaciones.
- Def: Nivel 5. Cpt: automatización avanzada + expediente trazable.

---

### Apéndice B — Plantillas reutilizables

ID: TDE-CPAT-APENDICE-B-01

#### B.1 Ficha de Trámite Digital (mínimos)

ID: TDE-CPAT-APENDICE-B1-01

- Cpt: Nombre y Objeto
- Cpt: Tipo CPAT
- Cpt: Nivel objetivo (próximo trimestre)
- Cpt: Autenticación (estándar)
- Cpt: URL de inicio
- Cpt: Canal transaccional
- Cpt: Pago asociado (sí/no)
- Cpt: Interoperabilidades
- Cpt: SLAs y métricas
- Cpt: Riesgo (IA/automatización) y salvaguardas
- Cpt: Propietario y equipo responsable

#### B.2 Checklist de IA responsable (por trámite con automatización)

ID: TDE-CPAT-APENDICE-B2-01

- [ ] Cpt: ¿Se clasificó el riesgo y se documentó?
- [ ] Cpt: ¿Hay revisión humana significativa cuando impacta derechos?
- [ ] Cpt: ¿Se mantiene bitácora y linaje de datos?
- [ ] Cpt: ¿Existe explicación simple al usuario?
- [ ] Cpt: ¿Se rotula el uso de IA (si aplica)?
- [ ] Cpt: ¿Se ejecutaron pruebas de desempeño y sesgo?
- [ ] Cpt: ¿Hay plan de incidentes y continuidad?
- [ ] Cpt: ¿Se incluyen cláusulas contractuales de IA responsable?

#### B.3 Cláusulas mínimas en contratación

ID: TDE-CPAT-APENDICE-B3-01

- Cpt: Entrega de documentación técnica y matriz de riesgos.
- Cpt: Métricas medibles de desempeño y sesgo.
- Cpt: Derecho de auditoría y pruebas; gestión de incidentes.
- Cpt: Propiedad y acceso a bitácoras/datos para fiscalización.
- Cpt: Cumplimiento normativo (datos, ciberseguridad, transparencia).

---

### Apéndice C — Árbol de decisión de clasificación (texto)

ID: TDE-CPAT-APENDICE-C-01

1. Cpt: ¿El resultado es un documento acreditativo? → **Certificado/Constancia**.
2. Cpt: ¿Crea/modifica un asiento en un padrón? → **Inscripción/Registro**.
3. Cpt: ¿El acto central es pagar? → **Pago/Arancel**.
4. Cpt: ¿Es solicitar una autorización/licencia? → **Solicitud/Permiso**.
5. Cpt: ¿Es postular a un beneficio/subsidio/beca? → **Beneficio/Subsidio/Postulación**.
6. Cpt: ¿Es reclamar/denunciar/pedir información pública? → **Reclamo/Denuncia/Transparencia**.
7. Cpt: ¿Es contratar/comprar (sector público)? → **Compras/Licitaciones**.
8. Cpt: ¿Sólo orienta/informa sin acto administrativo? → **Atención/Orientación**.
9. Cpt: Si no encaja → **Otro/No clasificado** (revisar manualmente).
