# How this deliverable maps to the role

The B2B Marketing Spanish-LATAM Growth Lead role description (publicly available at elevenlabs.io/careers) calls out specific responsibilities and requirements. This document maps each one to a concrete artifact in this repo.

## Responsibilities → artifacts

| Responsibility (verbatim from JD) | Artifact in this repo |
|---|---|
| "Regional Growth Engine: Make sure Spanish-speaking Latam B2B (Mexico especially) grows through aggressive lead generation and brand awareness." | The landing page is the brand-awareness piece. The agent (María) is the lead-generation piece: it qualifies inbound traffic and routes to the team. |
| "Outbound Strategy: Build and execute complex, multi-language outbound sequences that cut through the noise." | The Amanda voicemail (`samples/01_outbound_mexico_fintech_cmo.mp3`) is one node of an outbound sequence: a personalized audio voicemail drop with a named SDR persona. The script in `samples/outbound-script.md` shows the prompt-engineering approach. Multi-language is trivial to extend (same script in AR / CO accents under regional Amanda variants). |
| "Local Events: End-to-end ownership of local industry events, user conferences, and webinars in the region." | The agent could (and would, in production) live on event landing pages and run inbound qualification during webinar registrations. This is a sketch of that infrastructure. |
| "Cross-Functional Synergy: Collaborate with performance marketing on ABM initiatives and localized retargeting." | The widget on landing pages enables per-vertical landing variants for ABM: same agent, different page copy and KB doc per target account. Amanda's outbound script generalizes the same way for ABM audio drops. |
| "Analytics & Reporting: Monitor campaign performance, produce executive-level reporting, and recommend data-driven optimizations." | ElevenAgents has built-in analytics for conversation outcomes, transcripts, demos booked. The infrastructure to report on this lead-source is in place by default. |
| "Localization & Messaging: Adapt ElevenLabs' global voice to resonate deeply with the Latam business cultures." | The entire landing page + agent persona is Spanish Mexico, with vocabulary, tone, and objection-handling specific to LATAM B2B procurement realities (see `agent/knowledge-base/04-latam-objections.md`). |

## Requirements → evidence

| Requirement (verbatim) | Evidence |
|---|---|
| "Native Spanish speaker." | Repo and all artifacts in Spanish-MX neutral. |
| "Fluent English speaker." | All docs written in English. Code comments in English. |
| "Ownership Pedigree: You have implemented marketing projects from start to finish and held yourself accountable for the ROI." | Resume + cover letter cover this (Tecnikids Head of Marketing, Padre JP creator brand 3K→13K). This repo is itself an end-to-end shipped project. |
| "Entrepreneurial Background: You have a strong drive and a history of high engagement, ideally in an entrepreneurial endeavor or a similar high-stakes environment." | Real estate wholesaling founder. Building referido.pro. Independent for 18+ months across multi-client work plus own product. |
| "Thrives in Chaos: You are energized by a dynamic, ever-changing environment and can manage multiple workstreams without losing focus." | This repo + the resume + cover letter + form answers were all built in approximately one work day. |
| "The Jack of All Trades: Broad knowledge in growth marketing, ranging from numbers analysis and performance knowledge to campaign planning and event organizing." | Resume covers this. Repo shows it: I designed the agent, wrote the system prompt and knowledge base, built the landing page, deployed it, and documented the architecture. One person, full stack. |
| "DRI Mentality: Ability to act as the local Directly Responsible Individual (DRI) for all marketing operations." | This repo is a DRI proof: one person, full scope, shipped artifact. |

## Bonus experience → evidence

| Bonus (verbatim) | Evidence |
|---|---|
| "Proficiency in cold email, SEO, or affiliate management." | Resume: cold outreach in real estate wholesaling. AEO/SEO via referido.pro. |
| "Product marketing sense and design skills." | The landing page + agent persona are product marketing applied to ElevenLabs' own products. The landing page demonstrates basic design competence (minimal but coherent). |
| "Deep understanding of the Spanish-speaking LATAM tech ecosystem and buying-cycle shifts." | `agent/knowledge-base/04-latam-objections.md` documents the actual procurement realities (LFPDPPP Mexico, CFDI, MXN/ARS invoicing, local SLA expectations) that vary by country. |

## What "doing the work before being hired" looks like, applied to this role

If I were hired today and given Day 1 freedom, the first weeks of work would look very similar to this repo, but scaled up:

- **Week 1**: audit current inbound traffic, identify top 3 vertical opportunities in Mexico → here I built a generic vertical-agnostic discovery agent as proof
- **Week 2**: build the first inbound qualification motion → I built one for this proof
- **Week 3**: build the first outbound asset library → I built one Amanda voicemail as proof
- **Week 4**: ship the first landing variant for ABM → the landing page is a generic version; production would have per-vertical variants

The work in this repo is approximately 1-2% of what the role would entail in the first 90 days. It exists to demonstrate that the work would actually get done.
