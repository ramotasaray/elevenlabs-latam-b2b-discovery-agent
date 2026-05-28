# ElevenLabs LATAM B2B Discovery Agent

> A live conversational agent (María, an ElevenLabs LATAM commercial assistant) built with ElevenAgents + a bonus outbound MP3 generated via ElevenAPI. Constructed as proof-of-work for an application to the **B2B Marketing Spanish-LATAM Growth Lead** role at ElevenLabs, May 2026.

**Live demo**: https://elevenlabs-latam-demo.vercel.app *(to be deployed)*

**Author**: Daniel Ramírez · [linkedin.com/in/ramo5](https://linkedin.com/in/ramo5) · daniel.ramirez.crc@gmail.com

---

## What this is

A working demonstration of what a Spanish-LATAM B2B inbound qualification motion would look like if ElevenLabs ran it with its own product:

1. A prospect lands on a Spanish landing page
2. Talks (literally, by voice) with **María**, an agent built with ElevenAgents
3. María identifies their use case, maps it to the correct ElevenLabs product (Agents / Creative / API), manages 1-2 LATAM-typical objections, and offers a small commitment (book real demo with the team or send materials by email)

Plus a 30-second outbound voicemail-style MP3 sample generated via the TTS API, demonstrating the same product's capability for the OUTBOUND side of the funnel.

## Why this deliverable

The role description (publicly visible at elevenlabs.io/careers) calls for someone who:

- Builds "complex, multi-language outbound sequences that cut through the noise"
- Owns LATAM B2B from zero-to-one as the local DRI
- Adapts ElevenLabs' global voice to LATAM business cultures
- Acts as a "Jack of All Trades" across growth marketing, with bonus weight for product marketing sense

The most direct way to demonstrate I can do that work is to do a small slice of it. This repo is that slice:

- **María (the agent)** = the inbound qualification motion that doesn't exist yet
- **Outbound MP3** = the kind of audio asset that goes into multi-language outbound sequences
- **The Spanish landing page** = how the brand would localize for Mexican B2B
- **The repo and the docs** = how I would document and ship in production

## Architecture

```
┌────────────────────────────────────────────────────────────────┐
│                    Live URL (Vercel-hosted)                     │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  landing/index.html                                       │  │
│  │  - Spanish-LATAM B2B landing page                         │  │
│  │  - Embeds the ElevenAgents widget via a single tag        │  │
│  │  - Tailwind styling, mobile-responsive                    │  │
│  └─────────────────────┬────────────────────────────────────┘  │
└─────────────────────────┼─────────────────────────────────────┘
                          │
                          │ <elevenlabs-convai agent-id="...">
                          ▼
┌────────────────────────────────────────────────────────────────┐
│                  ElevenLabs (managed infra)                    │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  María (ElevenAgents)                                     │  │
│  │  - System prompt: defines identity, goals, guardrails     │  │
│  │  - Knowledge base: 4 markdown docs (uploaded via API)     │  │
│  │  - Voice: Spanish (Mexico neutral) from library           │  │
│  │  - LLM: GPT-4o or equivalent                              │  │
│  └──────────────────────────────────────────────────────────┘  │
└────────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────────┐
│                  Bonus: outbound MP3 sample                    │
│  samples/01_outbound_mexico_fintech_cmo.mp3                    │
│  - 30-second voicemail-style audio                             │
│  - Generated via ElevenAPI TTS endpoint                        │
│  - Script and prompt notes in samples/outbound-script.md       │
└────────────────────────────────────────────────────────────────┘
```

## Repo structure

```
elevenlabs-latam-b2b-discovery-agent/
├── README.md                            # This file
├── vercel.json                          # Vercel deploy config + security headers
├── landing/
│   ├── index.html                       # The landing page with widget embed
│   └── styles.css                       # Custom styles on top of Tailwind CDN
├── agent/
│   ├── system-prompt.md                 # María's full system prompt
│   ├── knowledge-base/
│   │   ├── 01-elevenagents-b2b.md       # KB doc: ElevenAgents use cases for LATAM B2B
│   │   ├── 02-elevencreative-mkt.md     # KB doc: ElevenCreative use cases for marketing
│   │   ├── 03-elevenapi-devs.md         # KB doc: ElevenAPI use cases for devs
│   │   └── 04-latam-objections.md       # KB doc: LATAM B2B objection handling
│   └── provision.py                     # Provisions María via API: agent + KB + voice
├── samples/
│   ├── 01_outbound_mexico_fintech_cmo.mp3  # 30-sec outbound voicemail demo
│   ├── outbound-script.md               # The script + prompt engineering notes
│   └── generate.py                      # Script to regenerate the MP3 via TTS API
├── docs/
│   ├── architecture.md                  # Deeper dive on how it connects
│   ├── design-decisions.md              # Why these choices (voice, prompt, scope)
│   └── how-this-maps-to-the-role.md     # Why this work demonstrates fit for the JD
├── requirements.txt                     # Python deps for provision.py + generate.py
└── .env.example                         # Template for ELEVENLABS_API_KEY
```

## Quickstart (reproducing locally)

### Prerequisites

- Python 3.10+
- An ElevenLabs API key (free tier works for testing; Starter $6/mo recommended for production review)
- `pip` and a virtual environment

### Steps

```bash
# 1. Clone and enter
git clone https://github.com/ramotasaray/elevenlabs-latam-b2b-discovery-agent.git
cd elevenlabs-latam-b2b-discovery-agent

# 2. Python deps
pip install -r requirements.txt

# 3. Copy env template and add your API key
cp .env.example .env
# Edit .env, set ELEVENLABS_API_KEY=your_key

# 4. Provision the agent + knowledge base
python agent/provision.py

# This will output the agent_id. Paste it into landing/index.html
# Replace AGENT_ID_PLACEHOLDER with your actual agent ID.

# 5. Regenerate the bonus MP3 (optional)
python samples/generate.py

# 6. Open the landing page
open landing/index.html
# Or serve locally:
python -m http.server 8000 --directory landing
```

### Deploying to Vercel

```bash
# After editing landing/index.html with the real agent_id:
cd landing
vercel --prod
```

Or import the GitHub repo into Vercel from the dashboard (no CLI needed).

## Design decisions

See `docs/design-decisions.md` for the long-form rationale. The short version:

- **Spanish Mexico voice**: largest LATAM Spanish-speaking market; closest to "neutral" within the regional accents
- **No price quotes**: the agent routes pricing conversations to the real ElevenLabs team
- **Disclaimer-first**: María always discloses she is a candidate's proof-of-work in turn 1
- **Knowledge base grounded**: 4 documents covering each product + LATAM-specific objections, to prevent hallucinations
- **Free tier scoped**: works on the 15-minute free tier; recommend Starter $6 for review-window safety margin
- **Conversation scope tight**: discovery and routing, not full sales cycle

## What I would do differently if I owned this in production

1. Integrate María with a real CRM (HubSpot / Salesforce) via the ElevenAgents tools framework, so qualified leads write directly to the pipeline
2. Per-country voice variants (Argentine, Colombian) routed by visitor IP
3. Branching workflows: different conversational paths for fintech / retail / telco
4. A/B testing different opening lines via ElevenAgents experiments feature
5. Outbound batch calling integration via Twilio for the OUTBOUND side
6. Real-time dashboards on demos booked vs conversations dropped

## Disclaimers

- This is not an official ElevenLabs product or representation
- Built independently in approximately 2 hours as proof-of-work for an application
- Knowledge base is grounded on public ElevenLabs documentation as of May 2026; product details may have evolved
- Free tier ElevenAgents includes 15 minutes of conversation per month; if the agent stops responding, the tier limit may have been reached

## Contact

Daniel Ramírez
daniel.ramirez.crc@gmail.com
linkedin.com/in/ramo5
referido.pro
