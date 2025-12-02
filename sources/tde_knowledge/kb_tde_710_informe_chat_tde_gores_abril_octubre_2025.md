# Síntesis y Análisis Técnico del Chat de CTDs de GOREs

> **Período Analizado**: 23 de Abril de 2025 a 6 de Octubre de 2025
> **Autor del Análisis**: Félix Sanhueza, GORE Ñuble

## 1. Introducción

### 1.1. Propósito y Audiencia

Este informe presenta un análisis técnico de las conversaciones mantenidas por los Encargados de Transformación Digital (CTD) de los Gobiernos Regionales (GOREs) de Chile. Su propósito es servir como un insumo práctico y de alto valor para los propios miembros de la red, al detallar los desafíos operativos, las soluciones tecnológicas y las dinámicas de colaboración que definen el proceso de transformación digital en los territorios.

### 1.2. Metodología

Se realizó un análisis de contenido del registro de chat, extrayendo y categorizando información técnica específica, incluyendo nombres de software, proveedores, versiones, configuraciones de infraestructura, problemas de implementación, costos, estrategias presupuestarias y discusiones sobre ciberseguridad. Los hallazgos se han estructurado en cuatro ejes temáticos para facilitar su comprensión y aplicación.

## 2. Resumen

El principal motor de la agenda de los CTDs es el cumplimiento de los hitos del **PMG de Transformación Digital**, un proceso que consume gran parte de sus esfuerzos. Este cumplimiento se ve obstaculizado por una brecha estructural entre las metas exigidas y los recursos disponibles, particularmente en **presupuesto para renovación de infraestructura y contratación de personal especializado**.

Desde una perspectiva tecnológica, la mayor frustración radica en la **dependencia de servicios centralizados que presentan intermitencias (FirmaGob) y la ausencia de soluciones transversales clave**, notablemente un **Sistema de Gestión Documental (DMS)**, lo que ha provocado una atomización en la contratación de soluciones de mercado (`Zecovery`, `Febos`, `Ingsoft`, etc.).

El **incidente de ransomware en el GORE Araucanía** marcó un punto de inflexión, elevando la ciberseguridad a una prioridad máxima y exponiendo la insuficiencia de las medidas de protección tradicionales (antivirus `ESET`). La discusión reveló una necesidad urgente de adoptar estrategias de seguridad más robustas y de clarificar el rol de los GOREs bajo la nueva Ley Marco de Ciberseguridad.

En este contexto, la **red informal de colaboración de los CTDs** se consolida como el activo más valioso. Funciona como una mesa de ayuda de facto, una base de conocimiento distribuida y un mecanismo de coordinación ágil que resulta indispensable para sortear los desafíos diarios y avanzar en la implementación de la Transformación Digital.

## 3. Eje 1: Gobernanza, Estrategia y Cumplimiento Normativo

### 3.1. Desafíos en la Implementación de Instrumentos de Diagnóstico

El cumplimiento de la Fase de Diagnóstico del PMG domina gran parte de la conversación, con discusiones técnicas sobre cómo abordar cada instrumento.

- **CPAT (Catálogo de Procedimientos Administrativos)**: Las dudas son recurrentes. La discusión del 28/05/25 aclara que al crear un nuevo PA, este no recibe codificación ni permite reportar transacciones hasta el siguiente ciclo de actualización, lo que obliga a mantener registros paralelos. La dependencia del informe de una consultora externa para poder recategorizar y limpiar el catálogo es un punto de bloqueo mencionado en varias ocasiones.
- **Pauta de Calidad Web**: Se percibe como un instrumento extenso y complejo. Un CTD señala el 24/06/25: *"Recuerden que solo queda esta semana para completar los instrumentos... es muy extenso"*. Se discuten problemas técnicos de acceso a las planillas en línea (Google Sheets), donde algunos usuarios solo tienen permisos de lectura, requiriendo elevar tickets a la mesa de ayuda de la SGD para obtener permisos de edición.
- **MGDE (Marco de Referencia de Gestión de Datos)**: Los resultados de la autoevaluación son consistentemente bajos. Un participante expresa su frustración: *"he contestado a todo NO porque nada de lo que preguntan lo hacemos... me da vergüenza"*. Se concluye que esto es un diagnóstico realista de la falta de madurez en gestión de datos. Se comparte el enlace al formulario en Google Forms para su llenado y se aclara que, a diferencia de otros instrumentos, no requiere una validación formal del Comité de TD institucional.

### 3.2. Gobernanza Interna y Articulación

Se comparten documentos y estrategias para formalizar la gobernanza, como resoluciones para la creación de los **Comités de Transformación Digital** y para el nombramiento de los **Encargados de Ciberseguridad**, un rol que genera preocupación por su alta responsabilidad sin una contrapartida en recursos o remuneración.

## 4. Eje 2: Ecosistema Tecnológico y Plataformas

### 4.1. El Ecosistema Fragmentado de la Gestión Documental

- **El Anhelo del Gestor Documental Transversal**: La noticia del 10/05/25 sobre la transferencia del gestor documental de la ATTA a la SGD es recibida con una mezcla de esperanza y escepticismo, debido a la experiencia con retrasos en otros proyectos de la SGD. La fecha estimada de liberación (segundo semestre de 2026) es considerada muy lejana.
- **Soluciones de Mercado**: Ante el vacío, los GOREs exploran activamente el mercado. Se comparten propuestas, costos y experiencias:
  - **Zecovery (Ceropapel)**: Mencionado por Magallanes y Antofagasta. Se comparten propuestas comerciales y TDRs. Se destaca su integración con DocDigital.
  - **Febos (Escritorio Digital)**: Implementado en Valparaíso, es visto como un caso de éxito. Los Lagos considera su contratación. Su capacidad de contingencia para firma electrónica (e-sign) cuando FirmaGob cae es una ventaja clave.
  - **Otras**: `Methasys` es mencionado como una solución heredada que se busca reemplazar. `Ingsoft` también es parte del ecosistema.
- **DocDigital y FirmaGob**:
  - **DocDigital**: Su uso para comunicaciones internas mediante la creación de "entidades dependientes" (una por cada División/Unidad) es una práctica compartida para evitar el cuello de botella de la Oficina de Partes central. Sin embargo, el proceso de configuración vía ticket a la mesa de ayuda es lento y problemático.
  - **FirmaGob**: Sus caídas (reportadas el 01/10/25 y en otras fechas) son un punto crítico que detiene procesos. Esto ha llevado a la conclusión de que cualquier gestor documental que se adquiera debe tener un mecanismo de firma de contingencia con un proveedor privado.

### 4.2. Interoperabilidad y Servicios Transversales

- **Nodo PISEE**: La implementación del nodo es un tema técnico recurrente. Se comparten las especificaciones de hardware y software utilizadas:
  - **GORE Araucanía**: Debian 12, 2 CPU, 2GB RAM, 20 GB disco.
  - **GORE Aysén**: Ubuntu 24, 4 CPU, 4GB RAM, 100 GB disco.
     La capacitación del 26/06/25 sobre PISEE es difundida en el grupo.
- **fondos.gob.cl**: Es la plataforma preferida para fondos concursables (FNDR 8%) por ser gratuita. Varios GOREs (Tarapacá, O'Higgins, Antofagasta) han migrado o están en proceso. Su principal limitación técnica es que no soporta el ciclo completo del proceso (admisibilidad, evaluación, rendición).
- **Integración con BIP**: Se confirma que el Banco Integrado de Proyectos no está en PISEE. La integración requiere un proceso manual: enviar un oficio a MIDESO para solicitar acceso a su Web Service y luego firmar un convenio.

### 4.3. Sistemas de Gestión Interna: BUK vs. Ingsoft

La elección de un sistema de RRHH es un tema relevante. `BUK` es presentado como una solución SaaS moderna, mientras que `Ingsoft` parece tener una base más amplia de módulos (inventario, bodega, boletas de garantía). Se comparten contactos comerciales de BUK y se discuten sus costos (aprox. $990,000 mensuales para 150 funcionarios). La principal crítica a BUK es la complejidad de su configuración inicial.

## 5. Eje 3: Infraestructura, Presupuesto y Ciberseguridad

### 5.1. Problemas la Infraestructura y Complejidad Presupuestaria

- **Obsolescencia Crítica**: Es uno de los temas más sentidos. Múltiples CTDs (Arica, O'Higgins) reportan tener servidores de 2014, con componentes fallando y sin posibilidad de renovación. La frase *"sigo con los mismos servidores del 2014"* resume la situación.
- **Ineficacia de EVALTIC**: El proceso es ampliamente criticado. Se le considera un ejercicio burocrático que no garantiza la asignación de recursos. Un CTD lo resume: *"el punto 3 resume todo lo que significa Evaltic...!! No sirve para nada..."*. A pesar de esto, deben cumplir con las capacitaciones y la formulación de proyectos.
- **Estrategias Presupuestarias**: Se comparten tácticas para obtener financiamiento, como la discusión sobre si imputar licencias de software y servicios en la nube al **subtítulo 22 (Servicios Generales)** o al **29 (Activos no Financieros)**, dependiendo de la disponibilidad presupuestaria de cada GORE.

### 5.2. Ciberseguridad

- **Anatomía del Incidente en GORE Araucanía (11/06/25)**:
  - **Vector**: Ransomware, posiblemente de la familia `Safepay`.
  - **Impacto**: Cifrado de servidores internos. El malware logró desactivar tanto el antivirus `ESET` como Windows Defender.
  - **Respuesta**: Se activó el protocolo de incidentes, se aisló el segmento de red comprometido y se contactó a la **ANCI**. La recuperación se planeó a partir de respaldos de máquinas virtuales almacenados fuera de la red, en **Google Drive**.
- **Cumplimiento de la Ley Marco de Ciberseguridad**: El incidente acelera la discusión sobre las obligaciones de la Ley 21.663. Surge un debate técnico-legal sobre si los GOREs califican como "servicios esenciales" u "Operadores de Importancia Vital (OIV)". La ANCI instruye la inscripción obligatoria de un encargado de ciberseguridad en su portal, lo que genera dudas sobre quién debe asumir esa alta responsabilidad.

## 6. Eje 4: Capital Humano y Cultura Digital

### 6.1. Brechas de Talento y Capacitación

- **Sobrecarga de los Equipos de TI**: Es una queja común. Los equipos son pequeños y están sobrecargados con múltiples responsabilidades: cumplir con el PMG, dar soporte diario, gestionar la ciberseguridad, liderar proyectos, etc. Esto limita la capacidad de abordar iniciativas más estratégicas.
- **Búsqueda Activa de Formación**: Se comparten activamente oportunidades de formación (cursos de ciberseguridad, diplomados SUBDERE, magísteres) y se discute la idea de traer expertos de renombre como Alejandro Barros para seminarios regionales, demostrando una clara proactividad en la búsqueda de conocimiento.

### 6.2. La Red de CTDs como Soporte Fundamental

### 6.1. La Red como Mesa de Ayuda

- **Configuración de DocDigital**: Ante la dificultad de un GORE para configurar oficinas de partes internas, otro CTD que ya lo había implementado organiza una videollamada para guiarlo paso a paso.
- **Especificaciones Técnicas**: Se piden y comparten specs para la instalación del nodo PISEE, TDRs para sistemas de control de acceso, y propuestas de gestores documentales.
- **Resolución de Bugs**: Cuando FirmaGob o DocDigital presentan fallas, el chat es el primer lugar donde se confirma si es una caída generalizada, antes de levantar tickets formales.

### 6.2. La Red como Base de Conocimiento

- **Normativa y Estándares**: Se comparten documentos como la norma ISO 27001 y se discute su aplicación.
- **Inteligencia de Mercado**: Se intercambian nombres de proveedores, contactos comerciales y costos de licencias y servicios (ej. BUK, Zecovery).
- **Capacitaciones y Eventos**: Se difunden enlaces a webinars y capacitaciones de la SGD, ANCI y otros organismos.

## 7. Conclusiones

1. **Recomendación Técnica (Infraestructura)**: Dada la obsolescencia crítica del hardware y la ineficacia percibida de EVALTIC, se recomienda **explorar modelos de adquisición de infraestructura como servicio (IaaS) a través de Convenio Marco**, lo que permitiría migrar de un modelo CAPEX (inversión) a OPEX (gasto operacional), facilitando su aprobación presupuestaria.

2. **Recomendación Técnica (Seguridad)**: El incidente en Araucanía demuestra que una estrategia de seguridad basada únicamente en antivirus es insuficiente. Se recomienda **implementar un modelo de seguridad por capas**, que incluya soluciones de EDR (Endpoint Detection and Response), segmentación de red, y un plan robusto de respaldos inmutables o fuera de línea (3-2-1), además de fortalecer la capacitación en phishing.

3. **Recomendación Estratégica (Ecosistema de Software)**: La fragmentación en la contratación de gestores documentales y otros sistemas es ineficiente. Se recomienda **formalizar ante la SGD la necesidad de acelerar la entrega del Gestor Documental transversal**. Mientras tanto, los GOREs deberían priorizar soluciones que ofrezcan APIs robustas y se integren nativamente con el ecosistema de Gobierno Digital (ClaveÚnica, FirmaGob, DocDigital).

4. **Recomendación Estratégica (Colaboración)**: La red de CTDs es el activo más valioso para la TD regional. Se recomienda **formalizar y potenciar este espacio**, quizás creando un repositorio centralizado de conocimiento (un "wiki" de los GOREs) donde se documenten las soluciones, TDRs y experiencias compartidas en el chat, para preservar y escalar este conocimiento colectivo.

## 8. Nota sobre el Documento y Solicitud de Retroalimentación

El presente documento corresponde a una síntesis del contenido de este chat. Se ha elaborado con el objetivo de disponer de un insumo para apoyar y articular los procesos de transformación digital en los Gobiernos Regionales, entendiendo que las conversaciones aquí vertidas constituyen un material valioso para comprender la realidad de dicho proceso.

Se solicita a los miembros de este grupo revisar el contenido y validar si representa adecuadamente los temas y cuestiones más relevantes tratados en las discusiones. Se agradecería cualquier comentario sobre posibles imprecisiones, interpretaciones erróneas o la omisión de temas que se consideren importantes.

Este documento ha sido compartido exclusivamente con los miembros de este grupo y no tiene otro fin que el de facilitar el trabajo colaborativo. Si el grupo considera que no debe ser utilizado como fuente de referencia para fines que excedan las conversaciones de este mismo chat, se respetará dicha decisión y su uso será estrictamente interno.

Se agradecen de antemano todos los comentarios y aportes.
