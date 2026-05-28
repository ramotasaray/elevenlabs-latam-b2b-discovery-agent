#!/usr/bin/env python3
"""
Generate the bonus outbound MP3 sample using the ElevenLabs TTS API.

Output: samples/01_outbound_mexico_fintech_cmo.mp3
Script source: hardcoded below (also documented in samples/outbound-script.md)

Usage:
    pip install -r requirements.txt
    cp .env.example .env  # fill in ELEVENLABS_API_KEY
    python samples/generate.py
"""

import os
import sys
from pathlib import Path

try:
    import requests
    from dotenv import load_dotenv
except ImportError:
    print("Missing deps. Run: pip install -r requirements.txt")
    sys.exit(1)


SCRIPT_MX_FINTECH = (
    "Hola María Fernanda, le habla Amanda, de ElevenLabs. "
    "Vi que Pago Veloz está escalando su volumen de transacciones, "
    "y normalmente, lo que viene es presión sobre el equipo de soporte. "
    "Construimos ElevenAgents, una plataforma de agentes conversacionales "
    "con voz humana en español mexicano, que atiende el primer nivel de soporte "
    "sin agente humano. "
    "Empresas como Meta ya la usan en producción. "
    "¿Tiene quince minutos esta semana, para revisar qué resolvería en su contexto? "
    "Le mando tres horarios por correo."
)

# Default voice: Sarah (multilingual). Set AGENT_VOICE_ID env var to override.
DEFAULT_VOICE_ID = "EXAVITQu4vr4xnSDxMaL"
DEFAULT_MODEL = "eleven_multilingual_v2"

OUTPUT_PATH = Path(__file__).resolve().parent / "01_outbound_mexico_fintech_cmo.mp3"


def main() -> None:
    load_dotenv()
    api_key = os.environ.get("ELEVENLABS_API_KEY")
    if not api_key:
        print("ERROR: ELEVENLABS_API_KEY not set.")
        sys.exit(1)

    voice_id = os.environ.get("AGENT_VOICE_ID", DEFAULT_VOICE_ID)
    model_id = os.environ.get("TTS_MODEL_ID", DEFAULT_MODEL)

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {
        "xi-api-key": api_key,
        "Content-Type": "application/json",
        "Accept": "audio/mpeg",
    }
    payload = {
        "text": SCRIPT_MX_FINTECH,
        "model_id": model_id,
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.75,
            "style": 0.2,
            "use_speaker_boost": True,
        },
    }

    print(f"Generating MP3 with voice_id={voice_id}, model={model_id}...")
    resp = requests.post(url, headers=headers, json=payload)

    if not resp.ok:
        print(f"FAILED: {resp.status_code}")
        print(resp.text)
        sys.exit(1)

    OUTPUT_PATH.write_bytes(resp.content)

    char_count = resp.headers.get("x-character-count", "?")
    request_id = resp.headers.get("request-id", "?")
    file_size_kb = len(resp.content) / 1024

    print(f"  ✓ Wrote {OUTPUT_PATH.name} ({file_size_kb:.1f} KB)")
    print(f"  ✓ Characters consumed: {char_count}")
    print(f"  ✓ Request ID: {request_id}")


if __name__ == "__main__":
    main()
