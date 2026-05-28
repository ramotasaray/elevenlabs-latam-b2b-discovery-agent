#!/usr/bin/env python3
"""
Provision María — the ElevenLabs LATAM B2B Discovery Agent.

Reads the system prompt from agent/system-prompt.md, uploads the 4 knowledge
base documents in agent/knowledge-base/, then creates the agent and prints
the agent_id. Paste that agent_id into landing/index.html where it says
AGENT_ID_PLACEHOLDER.

Idempotent: re-running uploads new versions of the KB docs (ElevenLabs assigns
new doc IDs each time, by design). The agent is recreated each run; if you
want to preserve a specific agent_id, edit this script to call the update
endpoint instead.

Usage:
    pip install -r requirements.txt
    cp .env.example .env  # fill in ELEVENLABS_API_KEY
    python agent/provision.py

Environment:
    ELEVENLABS_API_KEY  required, from your ElevenLabs dashboard
    AGENT_VOICE_ID      optional, default picks a Spanish neutral voice
    AGENT_MODEL_ID      optional, default eleven_flash_v2_5 for low latency
    AGENT_LLM           optional, default gemini-2.0-flash (cheap + fast)
"""

import os
import sys
import json
from pathlib import Path

try:
    import requests
    from dotenv import load_dotenv
except ImportError:
    print("Missing deps. Run: pip install -r requirements.txt")
    sys.exit(1)


# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

ROOT = Path(__file__).resolve().parent.parent
SYSTEM_PROMPT_PATH = ROOT / "agent" / "system-prompt.md"
KB_DIR = ROOT / "agent" / "knowledge-base"

API_BASE = "https://api.elevenlabs.io"

# Default voice: a Spanish-friendly multilingual voice from the public library.
# To use a different voice, set AGENT_VOICE_ID env var or change here.
# Many users pick "Sarah" (voice_id: EXAVITQu4vr4xnSDxMaL) which is multilingual.
DEFAULT_VOICE_ID = "EXAVITQu4vr4xnSDxMaL"  # Sarah — multilingual library voice
DEFAULT_MODEL_ID = "eleven_flash_v2_5"      # low-latency for conversation
DEFAULT_LLM = "gemini-2.0-flash"            # cheap + fast LLM for the agent


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _api_key() -> str:
    key = os.environ.get("ELEVENLABS_API_KEY")
    if not key:
        print("ERROR: ELEVENLABS_API_KEY not set. See .env.example.")
        sys.exit(1)
    return key


def _headers(json_body: bool = False) -> dict:
    h = {"xi-api-key": _api_key()}
    if json_body:
        h["Content-Type"] = "application/json"
    return h


def upload_kb_document(file_path: Path, name: str) -> str:
    """Upload one KB file. Returns the document ID."""
    url = f"{API_BASE}/v1/convai/knowledge-base/file"
    with open(file_path, "rb") as f:
        files = {"file": (file_path.name, f, "text/markdown")}
        data = {"name": name}
        resp = requests.post(url, headers=_headers(), files=files, data=data)
    if not resp.ok:
        print(f"FAILED to upload {file_path.name}: {resp.status_code} {resp.text}")
        sys.exit(1)
    body = resp.json()
    doc_id = body.get("id") or body.get("document_id")
    print(f"  ✓ Uploaded {file_path.name} → {doc_id}")
    return doc_id


def create_agent(system_prompt: str, kb_doc_ids: list[str]) -> str:
    """Create the agent with system prompt + linked KB documents."""
    url = f"{API_BASE}/v1/convai/agents/create"

    voice_id = os.environ.get("AGENT_VOICE_ID", DEFAULT_VOICE_ID)
    model_id = os.environ.get("AGENT_MODEL_ID", DEFAULT_MODEL_ID)
    llm = os.environ.get("AGENT_LLM", DEFAULT_LLM)

    knowledge_base = [
        {"type": "file", "id": doc_id, "name": f"kb_{i+1}"}
        for i, doc_id in enumerate(kb_doc_ids)
    ]

    first_message = (
        "Antes de empezar, soy un demo construido por Daniel Ramírez como "
        "prueba de trabajo para su aplicación al puesto de B2B Marketing "
        "Spanish-LATAM Growth Lead en ElevenLabs. Para una demo oficial con "
        "el equipo, los datos están al pie de la página. Dicho esto, "
        "¿en qué le ayudo?"
    )

    payload = {
        "name": "María — ElevenLabs LATAM B2B Discovery Agent",
        "tags": ["latam", "spanish", "b2b", "discovery", "candidate-demo"],
        "conversation_config": {
            "agent": {
                "prompt": {
                    "prompt": system_prompt,
                    "llm": llm,
                    "knowledge_base": knowledge_base,
                },
                "first_message": first_message,
                "language": "es",
            },
            "tts": {
                "voice_id": voice_id,
                "model_id": model_id,
            },
            "asr": {
                "quality": "high",
                "provider": "elevenlabs",
                "user_input_audio_format": "pcm_16000",
            },
        },
        "platform_settings": {
            "widget": {
                "action_text": "¿Conversamos?",
                "start_call_text": "Iniciar llamada",
                "end_call_text": "Finalizar llamada",
                "expand_text": "Abrir chat",
                "listening_text": "Escuchando...",
                "speaking_text": "María hablando...",
                "language_selector": False,
            },
        },
    }

    resp = requests.post(url, headers=_headers(json_body=True), json=payload)
    if not resp.ok:
        print(f"FAILED to create agent: {resp.status_code}")
        print(resp.text)
        sys.exit(1)
    agent_id = resp.json().get("agent_id")
    return agent_id


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    load_dotenv()
    _api_key()  # validate

    print("Reading system prompt...")
    system_prompt = SYSTEM_PROMPT_PATH.read_text(encoding="utf-8")

    print("\nUploading knowledge base documents...")
    kb_doc_ids = []
    for kb_file in sorted(KB_DIR.glob("*.md")):
        name = kb_file.stem  # e.g. "01-elevenagents-b2b"
        doc_id = upload_kb_document(kb_file, name)
        kb_doc_ids.append(doc_id)

    print(f"\nUploaded {len(kb_doc_ids)} documents. Creating agent...")
    agent_id = create_agent(system_prompt, kb_doc_ids)

    print()
    print("=" * 70)
    print(f"  AGENT CREATED")
    print(f"  agent_id: {agent_id}")
    print("=" * 70)
    print()
    print("Next steps:")
    print(f"  1. Open landing/index.html")
    print(f"  2. Replace AGENT_ID_PLACEHOLDER with: {agent_id}")
    print(f"  3. Test locally: python -m http.server 8000 --directory landing")
    print(f"  4. Deploy to Vercel: cd landing && vercel --prod")
    print()


if __name__ == "__main__":
    main()
