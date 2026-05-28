# Design Decisions

Notes on the choices behind this build and the reasoning. Useful for anyone reproducing or extending it.

## Personas: María (inbound) + Amanda (outbound)

**Why two personas instead of one**: inbound and outbound are different motions in real B2B teams, often staffed by different people. One agent per channel = clean separation of concerns. María handles inbound qualification (lives in the widget). Amanda handles outbound (lives in the MP3 sample). Both use the same product stack (ElevenAgents for live conversation, ElevenAPI for TTS audio assets), which is the point — same platform, two motions.

**Why not multi-persona within each channel**: scope. One persona per channel = one tight system prompt (María) or one tight script (Amanda) + one voice + one consistent test surface. Multi-persona per channel (María-MX + Lucía-AR + Camila-CO for inbound) would multiply the test surface 3x for marginal incremental value at the demo stage. Regional variants are the natural next step in production.

**Why Mexican neutral for both, not Argentine or Colombian**: Mexico is the explicit wedge market in the JD. Mexican Spanish has the largest Spanish-speaking economy ($1.4T GDP) and the highest enterprise SaaS adoption in LATAM. Mexican neutral is also the most widely understood across LATAM, so the demo conversation works for AR/CO/PE/CL visitors even if not optimized for them.

**Why "ejecutiva comercial" rather than "specialist" or "consultant"**: "ejecutiva comercial" is the LATAM enterprise term that signals B2B authority without being jargon-y. Maps to "BDR with strategic depth" in US terms.

## System prompt: tight scope, disclaimer-first

**Why mandatory disclaimer in turn 1**: legal hygiene + transparency. The agent is unmistakably labeled as a candidate's proof-of-work. No risk of confusion with official ElevenLabs sales.

**Why "no price quotes"**: avoids creating expectations the candidate cannot control. Real pricing depends on plan, volume, geography, contract. The agent routes to the real team.

**Why "discovery and route, not full sales cycle"**: scope. The agent does one thing well (qualify) rather than many things poorly (qualify + demo + close + onboard).

**Why use "usted" by default**: LATAM B2B norm. Switching to "tú" automatically signals American/casual which doesn't match enterprise procurement tone. Agent switches only if user tutea first.

## Knowledge base: 4 docs, grounded in public sources

**Why exactly 4 docs**: one per product line (Agents, Creative, API) plus one for cross-cutting LATAM-specific objections. Symmetric and easy to maintain.

**Why markdown not PDF**: ElevenAgents knowledge base ingests markdown cleanly. Markdown is also editable in any text editor and diffable in git.

**Why public sources only**: anything in the KB needs to be defensible if a reviewer asks "where did you get this?". Public docs + the marketing site cover all of it.

**Why include the LATAM objections doc separately**: the four most-common LATAM B2B objections (local invoicing, Spanish support, data residency, latency for real-time) are not in ElevenLabs' generic marketing copy. Making this a separate doc means the agent handles them deterministically.

## Landing page: dark theme, minimal, single-purpose

**Why dark theme**: ElevenLabs' own brand uses a dark surface in much of its product UI. Visual coherence with the source product.

**Why single-purpose (no nav, no extra pages)**: the page exists to host the widget and provide context. Adding pages would be off-brief.

**Why Tailwind CDN, not a framework**: speed. The page is 1 file. No build step. Vercel deploys it in 30 seconds.

**Why the emerald accent color**: an editorial choice that signals "live" and "operational" without copying ElevenLabs' actual brand. Distinct enough to read as candidate work, coherent enough to feel like a B2B SaaS asset.

## Outbound MP3 (Amanda): 1 sample, not 3

**Original plan**: 3 samples in MX, AR, CO accents under a single persona.

**Revised**: 1 high-quality Mexican sample under the Amanda persona. Reasoning:
- Mexico is the wedge; AR/CO are follow-ons
- 1 strong sample > 3 generic ones
- The Python script generalizes to any locale; reviewer can regenerate AR/CO if curious
- Credits focused on the live agent (María), Amanda as a single anchor sample

## Vercel + GitHub: zero infra cost, public artifact

**Why Vercel over GitHub Pages**: prettier URL, faster CDN, easier custom domain if needed later.

**Why a public repo**: the work is verifiable. Anyone can clone, run, modify. That is the proof.

**Why open-source the system prompt + KB**: shows my actual thinking, which is the more valuable artifact than the working demo itself.

## What is intentionally NOT included

- **CRM integration**: would require real production credentials, out of scope for a demo
- **Per-country variants of María**: scope; mentioned as next step
- **Multi-language interface**: Spanish only by design; English would dilute the point
- **Analytics dashboard**: ElevenAgents has built-in analytics; adding custom dashboards would be infrastructure work without proportional demo value
- **Voice cloning of a public ElevenLabs employee**: legal risk; the persona uses a generic library voice

## What I learned building this

- ElevenAgents free tier is generous enough to ship a demo (15 min calls + widget); this build upgraded to Starter ($6/mo, 75 min) for review-window safety margin
- The widget embed (`<elevenlabs-convai>`) is genuinely a single tag — closest thing to "no-code voice AI" I have used
- The knowledge base + system prompt combo is more important than any other config decision; everything else (voice, LLM choice, conversation flow) is downstream of the prompt + KB
- Spanish LATAM voice quality in ElevenLabs models v2/v3 is high enough that the "robotic IVR" objection should die in 12-24 months across the entire enterprise market

If I were running the LATAM B2B Growth motion, this third bullet is the actual market narrative: voice AI is past the threshold where "naturalness" is a buying criterion, and the next 18 months are about who builds the regional category first. The work is more category creation than feature selling.
