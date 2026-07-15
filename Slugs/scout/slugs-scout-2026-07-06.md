# Slugs Scout — July 6, 2026

## Entity Resolution

| Operator | Resolved URL | Status |
|----------|-------------|--------|
| Nate B. Jones | newsletter.natebjones.com | 000 (unreachable) |
| Tobi Lütke | tobi.lutke.com | 200 — latest post Dec 2019 (carbon), no recent AI/ops posts |
| Dan Oshinsky | danoshinsky.substack.com / danoshinsky.com | 200 |
| Patrick Boehler | gazzetta.substack.com | 200 |
| Christopher Penn | cspenn.com | 403 (blocked) |
| Rishad Patel | spliceframes.com | 000 (unreachable) |

## Sweep Summary

- **HN front page**: 160 hits scanned, 5 candidates above 30pt keyword threshold
- **Techmeme RSS**: 15 items parsed
- **Press Gazette**: 30 headlines extracted, 5 strong candidates
- **Digiday**: 20 stories extracted, 3 strong candidates
- **Nieman Lab**: RSS returned empty (feed issues)
- **The Verge AI**: JS-rendered, titles not extractable via curl
- **Tobi Lütke blog**: No recent posts since 2019

---

## Top 5 Candidates

### 1. Google AI Overviews surfaces suicide method in search results

**Date:** July 2, 2026
**Source:** https://pressgazette.co.uk/news/google-ai-overviews-suicide-detail/
**Discovered by:** Nicola Agius, Reach SEO and Discover director (LinkedIn post)

**The moment:** Google's AI Overview prominently displayed a suicide method at the top of search results when users searched for "Caroline Flack brother" — in direct breach of Samaritans and Mind reporting guidelines, and the UK Editors' Code.

**Key quotes:**
- Nicola Agius: "Google generated an AI Overview that didn't just confirm his death — it stated, right at the top of the SERP, that he had died by suicide. The AIO also included the location and method."
- Press Gazette describes the prominence as "incredibly worrying" and notes that Google was urged to look at how AI summaries handle sensitive subjects.

**Rupture:** AI search doesn't just hallucinate facts — it strips away the editorial safeguards that human-curated search built over decades. Traditional Google Search already had mechanisms to avoid surfacing suicide methods. The AI layer bypassed all of them. The distribution surface has no editor.

**Theme:** Platform power / AI and the media paradigm shift

**Alan signal needed:** Aviation safety — the Swiss cheese model. Google had layers (Editors' Code compliance, Samaritans guidelines, content policy) but the AI Overview layer aligned all the holes. A LaGuardia crash moment for AI search safety. His own experience with AI tools producing harmful outputs when context is absent.

**Angle:** The AI search surface is a distribution system with no editorial function. Every publisher who thinks they just need to "optimize for AI Overviews" should look at what happens when the model doesn't know what harm looks like.

**Closing provocation:** "If Google can't stop its AI from telling people how to kill themselves, what makes you think it'll protect your journalism?"

---

### 2. Valnet moves journalists to pay-per-click contracts — $8 per 1,000 clicks

**Date:** June 29, 2026 (updated July 2)
**Source:** https://pressgazette.co.uk/news/confusion-and-anger-as-publisher-moves-journalists-to-pay-per-click-contracts/

**The moment:** Valnet — a "digital media investment company" that owns Polygon, GameRant, Screenrant, Movieweb, and 23 other brands attracting 300 million monthly visitors — issued new terms to 30 freelance writers on The Gamer: $8 per thousand clicks, no base fee. At least 25 staff were laid off at Polygon after its 2025 acquisition by Valnet. All UK staff at Pocket-Lint were made redundant when Valnet bought it.

**Key quotes:**
- Press Gazette: "Journalists at a leading popular culture publisher have reacted with 'anger' and 'confusion' to news their pay has become entirely dependent on the amount of traffic they personally drive."
- Valnet operates 27 media brands attracting 300 million monthly visitors.

**Rupture:** This isn't a scrappy SEO farm — it's a major digital media company that now owns Polygon, a respected games journalism brand acquired in 2025. The click-chase economy has been explicitly encoded into employment contracts. A journalist's worth is literally their traffic number. The model says: "you are worth exactly $8 per thousand people who click."

**Theme:** Business strategy and product

**Alan signal needed:** A conversation with a media founder trying to balance quality and traffic. Or his own experience running Splice and watching the click-chase dynamic from the funder side. The coaching lens: what do you tell a journalist who just got this contract?

**Angle:** The funnel was always the problem. But when the funnel becomes the employment contract — when your paycheck is literally your click count — there's no pretending the work is about anything else. The business model eats the journalism from the inside.

**Closing provocation:** "What would your journalists write if you paid them $8 per thousand clicks?"

---

### 3. Time builds invisible bot-readable website for AI agents

**Date:** June 24-25, 2026 (Cannes Lions)
**Source:** https://pressgazette.co.uk/marketing/time-and-axios-turn-ai-prominence-into-advertising-revenue/
**Secondary:** https://digiday.com/media/how-time-and-others-are-rebuilding-parts-of-the-web-for-ai-agents/

**The moment:** Speaking at Cannes Lions, Time COO Mark Howard revealed the company has built an invisible, bot-readable version of its website — used to promote sponsored content to AI agents. Time and Axios are both commercializing AI visibility as a new ad product. This isn't blocking AI crawlers; it's building them a dedicated door.

**Key quotes:**
- Mark Howard (Time COO): Time is "already commercialising an invisible bot-readable version of its website which is used to promote sponsored content."
- The revelation came during the Press Gazette News Yacht event at Cannes Lions alongside executives from Hearst UK, Axios, The Guardian, Washington Post, and Future Plc.

**Rupture:** The dominant publisher narrative is "defend against AI scraping." Time has moved past that fight entirely — they're building a parallel web where the primary reader is a machine, and the business model is getting your brand into the agent's context window. The human-readable web becomes secondary.

**Theme:** AI and the media paradigm shift

**Alan signal needed:** His own context engineering framework — this is literally publishers doing context engineering for AI agents. He could reference his Magenta/FlyCheck build experience where he's thinking about AI consumption surfaces.

**Angle:** "Context engineering" was Alan's term for the work of specifying what AI should do. Time just made it a commercial product: engineer the context that goes into the agent, and sell access to it.

**Closing provocation:** "When the bot-readable version of your site matters more than the human one, who is your real audience?"

---

### 4. GLM 5.2 and the coming AI margin collapse

**Date:** July 6, 2026
**Source:** https://martinalderson.com/posts/the-upcoming-ai-margin-collapse-part-1-glm-5-2/

**The moment:** Martin Alderson's analysis of Chinese LLM GLM 5.2 (295B parameters, Apache 2.0 license, competitive with top models) argues that AI inference margins — currently ~90% gross margin on $25/MTok pricing — are about to collapse. The "real DeepSeek moment" isn't cheaper training; it's inference becoming a race to zero.

**Key quotes:**
- Alderson: "When Anthropic/OpenAI charge $25/MTok for inference, my napkin maths suggests that this is probably something like 90% gross margin on the cost of compute vs the rack rate."
- "The real DeepSeek moment is upon us... The mainstream understanding — that the API costs the providers charge are their real costs — is mistaken."
- Tencent also released Hy3 (295B parameters, Apache 2.0) on the same day — two competitive open-weight models in one day from China.

**Rupture:** The AI industry's business model is built on 90% inference margins that can't survive open-weight competition. When inference is near-free, the scarce resource isn't model access — it's the judgment to use it well. Alan's "production is free" thesis goes from metaphor to literal market reality.

**Theme:** AI and the media paradigm shift

**Alan signal needed:** His own AI tools (FlyCheck, Magenta) where inference cost is already negligible. The "production is free" thesis he's been writing about for a year — this is the market data that proves it.

**Angle:** Every media company betting on "AI-powered" as a differentiator needs to understand: the AI part is about to be free. The differentiator is everything else — the judgment, the specification, the context. Production is free. Context engineering is the business.

**Closing provocation:** "What's your product worth when the AI that powers it costs nothing?"

---

### 5. UK CMA dismantles Apple/Google app store tax for publishers

**Date:** July 2, 2026
**Source:** https://pressgazette.co.uk/platforms/cma-targets-apple-and-google-app-stores-good-news-for-publishers/

**The moment:** The UK Competition and Markets Authority (CMA) published new requirements under the Digital Markets Act allowing app developers to direct customers to external payment options — removing the 30% commission and allowing publishers to "sell directly from their apps and keep subscriber data."

**Key quotes:**
- Jonny Kaldor, CEO of Pugpig (app developer for news publishers): "This is good news for news organisations."
- The CMA designated both Apple and Google's mobile platforms as having "strategic market status" in October 2025 under the Digital Markets, Competition and Consumers Act.
- Currently publishers on iOS/Android must process digital purchases through in-app systems with up to 30% commission.

**Rupture:** For 15+ years, the 30% app store tax was an immovable fact of digital business — every publisher built subscription economics around it. Now a regulator has effectively said: no, you can route around it and keep your subscriber data. The platform power that shaped publisher revenue models is being rewired.

**Theme:** Platform power

**Alan signal needed:** Splice conversations with publishers about platform dependency. The relief of a founder who realizes they just got a 30% margin increase on every in-app subscription.

**Angle:** Publishers have spent a decade optimizing around a tax they couldn't avoid. Now the tax is being removed. The question isn't "will you save 30%?" — it's "what did you stop building because the math didn't work at 30%?"

**Closing provocation:** "What would you build if you got 30% of your subscription revenue back tomorrow?"

---

## Additional Signals (Not Ranked)

### Le Monde's "good bots, bad bots" framework
- **Source:** https://pressgazette.co.uk/publishers/how-le-monde-is-fiercely-defending-journalism-from-bad-bots/
- **Date:** July 6, 2026
- Le Monde has licensing deals with OpenAI, Perplexity, and Meta ("good bots") while fighting off scrapers and credential stuffers ("bad bots"). CTO Paul Laleu: "We see attempts to impersonate Google."
- **Rupture note:** The AI negotiation isn't binary; publishers are learning to differentiate between value-exchange bots and parasite bots.

### Google AI changes could deal further blow to publisher Discover traffic
- **Source:** https://pressgazette.co.uk/platforms/google-ai-changes-could-deal-further-blow-to-publisher-discover-traffic/
- Google Discover is a significant traffic source for publishers; AI changes could further cannibalize it.
- **Rupture note:** Weaker standalone but pairs with candidate #1 — Google's AI is attacking publisher traffic from multiple fronts.

### Illinois SB 315: AI safety audits required
- **Source:** https://www.techmeme.com/260706/p23 (via CBS News)
- **Date:** July 2026
- Illinois Governor signed bill requiring annual third-party safety audits of leading AI companies. OpenAI and Anthropic backed it.
- **Rupture note:** AI companies supporting regulation that audits them — preemptive compliance strategy.

