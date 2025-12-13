# Artefacto: Ley 21.719 de Protección de Datos Personales

ID: LEY-21719-DP-MASTER-01
Version: 1.0.0
Status: Draft
Human-Creator: FS
Model-Collaborator: IA-GEMINI
Creation-Date: 2025-10-02
Modification-Date: 2025-10-02
Source: Ley N° 21.719. Regula la protección y el tratamiento de los datos personales y crea la Agencia de Pr - Congreso Nacional de Chile - 2024.txt

---
**BEGIN_LLM_INSTRUCTIONS**

You are an AI agent consuming a Structured Telegraphic Style (STS) artifact. Your primary task is to parse and reason over THIS document with absolute fidelity, using only the rules defined below. This artifact is a self-contained source of truth.

1. **Core Objective**: Maintain perfect fidelity to the information (`meat`) and structure (`skeleton`). Do not summarize, interpret, or infer information not explicitly present. Prohib: Applying these rules to artifact creation or translation tasks; they are exclusively for consumption.
2. **Lexicon Mode & Expansion**: This document uses an **Abbreviated Lexicon**. You MUST treat the following keywords as valid and expand them according to this mapping before processing:
    - `Act:` -> `Action:`
    - `Cause:` -> `Cause:`
    - `Cpt:` -> `Concept:`
    - `Cond:` -> `Condition:`
    - `Ctx:` -> `Context:`
    - `Def:` -> `Definition:`
    - `Dln:` -> `Deadline:`
    - `Fnd:` -> `Foundation:`
    - `ID:` -> `ID:`
    - `Mech:` -> `Mechanism:`
    - `Nat:` -> `Nature:`
    - `Proc:` -> `Process:`
    - `Prohib:` -> `Prohibition:`
    - `Purp:` -> `Purpose:`
    - `Ref:` -> `Reference:`
    - `Req:` -> `Requirement:`
    - `Res:` -> `Result:`
    - `Resp:` -> `Responsible:`
    - `Src:` -> `Source:`
3. **Reference (`Ref:`) Policy**: `Ref:` is for **internal cross-references only**. It MUST point to an `ID:` that exists within THIS document.
4. **Language Invariance Policy**: The `Keywords` are a fixed control vocabulary in English. All `EssentialData` (content following a `Keyword:`) MUST be preserved in its original language (Spanish). Do not translate it.

**END_LLM_INSTRUCTIONS**
---

## Título I: Objeto y Definiciones

### Artículo 1 (Modificado): Objeto y Ámbito de Aplicación

ID: LEY-21719-ART01-01

- Purp: Regular la forma y condiciones del tratamiento y protección de datos personales de personas naturales.
- Fnd: Artículo 19, N° 4, de la Constitución Política de la República.
- Req: Todo tratamiento de datos por persona natural o jurídica, incluidos órganos públicos, debe respetar derechos y libertades de las personas.
- Req: Dicho tratamiento queda sujeto a las disposiciones de esta ley.
- Cpt: Excepciones al régimen de tratamiento.
  - Prohib: Aplicar al tratamiento de datos realizado en ejercicio de las libertades de emitir opinión e informar.
    - Fnd: Reguladas por el artículo 19, N° 12, de la Constitución.
    - Cond: Medios de comunicación social sí quedan sujetos a esta ley para tratamientos con finalidad distinta a opinar e informar.
  - Prohib: Aplicar al tratamiento de datos que efectúen personas naturales en relación con sus actividades personales.

### Artículo 1 bis: Ámbito de Aplicación Territorial

ID: LEY-21719-ART01BIS-01
Purp: Definir las circunstancias en que las disposiciones de la ley son aplicables.

- Cond: La ley se aplica si ocurre cualquiera de las siguientes circunstancias:
  - a) El responsable o mandatario están establecidos o constituidos en territorio nacional.
  - b) El mandatario, sin importar su ubicación, realiza tratamiento a nombre de un responsable establecido en territorio nacional.
  - c) El responsable o mandatario no están establecidos en Chile, pero sus operaciones de tratamiento están destinadas a:
    - i. Ofrecer bienes o servicios a titulares en Chile (con o sin pago requerido).
    - ii. Monitorear el comportamiento de titulares en Chile (incluyendo análisis, rastreo, perfilamiento o predicción).
- Cond: La ley también se aplica a un responsable no establecido en Chile si la legislación nacional le resulta aplicable por contrato o por derecho internacional.

### Artículo 2 (Modificado): Definiciones

ID: LEY-21719-ART02-01
Purp: Establecer las definiciones formales de los términos utilizados en la ley.

- Cpt: Almacenamiento de datos.
  - ID: LEY-21719-DEF-ALMACENAMIENTO-01
  - Def: La conservación o custodia de datos en un registro o base de datos.
- Cpt: Comunicación de datos personales.
  - ID: LEY-21719-DEF-COMUNICACION-01
  - Def: Dar a conocer datos personales por parte del responsable a personas distintas del titular, sin llegar a cederlos o transferirlos.
- Cpt: Dato personal.
  - ID: LEY-21719-DEF-DATO-PERSONAL-01
  - Def: Cualquier información vinculada o referida a una persona natural identificada o identificable.
  - Cpt: Persona identificable.
    - ID: LEY-21719-DEF-PERSONA-IDENTIFICABLE-01
    - Def: Persona cuya identidad puede determinarse, directa o indirectamente, mediante identificadores (nombre, cédula de identidad, elementos de identidad física, fisiológica, genética, psíquica, económica, cultural o social).
    - Cond: Para determinar si es identificable, deben considerarse todos los medios y factores objetivos que razonablemente se podrían usar en el momento del tratamiento.
- Cpt: Datos personales sensibles.
  - ID: LEY-21719-DEF-DATO-SENSIBLE-01
  - Def: Datos personales que se refieren a características físicas o morales, o a hechos de la vida privada o intimidad.
  - Cpt: Tipos de datos sensibles.
    - - Origen étnico o racial.
    - - Afiliación política, sindical o gremial.
    - - Situación socioeconómica.
    - - Convicciones ideológicas o filosóficas.
    - - Creencias religiosas.
    - - Datos relativos a la salud.
    - - Perfil biológico humano.
    - - Datos biométricos.
    - - Información relativa a la vida sexual, orientación sexual e identidad de género.
- Cpt: Fuentes de acceso público.
  - ID: LEY-21719-DEF-FUENTE-PUBLICA-01
  - Def: Bases de datos o conjuntos de datos personales cuyo acceso o consulta puede ser efectuada lícitamente por cualquier persona.
  - Ex: Diario Oficial, medios de comunicación, registros públicos que disponga la ley.
  - Req: El tratamiento de datos de estas fuentes se someterá a esta ley.
- Cpt: Anonimización.
  - ID: LEY-21719-DEF-ANONIMIZACION-01
  - Def: Procedimiento irreversible por el cual un dato personal no puede vincularse a una persona determinada ni permitir su identificación.
  - Cause: Se ha destruido o eliminado el nexo con la información que vincula, asocia o identifica a la persona.
  - Res: Un dato anonimizado deja de ser un dato personal.
- Cpt: Seudonimización.
  - ID: LEY-21719-DEF-SEUDONIMIZACION-01
  - Def: Tratamiento de datos que impide atribuirlos a un titular sin usar información adicional.
  - Cond: La información adicional debe figurar por separado y estar sujeta a medidas técnicas y organizativas para garantizar la no atribución.
- Cpt: Base de datos personales.
  - ID: LEY-21719-DEF-BASE-DATOS-01
  - Def: Conjunto organizado de datos personales que permite relacionarlos y realizar su tratamiento, sin importar finalidad, forma o modalidad de creación, almacenamiento, organización y acceso.
- Cpt: Responsable de datos (o responsable).
  - ID: LEY-21719-DEF-RESPONSABLE-01
  - Def: Persona natural o jurídica, pública o privada, que decide sobre los fines y medios del tratamiento de datos.
  - Ctx: Aplica independientemente de si el tratamiento es directo o a través de un tercero mandatario.
- Cpt: Titular de datos (o titular).
  - ID: LEY-21719-DEF-TITULAR-01
  - Def: Persona natural, identificada o identificable, a quien conciernen o se refieren los datos personales.
- Cpt: Tratamiento de datos.
  - ID: LEY-21719-DEF-TRATAMIENTO-01
  - Def: Cualquier operación o conjunto de operaciones (automatizadas o no) que permitan recolectar, procesar, almacenar, comunicar, transmitir o utilizar datos personales.
- Cpt: Consentimiento.
  - ID: LEY-21719-DEF-CONSENTIMIENTO-01
  - Def: Manifestación de voluntad libre, específica, inequívoca e informada, otorgada por el titular (o su representante/mandatario).
  - Mech: Declaración o una clara acción afirmativa que autoriza el tratamiento.
- Cpt: Derechos del Titular (ARCO+).
  - - Derecho de acceso. ID: LEY-21719-DEF-DERECHO-ACCESO-01. Def: Derecho del titular a solicitar y obtener del responsable confirmación, acceso a sus datos y a la información prevista en la ley.
  - - Derecho de rectificación. ID: LEY-21719-DEF-DERECHO-RECTIFICACION-01. Def: Derecho del titular a solicitar y obtener del responsable la modificación o completitud de sus datos si son inexactos, desactualizados o incompletos.
  - - Derecho de supresión. ID: LEY-21719-DEF-DERECHO-SUPRESION-01. Def: Derecho del titular a solicitar y obtener del responsable la eliminación de sus datos, según causales de ley.
  - - Derecho de oposición. ID: LEY-21719-DEF-DERECHO-OPOSICION-01. Def: Derecho del titular a solicitar y obtener del responsable que no se realice un tratamiento determinado, según causales de ley.
  - - Derecho a la portabilidad. ID: LEY-21719-DEF-DERECHO-PORTABILIDAD-01. Def: Derecho del titular a solicitar y obtener del responsable una copia de sus datos en formato electrónico estructurado, genérico, de uso común, y poder transferirlos a otro responsable. Incluye el derecho a transmisión directa entre responsables si es técnicamente posible.
- Cpt: Cesión de datos personales.
  - ID: LEY-21719-DEF-CESION-01
  - Def: Transferencia de datos personales por parte de un responsable a otro responsable.
- Cpt: Elaboración de perfiles.
  - ID: LEY-21719-DEF-PERFILAMIENTO-01
  - Def: Toda forma de tratamiento automatizado de datos personales para evaluar, analizar o predecir aspectos de una persona natural (rendimiento profesional, situación económica, salud, preferencias, etc.).
- Cpt: Tercero mandatario (o encargado).
  - ID: LEY-21719-DEF-ENCARGADO-01
  - Def: Persona natural o jurídica que trata datos personales por cuenta del responsable.
- Cpt: Agencia.
  - ID: LEY-21719-DEF-AGENCIA-01
  - Def: La Agencia de Protección de Datos Personales.
- Cpt: Registro Nacional de Sanciones y Cumplimiento.
  - ID: LEY-21719-DEF-REGISTRO-SANCIONES-01
  - Def: Registro nacional público administrado por la Agencia.
  - Ctx: Consigna modelos certificados de prevención, responsables que los adoptan y sanciones impuestas.

### Artículo 3 (Sustituido): Principios

ID: LEY-21719-ART03-01
Purp: Definir los principios que rigen el tratamiento de datos personales.

- Cpt: Principio de licitud y lealtad.
  - ID: LEY-21719-PRINCIPIO-LICITUD-01
  - Req: El tratamiento de datos solo puede ser lícito y leal.
  - Req: El responsable debe ser capaz de acreditar la licitud del tratamiento que realiza.
- Cpt: Principio de finalidad.
  - ID: LEY-21719-PRINCIPIO-FINALIDAD-01
  - Req: Los datos deben ser recolectados con fines específicos, explícitos y lícitos.
  - Req: El tratamiento debe limitarse al cumplimiento de dichos fines.
  - Prohib: Tratar datos con fines distintos a los informados al recolectar.
  - Cpt: Excepciones a la prohibición.
    - - El tratamiento es para fines compatibles con los autorizados originalmente.
    - - Existe una relación contractual o precontractual que justifica el tratamiento para una finalidad distinta, siempre que se enmarque en los fines del contrato o sea coherente con las tratativas previas.
    - - El titular otorga nuevamente su consentimiento.
    - - La ley lo disponga.
- Cpt: Principio de proporcionalidad.
  - ID: LEY-21719-PRINCIPIO-PROPORCIONALIDAD-01
  - Req: Los datos tratados deben limitarse a los necesarios, adecuados y pertinentes para los fines del tratamiento.
  - Req: Los datos pueden conservarse solo por el tiempo necesario para cumplir los fines del tratamiento.
  - Act: Después del período, los datos deben ser suprimidos o anonimizados.
    - Ctx: Sin perjuicio de excepciones legales.
  - Cond: Un período mayor requiere autorización legal o consentimiento del titular.
- Cpt: Principio de calidad.
  - ID: LEY-21719-PRINCIPIO-CALIDAD-01
  - Req: Los datos personales deben ser exactos, completos, actuales y pertinentes en relación con su proveniencia y fines.
- Cpt: Principio de responsabilidad.
  - ID: LEY-21719-PRINCIPIO-RESPONSABILIDAD-01
  - Req: Quienes realicen tratamiento de datos son legalmente responsables del cumplimiento de los principios, obligaciones y deberes de la ley.
- Cpt: Principio de seguridad.
  - ID: LEY-21719-PRINCIPIO-SEGURIDAD-01
  - Req: El responsable debe garantizar estándares adecuados de seguridad.
  - Purp: Proteger los datos contra tratamiento no autorizado o ilícito, y contra pérdida, filtración, daño accidental o destrucción.
  - Req: Las medidas de seguridad deben ser apropiadas y acordes con el tratamiento y la naturaleza de los datos.
- Cpt: Principio de transparencia e información.
  - ID: LEY-21719-PRINCIPIO-TRANSPARENCIA-01
  - Req: El responsable debe entregar al titular toda la información necesaria para el ejercicio de sus derechos.
  - Ctx: Incluye políticas y prácticas sobre el tratamiento, las cuales deben estar permanentemente accesibles de manera precisa, clara, inequívoca y gratuita.
  - Req: El responsable debe adoptar medidas adecuadas y oportunas para facilitar al titular el acceso a la información.
- Cpt: Principio de confidencialidad.
  - ID: LEY-21719-PRINCIPIO-CONFIDENCIALIDAD-01
  - Req: El responsable y quienes accedan a los datos deben guardar secreto o confidencialidad.
  - Req: El responsable debe establecer controles y medidas adecuadas para preservar el secreto o confidencialidad.
  - Cond: Este deber subsiste aún después de concluida la relación con el titular.

## Título I (Reemplazado): De los derechos del titular de datos personales

### Artículo 4: Derechos del titular de datos

ID: LEY-21719-ART04-01
Purp: Establecer los derechos fundamentales del titular de datos.

- Cpt: El titular tiene derecho de acceso, rectificación, supresión, oposición, portabilidad y bloqueo de sus datos personales.
  - Ref: LEY-21719-DEF-DERECHO-ACCESO-01
  - Ref: LEY-21719-DEF-DERECHO-RECTIFICACION-01
  - Ref: LEY-21719-DEF-DERECHO-SUPRESION-01
  - Ref: LEY-21719-DEF-DERECHO-OPOSICION-01
  - Ref: LEY-21719-DEF-DERECHO-PORTABILIDAD-01
- Mech: El titular puede actuar por sí mismo o a través de representante legal o mandatario.
- Nat: Tales derechos son personales, intransferibles e irrenunciables.
- Prohib: Limitar estos derechos por acto o convención.
- Cond: En caso de fallecimiento del titular, los herederos pueden ejercer los derechos.
  - Prohib: Herederos no pueden acceder, rectificar o suprimir datos si el fallecido lo prohibió expresamente o una ley lo establece.

### Artículo 5: Derecho de acceso

ID: LEY-21719-ART05-01
Purp: Detallar el alcance del derecho de acceso.
Ref: LEY-21719-DEF-DERECHO-ACCESO-01

- Cpt: El titular tiene derecho a solicitar y obtener del responsable:
  - 1. Confirmación sobre si sus datos personales están siendo tratados.
  - 2. En caso afirmativo, acceso a dichos datos y a la siguiente información:
    - a) Los datos tratados y su origen.
    - b) La finalidad o finalidades del tratamiento.
    - c) Las categorías, clases, tipos o identidad de destinatarios a quienes se comunicaron o cederán los datos.
    - d) El período de tiempo durante el cual los datos serán tratados.
    - e) Los intereses legítimos del responsable (si el tratamiento se basa en Art. 13, letra d).
    - f) Información significativa sobre la lógica aplicada en tratamiento automatizado (Art. 8 bis).
- Req: El responsable siempre está obligado a entregar información y dar acceso.
- Cpt: Excepción.
  - Cond: Cuando una ley disponga expresamente lo contrario.

### Artículo 6: Derecho de rectificación

ID: LEY-21719-ART06-01
Purp: Detallar el alcance del derecho de rectificación.
Ref: LEY-21719-DEF-DERECHO-RECTIFICACION-01

- Cpt: El titular tiene derecho a solicitar y obtener del responsable la rectificación de datos personales que sean inexactos, desactualizados o incompletos.
- Req: Los datos rectificados deben ser comunicados a las personas o entidades a quienes el responsable los haya comunicado o cedido.
  - Cpt: Excepción.
    - Cond: Salvo que dicha comunicación sea imposible o exija un esfuerzo desproporcionado.
- Prohib: Una vez efectuada la rectificación, no se podrán volver a tratar los datos sin rectificar.

### Artículo 7: Derecho de supresión

ID: LEY-21719-ART07-01
Purp: Detallar el alcance del derecho de supresión.
Ref: LEY-21719-DEF-DERECHO-SUPRESION-01

- Cpt: El titular tiene derecho a solicitar y obtener del responsable la eliminación de sus datos personales en los siguientes casos:
  - a) Los datos ya no son necesarios para los fines para los que fueron recogidos.
  - b) El titular ha revocado su consentimiento y no existe otro fundamento legal para el tratamiento.
  - c) Los datos han sido obtenidos o tratados ilícitamente por el responsable.
  - d) Se trata de datos caducos.
  - e) La supresión es necesaria para cumplir una sentencia judicial, resolución de la autoridad de protección de datos o una obligación legal.
  - f) El titular ejerció su derecho de oposición (Art. 8) y no existe otro fundamento legal para el tratamiento.
- Cpt: Casos en que no procede la supresión.
  - Cond: El tratamiento es necesario para:
    - i. Ejercer el derecho a las libertades de emitir opinión e informar.
    - ii. Cumplir una obligación legal o ejecutar un contrato entre titular y responsable.
    - iii. Cumplir una función pública o ejecutar una actividad de interés público.
    - iv. Razones de interés público en el área de la salud pública.
    - v. Fines históricos, estadísticos o científicos, o estudios de interés público.
    - vi. La formulación, ejercicio o defensa de una reclamación administrativa o judicial.

### Artículo 8: Derecho de Oposición

ID: LEY-21719-ART08-01
Purp: Detallar el alcance del derecho de oposición.
Ref: LEY-21719-DEF-DERECHO-OPOSICION-01

- Cpt: El titular tiene derecho a oponerse a un tratamiento específico en los siguientes casos:
  - a) La base de licitud es la satisfacción de intereses legítimos del responsable.
    - Cond: Puede ejercerse en cualquier momento.
    - Res: El responsable debe dejar de tratar los datos.
    - Cpt: Excepción.
      - Cond: Salvo que acredite motivos legítimos imperiosos que prevalezcan sobre los intereses, derechos y libertades del titular, o para la defensa de reclamaciones.
  - b) El tratamiento es exclusivamente para mercadotecnia o marketing directo (incluida la elaboración de perfiles).
    - Ref: LEY-21719-ART08BIS-01
  - c) El tratamiento es sobre datos de una fuente de acceso público y no hay otro fundamento legal.
- Cpt: Casos en que no procede la oposición.
  - Cond: Cuando el tratamiento se realice con fines de investigación científica o histórica o fines estadísticos, y sea necesario para cumplir una función pública o una actividad de interés público.

### Artículo 8 bis: Decisiones individuales automatizadas, incluida la elaboración de perfiles

ID: LEY-21719-ART08BIS-01
Purp: Regular el derecho a oponerse a decisiones automatizadas.
Ref: LEY-21719-DEF-PERFILAMIENTO-01

- Cpt: El titular tiene derecho a oponerse y a no ser objeto de decisiones basadas únicamente en tratamiento automatizado (incluido el perfilamiento) que produzcan efectos jurídicos en él o le afecten significativamente.
- Cpt: Casos en que la regla anterior no se aplica.
  - Cond:
    - a) La decisión es necesaria para la celebración o ejecución de un contrato entre titular y responsable.
    - b) Existe consentimiento previo y expreso del titular.
    - c) La ley lo señala, disponiendo salvaguardas a los derechos y libertades del titular.
- Req: En todos los casos de decisiones automatizadas (incluidas las excepciones a, b, y c), el responsable debe adoptar medidas para asegurar:
  - - Los derechos y libertades del titular.
  - - Su derecho a la información y transparencia.
  - - El derecho a obtener una explicación.
  - - El derecho a la intervención humana.
  - - El derecho a expresar su punto de vista.
  - - El derecho a solicitar la revisión de la decisión.

### Artículo 8 ter: Derecho de bloqueo del tratamiento

ID: LEY-21719-ART08TER-01
Purp: Establecer el derecho a la suspensión temporal del tratamiento.

- Cpt: El titular tiene derecho a solicitar la suspensión temporal (bloqueo) de cualquier operación de tratamiento en dos situaciones:
  - 1. Cuando formule una solicitud de rectificación, supresión u oposición, mientras dicha solicitud se resuelve.
  - 2. Como alternativa al derecho de supresión en los casos del Art. 7.
- Ctx: El ejercicio de este derecho no afecta el almacenamiento de los datos por parte del responsable.

### Artículo 9: Derecho a la portabilidad de los datos personales

ID: LEY-21719-ART09-01
Purp: Detallar el alcance del derecho a la portabilidad.
Ref: LEY-21719-DEF-DERECHO-PORTABILIDAD-01

- Cpt: El titular tiene derecho a solicitar y recibir una copia de los datos personales que haya facilitado al responsable, y a comunicarlos o transferirlos a otro responsable.
- Cond: Deben concurrir las siguientes circunstancias:
  - a) El tratamiento se realiza en forma automatizada.
  - b) El tratamiento está basado en el consentimiento del titular.
- Cpt: Formato de los datos.
  - Req: Formato electrónico estructurado, genérico y de uso común, que permita ser operado por distintos sistemas.
- Req: El responsable debe usar medios expeditos, menos onerosos y sin poner trabas para el ejercicio de este derecho.
- Req: El responsable debe comunicar de manera clara y precisa las medidas necesarias y las características técnicas para obtener los datos.
- Cpt: El titular tiene derecho a que sus datos se transmitan directamente de responsable a responsable cuando sea técnicamente posible.
- Ctx: El ejercicio de la portabilidad no implica la supresión automática de los datos ante el responsable cedente, a menos que el titular lo pida conjuntamente.

### Artículo 10: Forma y medios de ejercer los derechos del titular

ID: LEY-21719-ART10-01
Purp: Establecer el procedimiento general para el ejercicio de derechos.

- Mech: Los derechos se ejercen por el titular ante el responsable de datos.
- Cond: Si los datos son tratados por diversos responsables, el titular puede ejercer sus derechos ante cualquiera de ellos.
- Req: Para personas jurídicas no constituidas en Chile, el responsable debe señalar ante la Agencia un medio de comunicación electrónico válido para que el titular ejerça sus derechos y para recibir notificaciones.
  - Req: El responsable debe mantener esta información actualizada.
- Req: Los responsables deben implementar mecanismos y herramientas tecnológicas que permitan un ejercicio expedito, ágil y eficaz.
  - Req: Los medios dispuestos deben ser de operación sencilla.
- Cpt: Gratuidad y Costos.
  - Req: El ejercicio de los derechos de rectificación, supresión y oposición siempre son gratuitos.
  - Req: El derecho de acceso también es gratuito, al menos trimestralmente.
  - Cond: El responsable solo puede exigir pago de costos directos cuando el titular ejerce el derecho de acceso o portabilidad más de una vez en el trimestre.
  - Ctx: Los parámetros para determinar costos serán definidos por la Agencia mediante instrucción general.
- Resp: La Agencia velará por el efectivo ejercicio y cumplimiento de los derechos.

### Artículo 11: Procedimiento ante el responsable de datos

ID: LEY-21719-ART11-01
Purp: Detallar el procedimiento formal de solicitud ante el responsable.

- Proc: Solicitud del Titular.
  - 1. El titular debe presentar una solicitud escrita al responsable.
  - 2. Medio: Correo electrónico establecido, formulario de contacto o medio electrónico equivalente.
  - 3. Contenido mínimo de la solicitud:
    - a) Individualización y autenticación de identidad del titular (o representante).
    - b) Indicación de un domicilio o correo electrónico para la respuesta.
    - c) Identificación de los datos o tratamiento sobre los que se ejerce el derecho.
    - d) Requisitos específicos por derecho:
      - Rectificación: Indicar modificaciones precisas y adjuntar antecedentes sustentatorios.
      - Supresión: Indicar causal y adjuntar antecedentes si corresponde.
      - Oposición: Indicar causal y fundamentar brevemente (para Art. 8, letra a).
- Proc: Respuesta del Responsable.
  - 1. Recibida la solicitud, el responsable debe acusar recibo.
  - 2. Dln: Debe pronunciarse en un máximo de 30 días corridos desde el ingreso.
    - Cond: Plazo prorrogable por una sola vez, hasta por 30 días corridos.
  - 3. Mech: La respuesta debe ser por escrito al domicilio o correo electrónico fijado por el titular.
  - 4. Req: El responsable debe almacenar respaldos que demuestren el envío, fecha y contenido de la respuesta.
- Proc: Denegación de la Solicitud.
  - Cond: En caso de denegación total o parcial, el responsable debe fundar su decisión, indicando causa y antecedentes.
  - Req: Debe informar al titular que tiene 30 días hábiles para reclamar ante la Agencia.
- Proc: Silencio del Responsable.
  - Cond: Transcurrido el plazo sin respuesta, el titular puede reclamar directamente ante la Agencia.
- Proc: Bloqueo Temporal.
  - Cpt: Al formular solicitud de rectificación, supresión u oposición, el titular puede solicitar el bloqueo temporal de los datos.
  - Dln: El responsable debe responder a la solicitud de bloqueo en 2 días hábiles.
  - Prohib: Mientras no resuelva la solicitud de bloqueo, el responsable no puede tratar los datos del requerimiento.

## Título II (Reemplazado): Del tratamiento de los datos personales y de las categorías especiales de datos

### Párrafo Primero: Del consentimiento del titular, de las obligaciones y deberes del responsable y del tratamiento de datos en general

### Artículo 12: Regla general del tratamiento de datos

ID: LEY-21719-ART12-01
Purp: Establecer el consentimiento como la base principal de licitud.

- Cpt: El tratamiento de datos es lícito cuando el titular otorga su consentimiento.
- Req: Características del consentimiento.
  - - Debe ser libre, informado y específico en cuanto a su finalidad.
  - - Debe manifestarse de forma previa e inequívoca.
  - - Mech: Declaración verbal, escrita, medio electrónico o acto afirmativo claro.
- Cond: Si el consentimiento lo otorga un mandatario, debe estar expresamente facultado para ello.
- Cpt: Revocación del consentimiento.
  - Cpt: El titular puede revocar el consentimiento en cualquier momento y sin expresión de causa.
  - Mech: Usando medios similares o equivalentes a los usados para otorgarlo.
  - Prohib: La revocación no tendrá efectos retroactivos.
- Req: Los medios para otorgar o revocar el consentimiento deben ser expeditos, fidedignos, gratuitos y estar permanentemente disponibles.
- Cpt: Presunción de falta de libertad.
  - Cond: Se presume que el consentimiento no fue libremente otorgado si el responsable lo recaba en el marco de un contrato o servicio donde la recolección no es necesaria.
  - Cpt: Excepción a la presunción.
    - Cond: No se aplica si la única contraprestación por el bien, servicio o beneficio es el consentimiento para tratar datos.
- Resp: Corresponde al responsable probar que contó con el consentimiento y que el tratamiento fue lícito, leal y transparente.

### Artículo 13: Otras fuentes de licitud del tratamiento de datos

ID: LEY-21719-ART13-01
Purp: Establecer los casos en que el tratamiento es lícito sin el consentimiento del titular.

- Cpt: Es lícito el tratamiento sin consentimiento en los siguientes casos:
  - a) Se refiere a obligaciones de carácter económico, financiero, bancario o comercial, conforme a las normas del Título III.
  - b) Es necesario para el cumplimiento de una obligación legal o lo disponga la ley.
  - c) Es necesario para la celebración o ejecución de un contrato entre titular y responsable, o para medidas precontractuales a solicitud del titular.
  - d) Es necesario para la satisfacción de intereses legítimos del responsable o de un tercero.
    - Cond: Siempre que no se afecten los derechos y libertades del titular.
    - Req: El titular siempre podrá exigir ser informado sobre el tratamiento y el interés legítimo en que se basa.
  - e) Es necesario para la formulación, ejercicio o defensa de un derecho ante tribunales u órganos públicos.
- Resp: El responsable deberá acreditar la licitud del tratamiento.

### Artículo 14: Obligaciones del responsable de datos

ID: LEY-21719-ART14-01
Purp: Listar las obligaciones generales del responsable de datos.

- Req: El responsable tiene las siguientes obligaciones:
  - a) Informar y poner a disposición del titular los antecedentes que acrediten la licitud del tratamiento.
  - b) Asegurar que los datos se recojan de fuentes lícitas con fines específicos, explícitos y lícitos, y que su tratamiento se limite a esos fines.
  - c) Comunicar o ceder información exacta, completa y actual.
  - d) Suprimir o anonimizar los datos personales obtenidos para medidas precontractuales.
  - e) Cumplir con los demás deberes, principios y obligaciones de esta ley.
- Req: Responsables sin domicilio en Chile que traten datos de residentes deben señalar y mantener un contacto electrónico para comunicaciones de titulares y la Agencia.

### Artículo 14 bis: Deber de secreto o confidencialidad

ID: LEY-21719-ART14BIS-01
Purp: Establecer la obligación de confidencialidad.
Ref: LEY-21719-PRINCIPIO-CONFIDENCIALIDAD-01

- Req: El responsable está obligado a mantener secreto o confidencialidad sobre los datos personales.
  - Cpt: Excepción.
    - Cond: Salvo cuando el titular los hubiere hecho manifiestamente públicos.
- Cond: Este deber subsiste aún después de concluida la relación con el titular.
- Cond: Si el responsable realiza acciones sobre datos de fuentes públicas (organizar, clasificar, combinar), los datos resultantes quedan protegidos por este deber.
- Cpt: El deber de secreto no obsta a:
  - - Comunicaciones o cesiones de datos que deba realizar por ley.
  - - Cumplimiento de la obligación de dar acceso al titular e informar origen de los datos.
- Req: El responsable debe adoptar medidas para que sus dependientes o encargados cumplan este deber.
- Ctx: Quienes requieran y remitan información según el artículo 24 también quedan sujetos a esta obligación.

### Artículo 14 ter: Deber de información y transparencia

ID: LEY-21719-ART14TER-01
Purp: Establecer la información que el responsable debe mantener a disposición del público.
Ref: LEY-21719-PRINCIPIO-TRANSPARENCIA-01

- Req: El responsable debe facilitar y mantener permanentemente a disposición del público (en sitio web o medio equivalente) la siguiente información mínima:
  - a) Política de tratamiento de datos personales (con fecha y versión).
  - b) Individualización del responsable, su representante legal y el encargado de prevención (si existe).
  - c) Domicilio postal y medio de contacto electrónico para solicitudes de los titulares.
  - d) Descripción de los tratamientos:
    - - Categorías/tipos de datos tratados.
    - - Descripción genérica del universo de personas en sus bases de datos.
    - - Destinatarios a los que se prevé comunicar o ceder datos.
    - - Finalidades de los tratamientos.
    - - Base de legitimidad del tratamiento (y cuáles son los intereses legítimos, si aplica).
  - e) Política y medidas de seguridad adoptadas.
  - f) El derecho que asiste al titular para ejercer sus derechos (acceso, rectificación, etc.).
  - g) El derecho que asiste al titular de recurrir ante la Agencia si el responsable no responde.
  - h) Si hay transferencia internacional de datos, si el país de destino ofrece nivel adecuado de protección y, si no, las garantías que justifican la transferencia.
  - i) El período de conservación de los datos.
  - j) La fuente de los datos y si proceden de fuentes de acceso público.
  - k) Si el tratamiento se basa en consentimiento, la existencia del derecho a retirarlo en cualquier momento.
  - l) La existencia de decisiones automatizadas (incluido perfilamiento) y, en tal caso, información sobre la lógica aplicada y consecuencias para el titular.

### Artículo 14 quáter: Deber de protección desde el diseño y por defecto

ID: LEY-21719-ART14QUATER-01
Purp: Establecer los principios de privacidad desde el diseño y por defecto.

- Cpt: Protección desde el diseño.
  - Req: El responsable debe aplicar medidas técnicas y organizativas adecuadas desde el diseño (antes y durante el tratamiento).
  - Purp: Cumplir los principios y derechos de los titulares.
  - Ctx: Las medidas deben considerar el estado de la técnica, costos de implementación, naturaleza, ámbito, contexto, fines y riesgos del tratamiento.
- Cpt: Protección por defecto.
  - Req: El responsable debe aplicar medidas técnicas y organizativas para garantizar que, por defecto, solo se traten los datos personales específicos y estrictamente necesarios.
  - Ctx: Se debe considerar el número de datos recogidos, la extensión del tratamiento, el plazo de conservación y su accesibilidad.

### Artículo 14 quinquies: Deber de adoptar medidas de seguridad

ID: LEY-21719-ART14QUINQUIES-01
Purp: Detallar la obligación de implementar medidas de seguridad.
Ref: LEY-21719-PRINCIPIO-SEGURIDAD-01

- Req: El responsable debe adoptar las medidas necesarias para resguardar el cumplimiento del principio de seguridad.
- Ctx: Debe considerar el estado de la técnica, costos, naturaleza, alcance, contexto, fines, probabilidad y gravedad de los riesgos.
- Req: Las medidas deben asegurar la confidencialidad, integridad, disponibilidad y resiliencia de los sistemas.
- Req: Deben evitar la alteración, destrucción, pérdida, tratamiento o acceso no autorizado.
- Cpt: Ejemplos de medidas técnicas y organizativas apropiadas.
  - a) La seudonimización y el cifrado de datos personales.
  - b) La capacidad de garantizar la confidencialidad, integridad, disponibilidad y resiliencia permanentes.
  - c) La capacidad de restaurar la disponibilidad y el acceso a los datos de forma rápida en caso de incidente.
  - d) Un proceso de verificación, evaluación y valoración regulares de la eficacia de las medidas.
- Resp: En caso de controversia, corresponderá al responsable acreditar la existencia y funcionamiento de las medidas adoptadas.

### Artículo 14 sexies: Deber de reportar las vulneraciones a las medidas de seguridad

ID: LEY-21719-ART14SEXIES-01
Purp: Establecer la obligación de notificar brechas de seguridad.

- Req: El responsable debe reportar a la Agencia las vulneraciones a las medidas de seguridad.
- Cond: El reporte aplica a vulneraciones que ocasionen destrucción, filtración, pérdida, alteración accidental/ilícita, o comunicación/acceso no autorizado de datos.
- Cond: Debe existir un riesgo razonable para los derechos y libertades de los titulares.
- Dln: Por los medios más expeditos posibles y sin dilaciones indebidas.
- Req: El responsable debe registrar estas comunicaciones, describiendo:
  - - La naturaleza de la vulneración.
  - - Sus efectos.
  - - Categorías de datos y número aproximado de titulares afectados.
  - - Medidas adoptadas para gestionarlas y precaver incidentes futuros.
- Req: El responsable también debe comunicar la vulneración a los titulares de los datos.
- Cond: Cuando las vulneraciones se refieran a:
  - - Datos personales sensibles.
  - - Datos de niños y niñas menores de catorce años.
  - - Datos relativos a obligaciones de carácter económico, financiero, bancario o comercial.
- Req: La comunicación al titular debe ser en lenguaje claro y sencillo, singularizando los datos afectados, posibles consecuencias y medidas adoptadas.
- Mech: La notificación debe ser a cada titular afectado. Si no es posible, mediante aviso en un medio de comunicación masivo de alcance nacional.

### Artículo 14 septies: Diferenciación de estándares de cumplimiento

ID: LEY-21719-ART14SEPTIES-01
Purp: Permitir que los estándares de cumplimiento sean diferenciados.

- Cpt: Los estándares mínimos para los deberes de información (Art. 14 ter) y seguridad (Art. 14 quinquies) serán determinados considerando:
  - - El tipo de dato.
  - - Si el responsable es persona natural o jurídica.
  - - El tamaño de la entidad o empresa.
  - - La actividad que desarrolla.
  - - El volumen, naturaleza y finalidades de los datos que trata.
- Resp: La Agencia determinará estos estándares y medidas diferenciadas mediante instrucción general.

### Artículo 15: Cesión de datos personales

ID: LEY-21719-ART15-01
Purp: Regular la transferencia de datos a otro responsable.
Ref: LEY-21719-DEF-CESION-01

- Cpt: La cesión de datos es lícita en los siguientes casos:
  - - Con el consentimiento del titular para el cumplimiento de los fines del tratamiento.
  - - Cuando la cesión sea necesaria para la ejecución de un contrato en que es parte el titular.
  - - Cuando exista un interés legítimo del cedente o del cesionario (en los términos del Art. 13, letra d).
  - - Cuando lo disponga la ley.
- Cond: Si el consentimiento original no consideró la cesión, debe recabarse antes de que se produzca.
- Req: La cesión de datos debe constar por escrito o medio electrónico idóneo.
- Req: El registro de la cesión debe individualizar a las partes, los datos, las finalidades previstas y otros acuerdos.
- Req: El cesionario debe realizar el tratamiento de conformidad a las finalidades establecidas en el contrato de cesión.
- Res: Una vez perfeccionada la cesión, el cesionario adquiere la condición de responsable de datos.
- Ctx: El cedente también mantiene la calidad de responsable respecto de las operaciones que continúe realizando.
- Cpt: Nulidad de la cesión.
  - Cond: Si se verifica una cesión sin el consentimiento necesario del titular, la cesión será nula.
  - Req: El cesionario deberá suprimir todos los datos recibidos.

### Artículo 15 bis: Tratamiento de datos a través de un tercero mandatario o encargado

ID: LEY-21719-ART15BIS-01
Purp: Regular el tratamiento de datos por parte de un encargado.
Ref: LEY-21719-DEF-ENCARGADO-01

- Cpt: El responsable puede efectuar el tratamiento directamente o a través de un encargado.
- Req: El encargado realiza el tratamiento conforme al encargo y a las instrucciones del responsable.
- Prohib: El encargado no puede tratar los datos para un objeto distinto al convenido.
- Prohib: El encargado no puede ceder o entregar los datos sin autorización expresa del responsable.
- Resp: Si el encargado incumple (trata para fin distinto, cede sin autorización), se le considerará responsable de datos.
  - Res: Deberá responder personalmente por las infracciones y solidariamente con el responsable original por los daños.
- Fnd: El tratamiento se regirá por un contrato entre responsable y encargado.
- Req: El contrato debe establecer el objeto, duración, finalidad, tipo de datos, categorías de titulares y derechos/obligaciones de las partes.
- Prohib: El encargado no podrá delegar el encargo, salvo autorización específica y por escrito del responsable.
- Req: El encargado debe cumplir con los deberes de secreto (Art. 14 bis) y seguridad (Art. 14 quinquies).
- Req: El encargado debe reportar al responsable las vulneraciones a las medidas de seguridad.
- Act: Cumplida la prestación del servicio, los datos en poder del encargado deben ser suprimidos o devueltos al responsable.

### Artículo 15 ter: Evaluación de impacto en protección de datos personales

ID: LEY-21719-ART15TER-01
Purp: Establecer la obligación de realizar Evaluaciones de Impacto (EIPD).

- Req: El responsable deberá realizar una EIPD previo al inicio de las operaciones.
- Cond: Cuando sea probable que un tipo de tratamiento pueda producir un alto riesgo para los derechos de los titulares (por su naturaleza, alcance, contexto, tecnología o fines).
- Cpt: Casos en que la EIPD siempre se requerirá:
  - a) Evaluación sistemática y exhaustiva de aspectos personales basada en tratamiento automatizado (ej. perfilamiento) que produzca efectos jurídicos significativos.
  - b) Tratamiento masivo de datos o a gran escala.
  - c) Tratamiento que implique observación o monitoreo sistemático de una zona de acceso público.
  - d) Tratamiento de datos sensibles en las hipótesis de excepción del consentimiento.
- Resp: La Agencia publicará una lista orientativa de operaciones que requieran (o no) una EIPD.
- Resp: La Agencia establecerá las orientaciones mínimas para realizar la EIPD.
- Mech: El responsable podrá consultar a la Agencia si el resultado de la EIPD demuestra un alto riesgo.

### Párrafo Segundo: Del tratamiento de los datos personales sensibles

### Artículo 16: Regla general para el tratamiento de datos personales sensibles

ID: LEY-21719-ART16-01
Purp: Establecer las condiciones para el tratamiento de datos sensibles.
Ref: LEY-21719-DEF-DATO-SENSIBLE-01

- Cpt: Regla General.
  - Req: El tratamiento solo puede realizarse cuando el titular manifiesta su consentimiento en forma expresa.
  - Mech: Declaración escrita, verbal o por un medio tecnológico equivalente.
- Cpt: Excepciones (tratamiento lícito sin consentimiento).
  - Cond:
    - a) El titular ha hecho los datos manifiestamente públicos y el tratamiento se relaciona con los fines para los que fueron publicados.
    - b) El tratamiento lo realiza una persona jurídica sin fines de lucro (finalidad política, filosófica, religiosa, cultural, sindical o gremial) y se cumplen todas las siguientes condiciones:
      - i. Se refiere exclusivamente a sus miembros o afiliados.
      - ii. Tiene por objeto cumplir las finalidades específicas de la institución.
      - iii. La persona jurídica otorga garantías para evitar filtraciones o uso no autorizado.
      - iv. Los datos no se comunican o ceden a terceros.
    - c) El tratamiento es indispensable para salvaguardar la vida, salud o integridad del titular o de otra persona, y el titular está impedido de dar su consentimiento.
    - d) El tratamiento es necesario para la formulación, ejercicio o defensa de un derecho ante tribunales o un órgano administrativo.
    - e) El tratamiento es necesario para el ejercicio de derechos y cumplimiento de obligaciones en el ámbito laboral o de seguridad social, en el marco de la ley.
    - f) El tratamiento lo autoriza o mandata expresamente la ley.

### Artículo 16 bis: Datos personales sensibles relativos a la salud y al perfil biológico humano

ID: LEY-21719-ART16BIS-01
Purp: Establecer reglas específicas para el tratamiento de datos de salud y biológicos.

- Req: Con consentimiento expreso (Art. 16), estos datos solo podrán ser tratados para los fines previstos por las leyes especiales en materia sanitaria.
- Cpt: Excepciones (tratamiento lícito sin consentimiento).
  - Cond:
    - a) Es indispensable para salvaguardar la vida o integridad del titular u otra persona, y el titular está impedido de dar consentimiento.
    - b) En casos de alerta sanitaria legalmente decretada.
    - c) Son utilizados con fines históricos, estadísticos o científicos para estudios de interés público, beneficio de la salud humana, o desarrollo de productos médicos.
      - Req: Los resultados de estudios que se publiquen deben ser previamente anonimizados.
    - d) Es necesario para la formulación, ejercicio o defensa de un derecho ante tribunales o un órgano administrativo.
    - e) Es necesario para fines de medicina preventiva o laboral, evaluación de capacidad laboral, diagnóstico médico, prestación de asistencia sanitaria o social, o gestión de sistemas de salud.
    - f) La ley lo permite e indica expresamente la finalidad del tratamiento.
- Prohib: Tratamiento y cesión de datos de salud/biológicos y muestras biológicas si han sido recolectados en ámbito laboral, educativo, deportivo, social, de seguros, o de identificación.
  - Cpt: Excepción.
    - Cond: Salvo que la ley expresamente lo autorice en casos calificados y se refiera a uno de los casos mencionados en este artículo.

### Artículo 16 ter: Datos personales biométricos

ID: LEY-21719-ART16TER-01
Purp: Regular el tratamiento de datos biométricos.

- Def: Datos obtenidos de un tratamiento técnico específico sobre características físicas, fisiológicas o conductuales que permiten la identificación única de una persona.
- Ex: Huella digital, iris, rasgos faciales, voz.
- Req: Solo podrán tratarse con consentimiento expreso (Art. 16).
- Req: El responsable debe proporcionar al titular la siguiente información específica:
  - a) La identificación del sistema biométrico usado.
  - b) La finalidad específica para la cual serán utilizados.
  - c) El período durante el cual serán utilizados.
  - d) La forma en que el titular puede ejercer sus derechos.
- Cpt: Tratamiento sin consentimiento.
  - Cond: Solo en los casos señalados en el inciso segundo del artículo 16 bis.
    - Ref: LEY-21719-ART16BIS-01

### Párrafo Tercero: Del tratamiento de categorías especiales de datos personales

### Artículo 16 quáter: Datos personales relativos a los niños, niñas y adolescentes

ID: LEY-21719-ART16QUATER-01
Purp: Establecer reglas para el tratamiento de datos de menores de edad.

- Def: Niños/niñas: menores de 14 años. Adolescentes: mayores de 14 y menores de 18 años.
- Fnd: El tratamiento solo puede realizarse atendiendo al interés superior del menor y al respeto de su autonomía progresiva.
- Cpt: Tratamiento de datos de niños y niñas (<14).
  - Req: Se requiere el consentimiento de sus padres, representantes legales o quien tenga su cuidado personal.
  - Cpt: Excepción.
    - Cond: Salvo que la ley expresamente lo autorice o mandate.
- Cpt: Tratamiento de datos de adolescentes (>=14, <18).
  - Cpt: Se podrán tratar de acuerdo a las normas de autorización para adultos.
  - Cpt: Excepción (datos sensibles).
    - Req: Para datos sensibles de adolescentes menores de 16 años, se requiere consentimiento de padres, representantes o cuidadores.
    - Cond: Salvo que la ley expresamente lo autorice o mandate.
- Resp: Establecimientos educacionales y toda entidad que trate datos de menores tienen la obligación especial de velar por el uso lícito y la protección de dicha información.

### Artículo 16 quinquies: Datos personales con fines históricos, estadísticos, científicos y de estudios o investigaciones

ID: LEY-21719-ART16QUINQUIES-01
Purp: Regular el tratamiento de datos para fines de investigación.

- Cpt: Se entiende que existe un interés legítimo en el tratamiento de datos (incluidos los de organismos públicos) cuando se realiza exclusivamente con fines históricos, estadísticos, científicos y para estudios o investigaciones.
- Cond: Todos estos fines deben atender al interés público.
- Req: Los responsables deben adoptar y acreditar el cumplimiento de medidas de calidad y seguridad para resguardar que los datos se usen exclusivamente para tales fines.
- Req: Para datos sensibles, el responsable debe identificar riesgos e implementar medidas de mitigación.
- Cond: Cumplidas estas condiciones, el responsable podrá almacenar y utilizar los datos por un período indeterminado.
- Req: Las publicaciones con resultados deben adoptar medidas para anonimizar los datos que se publiquen.

### Artículo 16 sexies: Datos de geolocalización

ID: LEY-21719-ART16SEXIES-01
Purp: Regular el tratamiento de datos de geolocalización.

- Cpt: El tratamiento se podrá realizar bajo las mismas fuentes de licitud establecidas en los artículos 12 (consentimiento) y 13 (otras bases de licitud).
- Req: El titular debe ser informado de manera clara, suficiente y oportuna sobre:
  - - El tipo de datos de geolocalización que serán tratados.
  - - La finalidad y duración del tratamiento.
  - - Si los datos se comunicarán o cederán a un tercero para un servicio con valor añadido.

### Artículo 17 (Modificado): Tratamiento de datos relativos a obligaciones de carácter financiero, bancario o comercial

ID: LEY-21719-ART17-01

- Req: Los responsables deben suprimir de sus registros toda información personal relativa a obligaciones prescritas, sin necesidad de solicitud, orden judicial o instrucción.

### Artículo 18 (Modificado): Limitación del tratamiento de datos para obligaciones financieras, bancarias o comerciales

ID: LEY-21719-ART18-01

- Ctx: Se agrega epígrafe para clarificar el propósito del artículo.

### Artículo 19 (Modificado): Efectos de la extinción de la obligación

ID: LEY-21719-ART19-01

- Ctx: Se actualizan referencias internas y se alinea con el nuevo Título VII sobre el procedimiento sancionatorio.

## Título IV (Reemplazado): Del tratamiento de datos personales por los órganos públicos

### Artículo 20: Regla general del tratamiento de datos por órganos públicos

ID: LEY-21719-ART20-01

- Cpt: Es lícito el tratamiento de datos por órganos públicos sin el consentimiento del titular.
- Cond: Debe realizarse para el cumplimiento de sus funciones legales, dentro de sus competencias y de conformidad a la ley y este Título.
- Ctx: En estas condiciones, los órganos públicos actúan como responsables de datos.

### Artículo 21: Principios y normas aplicables

ID: LEY-21719-ART21-01

- Fnd: El tratamiento se rige por los principios del Art. 3 y los principios de la Administración del Estado (coordinación, probidad, eficiencia).
- Cpt: Principio de coordinación.
  - Purp: Alcanzar alto grado de interoperabilidad para evitar contradicciones y reiteración de requerimientos de información a los titulares.
- Cpt: Principio de eficiencia.
  - Purp: Evitar la duplicación de procedimientos y trámites.
- Ctx: Se listan los artículos de la ley que son aplicables a los órganos públicos.

### Artículo 22: Comunicación o cesión de datos por un órgano público

ID: LEY-21719-ART22-01

- Cpt: Comunicación entre órganos públicos.
  - Cond: Están facultados para comunicar o ceder datos a otros órganos públicos si es necesario para el cumplimiento de sus funciones legales y ambos actúan dentro de sus competencias.
  - Req: La comunicación debe ser para un tratamiento específico; el receptor no puede usarlos para otros fines.
  - Cond: También se permite para otorgar beneficios al titular o evitar duplicidad de trámites.
- Cpt: Comunicación a entidades privadas.
  - Req: Se debe contar con el consentimiento del titular.
  - Cpt: Excepción.
    - Cond: Salvo que la comunicación sea necesaria para cumplir funciones de fiscalización o inspección.

## Artículos Segundo y Tercero (Permanentes)

### Artículo Segundo: Modificación Ley N° 20.285

ID: LEY-21719-ART-SEGUNDO-01

- Act: Suprímese el literal m) del artículo 33 del artículo primero de la ley N° 20.285 (Ley de Transparencia).

### Artículo Tercero: Modificación Ley N° 19.496

ID: LEY-21719-ART-TERCERO-01

- Act: Suprímese el artículo 15 bis de la ley N° 19.496 (Ley de Protección de los Derechos de los Consumidores).

## Disposiciones Transitorias

### Artículo Primero Transitorio: Entrada en vigencia

ID: LEY-21719-TRANS-ART01-01

- Dln: Las modificaciones a las leyes N° 19.628, N° 20.285 y N° 19.496 entrarán en vigencia el primer día del mes 24 posterior a la publicación de esta ley.

### Artículo Segundo Transitorio: Dictación de reglamentos

ID: LEY-21719-TRANS-ART02-01

- Dln: Los reglamentos referidos en la ley deberán dictarse dentro de los 6 meses siguientes a la publicación.

### Artículo Tercero Transitorio: Eliminación de registro de bancos de datos

ID: LEY-21719-TRANS-ART03-01

- Act: El Servicio de Registro Civil e Identificación deberá eliminar el registro de bancos de datos personales.
- Dln: Dentro de los 60 días anteriores a la entrada en vigencia de las modificaciones a la ley N° 19.628.

### Artículo Cuarto Transitorio: Designación del Consejo de la Agencia

ID: LEY-21719-TRANS-ART04-01

- Proc: La primera designación de consejeros de la Agencia se hará dentro de los 60 días anteriores a la entrada en vigencia.
- Cpt: La primera propuesta al Senado especificará la duración escalonada de los cargos (2, 4 y 6 años).

### Artículo Quinto Transitorio: Designación de encargados de prevención

ID: LEY-21719-TRANS-ART05-01

- Req: Los órganos públicos que establezcan un encargado de prevención deberán designar a un funcionario de la dotación vigente.

### Artículo Sexto Transitorio: Régimen sancionatorio para empresas de menor tamaño

ID: LEY-21719-TRANS-ART06-01

- Cond: Durante los primeros 12 meses de vigencia, la Agencia podrá aplicar solo una amonestación por escrito como sanción a empresas de menor tamaño.

### Artículo Séptimo Transitorio: Dictación de políticas internas

ID: LEY-21719-TRANS-ART07-01

- Dln: Las instituciones del artículo 54 deberán dictar sus políticas internas dentro de los 18 meses siguientes a la publicación de la ley.

### Artículo Octavo Transitorio: Financiamiento

ID: LEY-21719-TRANS-ART08-01

- Cpt: El mayor gasto fiscal del primer año se financiará con recursos del Ministerio de Economía o del Tesoro Público.
