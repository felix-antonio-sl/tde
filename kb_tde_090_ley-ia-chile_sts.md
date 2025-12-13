# Master Guide: Análisis de la Legislación en Trámite sobre IA en Chile

ID: KB-TDE-IA-LAW-ANALYSIS-01
Version: 1.0.0
Status: Draft
Human-Creator: FS
Model-Collaborator: Kronos
Creation-Date: 2025-10-02
Modification-Date: 2025-10-02
Ref-STS-Guide: GUIDE-STS-MASTER-01

---
**BEGIN_LLM_INSTRUCTIONS**
You are an AI agent consuming a Structured Telegraphic Style (STS) artifact. Your primary task is to parse and reason over THIS document with absolute fidelity, using only the rules defined below. This artifact is a self-contained source of truth.

1. **Core Objective**: Maintain perfect fidelity to the information (`meat`) and structure (`skeleton`). Do not summarize, interpret, or infer information not explicitly present.
2. **Lexicon Mode & Expansion**: This document uses an **Abbreviated Lexicon**. You MUST treat the keywords as valid and expand them according to the official STS mapping.
3. **Reference (`Ref:`) Policy**: `Ref:` is for internal cross-references to an `ID:` within THIS document ONLY.
4. **Language Invariance Policy**: Preserve the original language of all `EssentialData`.
**END_LLM_INSTRUCTIONS**

---

## 1. Antecedentes Políticos y Técnicos

ID: KB-TDE-IA-LAW-BACKGROUND-01
Fnd: Fusión de dos iniciativas legislativas.

- Cpt: Iniciativa-1. Def: Mensaje presidencial (boletín Nº 16.821-19). Dln: 7 de mayo de 2024.
- Cpt: Iniciativa-2. Def: Moción parlamentaria (boletín Nº 15.869-19). Dln: 24 de abril de 2023.
Cpt: Contexto-Mocion.
- Purp: Regular sistemas de IA, robótica y tecnologías conexas.
- Ctx: Impulsada por la Comisión de Futuro, Ciencia, Tecnología e Innovación.
Cpt: Contexto-Mensaje.
- Cpt: Urgencia. Def: Suma.
- Cpt: Justificacion. Def: Abordar el potencial de bienestar y competitividad de la IA frente a sus riesgos y desafíos éticos.
- Cpt: Referentes-Internacionales.
  - - Ctx: Recomendación UNESCO 2021 sobre ética de la IA.
  - - Ctx: Ley de IA de la Unión Europea (enfoque de riesgo).
  - - Ctx: Aproximación de Estados Unidos (autorregulación y compromisos voluntarios).
  - - Ctx: Regulación en China (algoritmos y contenido sintético).
Cpt: Sintesis.
- Ctx: Político. Purp: Impulsar la IA de forma responsable, alineada con estándares internacionales y la estrategia de transformación digital del país.
- Ctx: Técnico. Purp: Incorporar principios éticos y lecciones comparadas para garantizar certezas regulatorias que respeten los derechos fundamentales.
Cpt: Proceso-Judicial.
- Act: El proyecto fue remitido a la Excma. Corte Suprema para informe sobre su incidencia en materias judiciales.
- Dln: Consulta realizada el 8 de mayo de 2024; respuesta recibida el 21 de junio de 2024.
Cpt: Apoyo-Politico.
- Res: El proyecto fue aprobado por unanimidad en general en la Comisión especializada.

## 2. Estructura y Contenido del Proyecto de Ley de IA

ID: KB-TDE-IA-LAW-STRUCTURE-01
Cpt: Estructura. Def: 31 artículos permanentes y 3 transitorios.
Cpt: Titulos-Tematicos.

- - Disposiciones Generales (objeto, ámbito, definiciones, clasificación de riesgos).
- - Sistemas de Riesgo Inaceptable.
- - Sistemas de IA de Alto Riesgo.
- - Sistemas de IA de Riesgo Limitado.
- - Incidentes Graves.
- - Gobernanza de IA.
- - Medidas de Apoyo a la Innovación.
- - Confidencialidad, Infracciones y Sanciones.
- - Disposiciones Finales y Transitorias.

### 2.1. Objeto y Ámbito de Aplicación (Art. 1-2)

ID: KB-TDE-IA-LAW-STRUCTURE-SCOPE-01

- Obj: Promover la creación, desarrollo, innovación e implementación de sistemas de IA al servicio del ser humano, de manera coherente con los principios democráticos y los derechos fundamentales.
- Cpt: Ambito-Aplicacion.
  - Dest: Todos los actores de la cadena de valor (desarrolladores, proveedores, implementadores, importadores, distribuidores) cuando las salidas del sistema se usen en territorio nacional.
- Cpt: Exclusiones.
  - - Cpt: Defensa-Nacional. Def: Sistemas de IA desarrollados y usados con fines de defensa nacional.
  - - Cpt: Investigacion-Desarrollo. Def: Actividades previas a la comercialización que respeten derechos fundamentales y no involucren pruebas en condiciones reales.
  - - Cpt: Codigo-Abierto. Def: Componentes de IA de licencia libre, salvo que se comercialicen como parte de un sistema de IA de alto riesgo.
  - - Cpt: Uso-Privado. Def: Uso personal y no comercial de un sistema de IA.

### 2.2. Definiciones Clave (Art. 3)

ID: KB-TDE-IA-LAW-STRUCTURE-DEFS-01

- Cpt: Sistema-de-IA. Def: Sistema basado en máquinas que infiere salidas (predicciones, contenidos, etc.) capaces de influir en entornos físicos o virtuales.
- Cpt: Riesgo-Significativo. Def: Combinación de la probabilidad y gravedad del daño que puede afectar a las personas.
- Cpt: Operadores-de-IA. Def: Agrupa a proveedores, implementadores, importadores, distribuidores y representantes autorizados.
- Cpt: Sistema-de-IA-de-Uso-General. Def: IA de propósito general con múltiples aplicaciones.

### 2.3. Principios Rectores (Art. 4)

ID: KB-TDE-IA-LAW-STRUCTURE-PRINCIPLES-01
Purp: Consagrar principios éticos y operativos que deben observar los operadores de IA.
Cpt: Lista-Principios.

- - Intervención y supervisión humana.
- - Solidez y seguridad técnica.
- - Privacidad y gobernanza de datos.
- - Transparencia y explicabilidad.
- - Diversidad, no discriminación y equidad.
- - Bienestar social y medioambiental.
- - Rendición de cuentas y responsabilidad.
- - Protección de los derechos de los consumidores.
Resp: La observancia de estos principios será orientada, regulada y fiscalizada por el Ministerio de CTCI, la Agencia de Protección de Datos Personales (APDP) y la Agencia Nacional de Ciberseguridad (ANCI). Ref: KB-TDE-IA-LAW-INSTITUTIONAL-ROLES-01.

### 2.4. Clasificación por Nivel de Riesgo (Art. 5)

ID: KB-TDE-IA-LAW-STRUCTURE-RISK-LEVELS-01
Fnd: Enfoque regulatorio basado en el riesgo, similar al modelo europeo.
Cpt: Categorias-Riesgo.

- - Cpt: Riesgo-Inaceptable. Def: Sistemas incompatibles con el respeto a los derechos fundamentales. Prohibidos absolutamente. Ref: KB-TDE-IA-LAW-STRUCTURE-UNACCEPTABLE-RISK-01.
- - Cpt: Alto-Riesgo. Def: Sistemas cuyo uso presenta un riesgo significativo de perjuicio. No se prohíben, pero su uso está condicionado a requisitos obligatorios. La lista específica será definida por reglamento. Ref: KB-TDE-IA-LAW-STRUCTURE-HIGH-RISK-01.
- - Cpt: Riesgo-Limitado. Def: Sistemas con riesgos no significativos de manipulación o engaño. Se les imponen reglas básicas de transparencia. Ref: KB-TDE-IA-LAW-STRUCTURE-LIMITED-RISK-01.
- - Cpt: Sin-Riesgo-Evidente. Def: Sistemas que no presentan riesgos significativos. No se les imponen requisitos adicionales.

### 2.5. Usos de Riesgo Inaceptable (Art. 6)

ID: KB-TDE-IA-LAW-STRUCTURE-UNACCEPTABLE-RISK-01
Purp: Enumerar taxativamente las prácticas de IA prohibidas.
Fnd: Corresponde a la categoría de Riesgo Inaceptable. Ref: KB-TDE-IA-LAW-STRUCTURE-RISK-LEVELS-01.
Cpt: Practicas-Prohibidas.

- - a) Manipulación subliminal que cause daño físico o mental (con excepción terapéutica consentida).
- - b) Explotación de vulnerabilidades para inducir comportamientos dañinos (con especial protección a NNA).
- - c) Categorización masiva basada en datos sensibles que provoque discriminación (con excepción terapéutica consentida).
- - d) Calificación social generalizada ("social scoring") que resulte en trato discriminatorio.
- - e) Identificación biométrica remota en tiempo real en espacios públicos (con excepción para seguridad pública y persecución penal).
- - f) Extracción masiva e indiscriminada de imágenes faciales ("facial scraping").
- - g) Evaluación de emociones en ámbitos sensibles (penal, laboral, educativo, etc.).

### 2.6. Obligaciones para Alto Riesgo (Art. 7-10)

ID: KB-TDE-IA-LAW-STRUCTURE-HIGH-RISK-01
Purp: Detallar los requisitos obligatorios para sistemas de IA de alto riesgo.
Fnd: Corresponde a la categoría de Alto Riesgo. Ref: KB-TDE-IA-LAW-STRUCTURE-RISK-LEVELS-01.
Req: Obligaciones.

- - Gestión de Riesgos: Implementar un sistema de gestión de riesgos continuo durante todo el ciclo de vida.
- - Gobernanza de Datos: Asegurar una adecuada gobernanza de datos, incorporando estándares de seguridad y protección.
- - Documentación Técnica: Contar con documentación inteligible que demuestre el cumplimiento de la ley.
- - Registros (Logs): Implementar funcionalidades para registrar eventos y almacenarlos de forma segura.
- - Transparencia y Explicabilidad: Diseñar sistemas con un nivel suficiente de transparencia para que su funcionamiento sea comprensible.
- - Supervisión Humana: Contar con mecanismos técnicos y operativos para la supervisión por parte de personal capacitado.
- - Precisión, Solidez y Ciberseguridad: Desarrollar sistemas bajo el principio de seguridad desde el diseño, alineados con la Ley Marco de Ciberseguridad.
Cpt: Flexibilidad-Proporcional.
- Def: El reglamento podrá establecer estándares diferenciados para pymes.

### 2.7. Obligaciones para Riesgo Limitado (Art. 11)

ID: KB-TDE-IA-LAW-STRUCTURE-LIMITED-RISK-01
Fnd: Corresponde a la categoría de Riesgo Limitado. Ref: KB-TDE-IA-LAW-STRUCTURE-RISK-LEVELS-01.

- Req: Deber-de-Transparencia. Def: Informar a las personas que están interactuando con un sistema de IA.
- Cpt: Excepcion. Def: No aplica para sistemas autorizados por ley para fines de investigación o enjuiciamiento penal.

### 2.8. Gestión de Incidentes Graves (Art. 13)

ID: KB-TDE-IA-LAW-STRUCTURE-INCIDENTS-01

- Mech: Cualquier persona puede reportar un incidente grave a la Agencia de Protección de Datos Personales (APDP).
- Proc: La APDP informará al operador responsable para que adopte medidas de contención.
- Cpt: Coordinacion. Def: Si el incidente afecta a operadores vitales, la APDP deberá coordinarse con la Agencia Nacional de Ciberseguridad (ANCI).
- Ctx: Roles institucionales de APDP y ANCI. Ref: KB-TDE-IA-LAW-INSTITUTIONAL-ROLES-01.

### 2.9. Gobernanza Institucional (Arts. 14-18)

ID: KB-TDE-IA-LAW-STRUCTURE-GOVERNANCE-01
Purp: Definir la estructura institucional para la supervisión y asesoría de la ley.
Cpt: Pilares-Gobernanza.

- - Cpt: Pilar-1. Def: Consejo Asesor Técnico de IA. Nat: Organismo permanente y consultivo. Func: Asesorar al Ministerio de CTCI en la implementación de la ley.
- - Cpt: Pilar-2. Def: Autoridad de Fiscalización (APDP). Func: Supervisar el cumplimiento, determinar infracciones y ejercer la potestad sancionadora.
Cpt: Actores-Clave.
- - Ministerio de Ciencia, Tecnología, Conocimiento e Innovación (MCTCI): Cartera líder del proyecto.
- - Cámara de Diputadas y Diputados: Corporación de origen, con un rol central de la Comisión de Futuro.
- - Excma. Corte Suprema: Consultada sobre aspectos que inciden en competencias judiciales.
- - Consejo Asesor Técnico de IA: Órgano consultivo a ser creado por la ley. Ref: KB-TDE-IA-LAW-STRUCTURE-GOVERNANCE-01.
- - Agencia de Protección de Datos Personales (APDP): Futura autoridad de fiscalización y sanción. Ref: KB-TDE-IA-LAW-STRUCTURE-GOVERNANCE-01, KB-TDE-IA-LAW-STRUCTURE-INCIDENTS-01.
- - Consejo para la Transparencia: Rol ratificado para garantizar el acceso a la información pública sobre IA.
- - Agencia Nacional de Ciberseguridad (ANCI): Papel complementario en la gestión de incidentes de seguridad. Ref: KB-TDE-IA-LAW-STRUCTURE-INCIDENTS-01.
- - Otros Actores: Ministerios sectoriales, academia, sociedad civil y empresa privada.

### 2.10. Medidas de Apoyo a la Innovación (Arts. 20-22)

ID: KB-TDE-IA-LAW-STRUCTURE-INNOVATION-01

- Cpt: Sandboxes-Regulatorios. Def: Se faculta la creación de "espacios controlados de prueba" para experimentar con innovaciones de IA en entornos restringidos y supervisados.
- Cpt: Apoyo-Pymes. Def: Se incluyen medidas de apoyo técnico y financiero para la adopción de IA en empresas de menor tamaño.

### 2.11. Régimen Sancionatorio y Responsabilidad (Arts. 23-29)

ID: KB-TDE-IA-LAW-STRUCTURE-SANCTIONS-01

- Cpt: Confidencialidad. Req: Resguardar la información obtenida por las autoridades durante la fiscalización.
- Cpt: Infracciones-Sanciones. Def: Se establece un catálogo de infracciones (leves, graves, muy graves) y multas administrativas (hasta 20.000 UTM para infracciones muy graves).
- Cpt: Responsabilidad-Civil. Def: Se regulan las acciones civiles por daños causados por sistemas de IA.
- Resp: La potestad sancionadora recae en la APDP. Ref: KB-TDE-IA-LAW-STRUCTURE-GOVERNANCE-01.

### 2.12. Disposiciones Finales y Transitorias

ID: KB-TDE-IA-LAW-STRUCTURE-FINAL-PROVISIONS-01

- Cpt: Modificacion-Propiedad-Intelectual. Act: Se introduce una excepción al derecho de autor para permitir la minería de datos (text and data mining) para el desarrollo de IA.
- Cpt: Vacatio-Legis. Def: Las normas transitorias establecen la entrada en vigencia de la ley y los plazos para dictar los reglamentos correspondientes.

## 3. Análisis de Indicaciones al Proyecto

ID: KB-TDE-IA-LAW-AMENDMENTS-01
Cpt: Hitos-Indicaciones.

- - Dln: 18 de octubre de 2024. Purp: Aclarar tratamiento de "sistemas de IA de uso general" y naturaleza voluntaria de los sandboxes.
- - Dln: 4 de marzo de 2025. Purp: Reforzar principios, redefinir usos de riesgo inaceptable, clarificar obligaciones para alto riesgo y mejorar coordinación interinstitucional (APDP-ANCI).
- - Dln: 19 de agosto de 2025. Purp: Realizar ajustes finales, ratificar competencias del Consejo para la Transparencia, ampliar funciones del Consejo Asesor de IA y facilitar acceso a datos en sandboxes.
Cpt: Indicacion-Parlamentaria.
- Dln: 4 de agosto de 2025.
- Act: Presentada por Diputada Mónica Arce.
- Purp: Agregar vulneración a la Ley Nº21.430 (Garantías de la Niñez y Adolescencia) como definición de "incidente grave".

## 4. Puntos Controversiales y Evaluación Crítica

ID: KB-TDE-IA-LAW-CRITICAL-ANALYSIS-01

- Cpt: Ambito-Aplicacion. Ctx: Exclusión de sistemas de defensa nacional y el potencial vacío legal en actividades de I+D. Ref: KB-TDE-IA-LAW-STRUCTURE-SCOPE-01.
- Cpt: Excepciones-Riesgo-Inaceptable. Ctx: Permiso para uso de identificación biométrica remota por parte de la policía. Ref: KB-TDE-IA-LAW-STRUCTURE-UNACCEPTABLE-RISK-01.
- Cpt: Delegacion-Reglamentaria. Ctx: Inquietud por delegar la lista de IA de alto riesgo a un reglamento del Ejecutivo. Ref: KB-TDE-IA-LAW-STRUCTURE-HIGH-RISK-01.
- Cpt: Enfoque-en-Usos. Ctx: La responsabilidad recae principalmente en los implementadores, lo que puede ser complejo para los desarrolladores originales.
- Cpt: IA-de-Uso-General. Ctx: Dificultad de hacer cumplir las obligaciones a los desarrolladores de modelos fundacionales, a menudo extranjeros.
- Cpt: Regimen-Sancionatorio. Ctx: Necesidad de garantizar la proporcionalidad de las multas, especialmente para las pymes. Ref: KB-TDE-IA-LAW-STRUCTURE-SANCTIONS-01.
- Cpt: Capacidad-Institucional. Ctx: Duda sobre si la APDP tendrá los recursos técnicos y financieros para fiscalizar eficazmente la ley. Ref: KB-TDE-IA-LAW-STRUCTURE-GOVERNANCE-01.
- Cpt: Propiedad-Intelectual. Ctx: Tensión entre la necesidad de acceso a datos para la innovación y la protección de los derechos de autor. Ref: KB-TDE-IA-LAW-STRUCTURE-FINAL-PROVISIONS-01.

## 5. Participación Institucional en la Gobernanza

ID: KB-TDE-IA-LAW-INSTITUTIONAL-ROLES-01
Cpt: Actores-Clave.

- - Ministerio de Ciencia, Tecnología, Conocimiento e Innovación (MCTCI): Cartera líder del proyecto.
- - Cámara de Diputadas y Diputados: Corporación de origen, con un rol central de la Comisión de Futuro.
- - Excma. Corte Suprema: Consultada sobre aspectos que inciden en competencias judiciales.
- - Consejo Asesor Técnico de IA: Órgano consultivo a ser creado por la ley. Ref: KB-TDE-IA-LAW-STRUCTURE-GOVERNANCE-01.
- - Agencia de Protección de Datos Personales (APDP): Futura autoridad de fiscalización y sanción. Ref: KB-TDE-IA-LAW-STRUCTURE-GOVERNANCE-01, KB-TDE-IA-LAW-STRUCTURE-INCIDENTS-01.
- - Consejo para la Transparencia: Rol ratificado para garantizar el acceso a la información pública sobre IA.
- - Agencia Nacional de Ciberseguridad (ANCI): Papel complementario en la gestión de incidentes de seguridad. Ref: KB-TDE-IA-LAW-STRUCTURE-INCIDENTS-01.
- - Otros Actores: Ministerios sectoriales, academia, sociedad civil y empresa privada.

## 6. Cronología Legislativa

ID: KB-TDE-IA-LAW-TIMELINE-01

- Dln: 24 de abril de 2023. Act: Presentación de moción parlamentaria (Boletín 15.869-19).
- Dln: 7 de mayo de 2024. Act: Ingreso de Mensaje presidencial (Boletín 16.821-19).
- Dln: 21 de junio de 2024. Act: Recepción de informe de la Corte Suprema.
- Dln: 3 de julio de 2024 (aprox.). Act: Aprobación en general en la Comisión de Futuro.
- Dln: 18 de octubre de 2024. Act: Ingreso de la primera ronda de indicaciones del Ejecutivo.
- Dln: 4 de marzo de 2025. Act: Ingreso de la segunda ronda de indicaciones del Ejecutivo.
- Dln: 4 de agosto de 2025. Act: Aprobación en general en la Sala de la Cámara de Diputados.
- Dln: 19 de agosto de 2025. Act: Ingreso de la tercera ronda de indicaciones del Ejecutivo.
- Cpt: Proximos-Pasos. Act: Votación en particular en la Cámara y posterior trámite en el Senado.
