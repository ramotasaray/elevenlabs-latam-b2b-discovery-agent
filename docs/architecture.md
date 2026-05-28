# Architecture

## Overview

Three components, each running in different infrastructure, connected by the agent ID and the API key.

```
┌──────────────────────────────────────────────────────────────────┐
│  1. Static landing page  (Vercel CDN, free tier)                 │
│     - HTML + Tailwind CDN + custom CSS                           │
│     - Loads ElevenLabs widget script                             │
│     - Mounts <elevenlabs-convai agent-id="..."> in body          │
└──────────────────────────────────────────────────────────────────┘
                          │
                          │ (visitor's browser establishes WebSocket
                          │  to ElevenLabs infra on agent activation)
                          ▼
┌──────────────────────────────────────────────────────────────────┐
│  2. ElevenAgents runtime  (ElevenLabs managed infra)             │
│     - ASR (speech recognition, fine-tuned)                       │
│     - LLM (GPT-4o or selected model)                             │
│     - Turn-taking proprietary model                              │
│     - TTS (Spanish MX voice from library)                        │
│     - RAG over uploaded knowledge base                           │
└──────────────────────────────────────────────────────────────────┘
                          │
                          │ (knowledge base + system prompt loaded
                          │  on agent provisioning)
                          ▼
┌──────────────────────────────────────────────────────────────────┐
│  3. Knowledge base + system prompt  (uploaded once via API)      │
│     - 4 markdown docs in agent/knowledge-base/                   │
│     - system-prompt.md as the agent's prompt                     │
│     - Stored in ElevenLabs and indexed for RAG                   │
└──────────────────────────────────────────────────────────────────┘
```

Separately, the bonus MP3:

```
┌──────────────────────────────────────────────────────────────────┐
│  Bonus outbound: samples/01_outbound_mexico_fintech_cmo.mp3      │
│                                                                  │
│  samples/generate.py  →  ElevenLabs TTS API  →  MP3 file         │
│       (with Spanish MX voice, the persuasive cold outbound)      │
└──────────────────────────────────────────────────────────────────┘
```

## Why this architecture (vs alternatives)

**Why static frontend, not a Next.js / React app?**
The landing page is content + a widget. A full framework adds build complexity for no functional gain. One HTML file deploys in 30 seconds and loads instantly.

**Why widget embed, not a custom WebSocket client?**
ElevenLabs provides the `<elevenlabs-convai>` web component. It handles WebSocket negotiation, audio I/O, UI, and reconnection. Building a custom client would 5x the development time for no user-facing benefit at this scope.

**Why the agent runs on ElevenLabs infra, not self-hosted?**
ElevenAgents includes ASR, LLM, TTS, and turn-taking as a managed service. Self-hosting would require recreating their proprietary turn-taking model (not feasible) plus running expensive GPUs (not necessary for a demo).

**Why provision the agent via API, not the dashboard?**
The Python script in `agent/provision.py` makes the build reproducible. Someone reviewing the repo can run the script and recreate the exact agent. The dashboard is faster for one-off setup but not reproducible.

## Data flow during a conversation

1. Visitor clicks the page → widget script auto-loads
2. Visitor clicks the widget mic icon → browser asks for mic permission
3. Audio stream from visitor → WebSocket → ElevenLabs ASR
4. ASR transcript → LLM (with system prompt + RAG context from KB)
5. LLM response text → TTS (María's voice)
6. TTS audio stream → WebSocket → visitor's browser → plays in widget
7. Turn-taking model decides when visitor should speak again
8. Loop until conversation ends

Conversation transcript and audio are stored in ElevenLabs dashboard (configurable retention).

## Costs in this architecture

Per the May 2026 ElevenLabs pricing:

- **Free tier**: 15 minutes of agent calls per month, includes widget
- **Starter $6/mo**: 75 minutes of agent calls, includes widget
- **Vercel free tier**: unlimited static hosting for personal projects
- **Knowledge base storage**: included in plan
- **TTS for bonus MP3**: free tier covers ~10 minutes of audio; this build uses ~30 seconds

For the demo / review window, total cost is $0-6 depending on plan.

## Security and disclaimers

- API key stored in `.env`, never committed (see `.gitignore`)
- Visitor audio is processed by ElevenLabs per their terms; no third-party processing
- The agent identifies itself as a candidate's proof-of-work in turn 1 (mandatory in system prompt)
- The landing page footer carries the same disclaimer
- The agent does not collect emails or write to any external system; it only routes to the real ElevenLabs team if visitor wants a real demo

## Reproducibility

The entire build is reproducible end-to-end:

```bash
git clone <repo>
cd <repo>
pip install -r requirements.txt
cp .env.example .env
# add ELEVENLABS_API_KEY to .env
python agent/provision.py    # creates agent, uploads KB
# copy the agent ID from the script output into landing/index.html
python samples/generate.py   # optional, regenerates bonus MP3
cd landing
vercel --prod                # or open index.html directly
```

No private data, no custom infrastructure, no proprietary dependencies.
