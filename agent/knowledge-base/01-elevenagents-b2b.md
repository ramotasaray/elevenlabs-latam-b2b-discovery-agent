# ElevenAgents — Use Cases B2B para LATAM

ElevenAgents es la plataforma de agentes conversacionales de voz de ElevenLabs. Está diseñada para empresas que necesitan automatizar interacciones de customer experience a escala con voz humana natural, en 31+ idiomas incluyendo español (México, España, neutro).

## Componentes core

ElevenAgents coordina 4 componentes:

1. **Speech-to-Text (ASR)** fine-tuneado para reconocimiento preciso
2. **LLM** a elección: modelos soportados de terceros o LLM custom propio
3. **Text-to-Speech** de baja latencia con 5k+ voces en 70+ idiomas
4. **Modelo propietario de turn-taking** que maneja timing de conversación natural

## Capacidades de configuración

- **Workflows visuales**: builder de flujos multi-paso para conversaciones complejas
- **System prompts**: para definir personalidad, alcance, reglas
- **Knowledge base + RAG**: subir documentos para respuestas grounded sin alucinaciones
- **Tools**: agentes pueden invocar APIs externos (consultar CRM, crear ticket, agendar)
- **Personalization**: variables dinámicas por conversación para context per-user
- **Authentication**: protección de agentes con auth custom

## Deployment

- **Widget embed en website**: línea de código para cualquier sitio (como el de este demo)
- **React, Swift, Kotlin, React Native SDKs**: apps nativas y cross-platform
- **SIP trunk + Twilio integration**: telefonía empresarial
- **Batch outbound calls**: llamadas salientes programáticas a escala
- **WebSocket API**: protocolo low-level para integraciones custom

## Use cases B2B clásicos para LATAM

### Customer support automation

Atender 60-80% de interacciones inbound en primer nivel sin agente humano. Liberar equipo para casos complejos.

Verticales típicos en LATAM:
- Fintech (qualification, soporte cuentas, FAQs)
- Telco (soporte plan, recargas, troubleshooting)
- Retail / ecommerce (estado pedido, devoluciones, recomendación producto)
- Healthcare privado (agendamiento citas, recordatorios, triage)
- Servicios financieros (account info, transacciones, alertas)

### Inbound qualification

Filtrar leads en primer touch. El agente hace 3-5 preguntas, califica, y o agenda demo con sales humano, o desestima si no califica.

Ejemplo: empresa SaaS B2B con tráfico inbound desordenado → agente filtra por tamaño de empresa, vertical, presupuesto, urgencia, y solo agenda los calificados con SDR.

### Outbound calling at scale

Batch calls programáticos para:
- Recordatorios de cita / pago
- Follow-up post-compra
- Encuestas NPS conversacionales
- Reactivación de cuentas dormidas

### Multi-language support

Mismo agente atendiendo en español MX, español AR, portugués Brasil, inglés. Cambio de idioma mid-conversación si el usuario lo necesita.

## Ventajas competitivas vs alternativas (IVR legacy, otros voice AI)

- **Voz natural humana** vs IVRs robóticos
- **31+ idiomas** vs voice AI competidores típicamente 5-10 idiomas
- **Latencia sub-segundo** con modelos Flash
- **Interrupciones humanas naturales** (el usuario puede interrumpir, el agente reacciona)
- **No hay tono robótico característico** que delate "soy IA"

## Referencias enterprise verificadas

- **Deutsche Telekom**: deployment voice AI a gran escala
- **Meta**: clientes enterprise
- ElevenLabs sirve millones de usuarios y miles de empresas globalmente

(Para referencias LATAM específicas por vertical, contactar al equipo comercial bajo NDA.)

## Pricing model resumido

- **Free tier**: 15 minutos de calls/mes + widget incluido
- **Starter**: 75 min calls
- **Creator**: 275 min calls + voice cloning profesional
- **Pro / Scale / Business / Enterprise**: hasta 12k+ min calls, custom pricing

LLM cost se deduce de credits del workspace cuando se usan modelos soportados; con custom LLM, sin costo adicional de ElevenLabs.

**Burst pricing** permite exceder concurrency de forma temporal con cargo 2x.

## Setup time real

- **Free tier setup → primer agente live en widget**: 5-15 minutos
- **Agente production-ready con KB + tools + auth**: 1-3 semanas
- **Migración completa desde IVR legacy + integración con CRM**: 1-3 meses
