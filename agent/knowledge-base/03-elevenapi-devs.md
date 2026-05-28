# ElevenAPI — Use Cases para Equipos Técnicos LATAM

ElevenAPI da acceso a los modelos foundational de audio de ElevenLabs a desarrolladores. Es la opción para equipos técnicos que quieren integrar voz a su propio producto.

## SDKs oficiales

- **Python**: `pip install elevenlabs`
- **Node.js**: `npm install @elevenlabs/elevenlabs-js`
- HTTP/Websocket directo desde cualquier lenguaje

## Endpoints principales

### Text-to-Speech (`/v1/text-to-speech`)

Convierte texto en audio. Soporta:
- Selección de voice ID (5k+ voces)
- Selección de modelo (v3, multilingual v2, Flash v2.5)
- Voice settings: stability, similarity boost
- Streaming para latencia ultra-baja
- Raw response con headers para tracking de costos (character count, request ID)

### Speech-to-Text (`/v1/speech-to-text`)

Transcripción con timestamps, speaker diarization opcional.

### Voice Library / Voice Cloning

- Acceder a biblioteca pública
- Instant voice cloning desde 30+ segundos de audio
- Professional voice cloning para fidelidad máxima

### Dubbing API

Dubbing automatizado de video/audio entre idiomas.

### Sound Effects + Music

Generación de SFX y música desde prompts.

## Use cases B2B LATAM por vertical

### Fintech mexicana

- Voz de confirmación de transacción en app
- Voicebot para soporte cuentas
- Notificaciones de seguridad por voz (más fricción que SMS = menos phishing)
- Onboarding KYC narrado

### Edtech LATAM

- Audiobooks de contenido textual
- Narración para cursos
- Tutores conversacionales (combinado con ElevenAgents)
- Localización de contenido en 31+ idiomas

### Healthcare / Telesalud

- Recordatorios de medicación con voz natural (mejor adherencia que beep)
- Triage conversacional pre-consulta
- Educación al paciente post-consulta

### Retail / Ecommerce

- Descripciones de producto en audio para PDPs
- Asistentes voice-first para apps móviles
- Audio reviews generados desde texto

### Telco / ISP

- IVRs naturales vs robóticos
- Soporte 24/7 voice-first
- Encuestas NPS conversacionales

## Latency optimization

Para conversación real-time, usar Flash v2/v2.5:
- Latency sub-segundo
- 50% lower price per character
- 32 idiomas

## Streaming

Endpoints de streaming permiten:
- Audio que llega chunk-by-chunk mientras se genera
- Reduce time-to-first-byte significativamente
- Ideal para chat voice o conversación

## Tracking de costos

Headers de raw response:
- `x-character-count`: cuántos chars se usaron
- `request-id`: para correlación con logs

Permite alertas de gasto, attribution por feature, y optimización fina.

## Pricing model API

- **Free**: 10k credits/mes
- **Starter $6**: 30k credits
- **Creator $22**: 121k credits
- **Pro $99**: 600k credits
- **Scale $299**: 1.8M credits
- **Business $990**: 6M credits + low-latency TTS desde 5c/min
- **Enterprise**: custom

## Authentication + security

- API key based
- Rate limiting por plan
- Webhooks para eventos
- Audit logs en planes Enterprise

## Setup developer realista

- Primer "hello world" TTS: 5 minutos
- Integración production con error handling, retry, costos tracking: 1-3 días
- Voice agent custom completo via ElevenAgents API: 1-3 semanas
- Producción enterprise con monitoreo, observability, SLOs: 1-3 meses

## Startup Grants Program

ElevenLabs ofrece grant de 12 meses gratis con 33M characters para startups en early stage construyendo agentes conversacionales. Aplicable para startups LATAM que califiquen.
