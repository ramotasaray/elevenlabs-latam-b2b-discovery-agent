# Manejo de Objeciones LATAM B2B

Respuestas grounded para las objeciones más comunes que aparecen en discovery calls con prospects empresariales en México, Argentina, Colombia, Perú y Chile.

## Objeción 1: "¿Hay soporte en español?"

**Respuesta corta**: Sí.

**Detalle**: ElevenLabs ofrece:
- Documentación oficial con traducciones progresivas
- Equipo de soporte que atiende en español
- Comunidad activa de usuarios hispanohablantes
- Recursos de aprendizaje en español

**Si insisten en SLA de soporte en español**: planes Business/Enterprise permiten SLA contractual en idioma específico. El equipo comercial lo confirma.

## Objeción 2: "¿Facturan a entidad local? ¿Aceptan pesos mexicanos / pesos argentinos / pesos colombianos?"

**Respuesta corta**: Variable según plan y país.

**Detalle**:
- Planes self-serve (Free, Starter, Creator, Pro) se cobran en USD vía tarjeta o métodos digitales globales
- Planes Enterprise pueden estructurarse con facturación a entidad local del cliente, contratos en moneda local, términos de pago extendidos (NET30, NET60), y procesos de procurement formal
- Para empresas mexicanas grandes con requirements de CFDI / SAT, el equipo Enterprise tiene la conversación

**Routing**: si la objeción es real (no nice-to-have), agendar con equipo Enterprise directamente.

## Objeción 3: "¿Los modelos suenan natural en español mexicano / argentino / colombiano?"

**Respuesta corta**: Sí, en mayoría de casos.

**Detalle**:
- Modelos multilingual v2 y v3 incluyen Spanish (España) y Spanish (México) como acentos nativos
- Para acentos rioplatense (AR), colombiano, peruano, chileno: voces de la biblioteca con esos acentos disponibles
- Para máxima fidelidad de acento específico: voice cloning de un talento local (instant o professional)
- Demo en vivo: ofrece generar un sample con el texto que ellos elijan en ese momento

**Tip de discovery**: pedirles ejemplos de uso real. Voicemail vs IVR vs podcast tienen tolerancias diferentes a "acento perfecto".

## Objeción 4: "¿Es seguro para datos sensibles? ¿Cumple con regulaciones locales (LGPD Brasil, LFPDPPP México)?"

**Respuesta corta**: Sí, con caveats por plan.

**Detalle**:
- SOC 2 Type II compliance
- GDPR-compliant (aplicable a clientes con datos europeos)
- Zero data retention disponible en planes Enterprise (audio + transcripts no se almacenan)
- Para LGPD Brasil, LFPDPPP México: revisar con equipo legal de ElevenLabs el contrato Enterprise específico
- Encriptación en tránsito y en reposo

**Si la objeción es regulatoria seria**: rutear a equipo Enterprise / Commercial Counsel LATAM.

## Objeción 5: "¿Cuál es la latencia? Necesitamos tiempo real."

**Respuesta corta**: Sub-segundo con modelos Flash.

**Detalle**:
- Eleven Flash v2.5: latencia muy baja, optimizado para conversación
- Streaming endpoints reducen time-to-first-byte
- Para deployment LATAM: la latencia depende de la región de servidor; el equipo de infra puede confirmar región óptima

**Demo en vivo**: cualquier interacción con este mismo agente es prueba de latencia real (~500ms-1s).

## Objeción 6: "¿Se integra con [HubSpot / Salesforce / Zoho / Pipedrive / etc.]?"

**Respuesta corta**: Sí, vía API + tools framework de ElevenAgents.

**Detalle**:
- ElevenAgents permite "tools" que invocan APIs externos durante conversación
- Integraciones nativas con Twilio + SIP trunk para telefonía
- Para CRMs específicos: integración custom vía webhooks + API del CRM
- ElevenLabs UI library (basada en shadcn) acelera frontend

**Si tienen stack específico que no conoces**: "El equipo técnico puede confirmar tiempo de integración real. ¿Le paso un AE técnico?"

## Objeción 7: "¿Cuánto cuesta esto realmente? Las páginas de pricing tienen muchas variables."

**Respuesta corta**: Free tier para probar; planes desde $6/mes; Enterprise se cotiza por volumen.

**Detalle**:
- Free tier completo para validar fit antes de pagar
- Planes self-serve cubren la mayoría de SMBs y mid-market
- Enterprise se cotiza por minutos/credits/concurrency
- Cost optimization disponible: mezclar modelos (Flash para volume, v3 para premium), prompt engineering, caching

**No cotices número específico**. Rutea: "Para números reales le agendo 20 min con el equipo comercial. ¿Le va esta semana?"

## Objeción 8: "¿Quién más en mi industria / país usa esto?"

**Respuesta corta**: Referencias enterprise globales públicas, LATAM por NDA.

**Detalle**:
- Referencias públicas: Deutsche Telekom, Meta
- LATAM enterprise: referencias bajo NDA, el equipo comercial las comparte en conversación seria
- Categoría: empresas líderes en su vertical están adoptando voice AI en 2025-2026; quien no lo haga queda atrás en CX

**Tip**: la objeción "nadie en mi país lo usa" muchas veces esconde "no quiero ser el primero en explicar esto a mi equipo". Manejar con: "El value es ser de los primeros. Le agendo un piloto de 30 días para que tenga el case study interno antes que su competencia."

## Objeción 9: "Nuestro equipo no está listo para esto / no tenemos developers."

**Respuesta corta**: ElevenAgents tiene no-code builder. ElevenCreative no requiere developers.

**Detalle**:
- Visual workflow builder en dashboard
- Widget embed = 1 línea de código (un dev junior lo hace)
- Para deployment sin developers: ElevenLabs tiene partner program con systems integrators que despliegan llave-en-mano

**Si están realmente sin equipo técnico**: "Le conecto con un partner integrador en México que cierra el despliegue."

## Objeción 10: "Ya tenemos un IVR / chatbot. ¿Por qué cambiar?"

**Respuesta corta**: La voz humana convierte mejor que IVR o chatbot de texto.

**Detalle**:
- IVRs robóticos tienen NPS bajo histórico; clientes piden agente humano en 60%+ de los casos
- Chatbots de texto pierden en problemas complejos donde el cliente necesita explicar
- Voice AI natural mantiene el feeling de "agente humano" sin el costo de un human team 24/7
- Casos donde IVR sigue ganando: transacciones simples 100% rutinarias (saldo, último corte). Para todo lo demás, voice AI conversacional gana

**Convertir**: "¿Cuánto les cuesta su deflection actual? ¿Qué % de calls terminan en humano de todos modos? Eso es el ROI directo."

## Cierre estándar

Después de manejar 1-2 objeciones, ofrecer compromiso pequeño:

1. **Demo con equipo comercial**: "¿Le agendo 20 minutos con el equipo comercial de [Mexico/Argentina/etc.]?"
2. **Materiales por email**: "Le mando un caso de uso de su vertical + acceso al sandbox."
3. **Piloto de 30 días**: "Si está serio en evaluar, le proponemos un piloto de 30 días con KPI acordado upfront."

No empujar más allá. Si la persona no califica o no está lista, agradecer y cerrar.
