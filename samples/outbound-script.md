# Outbound MP3 Sample — Script & Prompt Engineering Notes

## Use case

A Mexican fintech CMO (synthetic persona, María Fernanda López, CMO of "Pago Veloz" — fictional Mexican B2B payments fintech) receives this 30-second audio attachment in a cold outbound email. The premise: ElevenLabs' Spanish-LATAM Growth Lead is opening dialogue with mid-market Mexican fintech CMOs about ElevenAgents.

## The script (Spanish Mexico, ~30 seconds)

> "Hola María Fernanda, le habla Amanda, de ElevenLabs. Vi que Pago Veloz está escalando su volumen de transacciones, y normalmente, lo que viene es presión sobre el equipo de soporte. Construimos ElevenAgents, una plataforma de agentes conversacionales con voz humana en español mexicano, que atiende el primer nivel de soporte sin agente humano. Empresas como Meta ya la usan en producción. ¿Tiene quince minutos esta semana, para revisar qué resolvería en su contexto? Le mando tres horarios por correo."

## Why Amanda for outbound and María for inbound

Two personas, two roles. Amanda is the SDR persona on cold outbound (audio attachments, voicemail drops, ABM sequences). María is the inbound discovery agent on the landing page. This mirrors how real B2B teams structure their motion: outbound and inbound are different muscles, often different people. Both use the same product stack (ElevenLabs API for outbound audio, ElevenAgents for inbound conversation), which is the point.

## Prompt engineering decisions

**Why personalized opener with first name + company**: outbound LATAM B2B is saturated with generic mass templates. Specific opener is the only way to get past the first 5 seconds.

**Why lead with their pain, not the product**: classic Hormozi value-equation opener. State the dream outcome and the gap; the product is the bridge, not the headline.

**Why only Meta as the reference**: third-party social proof condensed to one strong anchor. Tested originally with "Deutsche Telekom y Meta"; the TTS pronunciation of "Deutsche Telekom" sounded foreign and broke the flow. One clean reference reads more naturally than two with one broken.

**Why "sin agente humano" instead of "24/7"**: TTS reads "24/7" as separated numerals which sounded off. "Sin agente humano" carries the same meaning ("no human in the loop") and flows naturally in Spanish.

**Why "¿tiene quince minutos esta semana?"**: small commitment, time-boxed. Compresses time-to-decision.

**Why "le mando tres horarios por correo"**: removes friction. The CMO doesn't have to schedule; they just pick from three options.

**Length**: ~30 seconds. Long enough to deliver value, short enough that the CMO doesn't tune out.

## Audio generation (via TTS API)

The script is fed to ElevenLabs TTS via the API in `samples/generate.py`. Parameters:

- **Voice**: Spanish library voice with neutral Mexican accent
- **Model**: `eleven_multilingual_v2` (or `eleven_v3` if available on plan) for expressive Spanish
- **Stability**: 0.5 (balance between consistency and natural variation)
- **Similarity boost**: 0.75 (close to source voice character)
- **Output format**: `mp3_44100_128` (standard quality, small file)

## How this would integrate into a real outbound sequence

This MP3 is one node in a multi-touch ABM sequence. The full sequence (production version):

1. **Day 0**: LinkedIn warm view + connect request with personalized note
2. **Day 2**: First cold email with this MP3 attached, subject line referencing prospect's company news
3. **Day 5**: LinkedIn DM following up on the email
4. **Day 8**: Second email with a relevant case study (the ElevenLabs MX dental clinic case, if it existed)
5. **Day 12**: Voicemail drop using ElevenAgents batch outbound (same voice, different script)
6. **Day 20**: Break in sequence, re-engage at month 2 if no response

The MP3 is the differentiator in steps 2 and 5. Most outbound is text-only; audio attachments measurably increase open and reply rates in saturated channels.

## How to regenerate

```bash
cp .env.example .env  # add ELEVENLABS_API_KEY
python samples/generate.py
```

This will regenerate `01_outbound_mexico_fintech_cmo.mp3` using current voice + model settings.

## Extending to other countries

Same script template, swap voice + minor vocabulary adjustments:

- **Argentina**: voice with Buenos Aires accent, use "vos hablás" instead of "usted habla", reference local context ("MercadoLibre, Globant ya están usándola")
- **Colombia**: voice with neutral Colombian accent, formal "usted", reference local ("Bancolombia, Rappi en la región")
- **Peru**: voice with Lima neutral accent, formal "usted", reference local enterprise context

`samples/generate.py` can be parameterized with `--country` flag to generate variants. For this proof-of-work I shipped the Mexico variant only; the script generalizes trivially.
