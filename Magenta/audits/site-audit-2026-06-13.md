From: alan@magentadebrief.com
To: alan@magentadebrief.com
Subject: Magenta Debrief — bi-weekly site audit, 13 June 2026

DO NOW

1. British "licence" persists on homepage and SG guide

"licence" (UK spelling) appears twice on the homepage hero section and three times on the Singapore pathway guide at https://magentadebrief.com/general-aviation-training-in-singapore/. "organisation" also appears on that page. Fix to US "license" and "organization" for editorial consistency.

2. School Profiles hub has a confusing title

The page at https://magentadebrief.com/schools/ has the title "Magenta Flight School Standard — Magenta Debrief", which reads like a variant of The Magenta Standard. This creates confusion for both readers and AI crawlers trying to distinguish the school evaluation framework from the sim hardware standard. Rename to something like "Flight School Profiles — Magenta Debrief" or "School Evaluations by Magenta Debrief".

3. 404 page still blocks pinch-zoom on mobile

The Cloudflare fallback at https://magentadebrief.com/nonexistent-test serves `user-scalable=no, maximum-scale=1` in its viewport meta — a Google mobile usability error and WCAG 2.2 violation. This requires a paid Cloudflare plan to customize, so flagging for awareness rather than urgency.

4. RAAus directory page weight still high at 109KB

https://magentadebrief.com/list-of-all-raaus-flight-schools/ serves 109KB of HTML — roughly 1-2 seconds first paint on 4G. The 143-row table with pricing, aircraft, and links per cell is the cause. Consider paginating to 20 rows with a "load more" toggle, especially with mobile at 36% of traffic.

5. Product schema still missing price on hardware reviews

The VKB T-Rudder review at https://magentadebrief.com/vkbsim-t-rudder-mk-v-review/ has a complete Product + Review schema now (ratingValue 4.1, brand, category, image) but no `offers` (price) in the JSON-LD. An AI extracting this data gets the product specs but not the purchase price. Same gap likely applies to the 6 other hardware reviews. Adding `offers` with `price` and `priceCurrency` closes a structured data gap that matters for AI citation.

WORTH DOING WITH CONDITIONS

6. Consider a review template for consistent Product schema

Now that Product+Review schema is present on at least one review page, the next step is ensuring all 7 hardware reviews have parity. The VKB review has brand, category, image, and aggregateRating embedded. Check the remaining 6 (Virpil R1-Falcon, PU Air GNS-530, PU Air Korea radio, Desktop Pilot TPM, Tobii Eye Tracker 5, Octavi IFR-1) for the same fields. Condition: verify each page individually rather than assuming API data mirrors rendered HTML schema.

7. Sodo-search updated but still a single render-blocking concern

The search widget at https://magentadebrief.com/ uses sodo-search 1.8.23 (up from 1.8.21) and loads with `defer` — good. But the `/umd/main.css` stylesheet referenced in the `data-styles` attribute may still introduce a render delay on first load. Worth monitoring if Lighthouse or PageSpeed Insights flags it. Low priority — only act if tools show impact.

8. Rybbit chat widget removed — good, confirm pull request

The Rybbit chat widget (app.rybbit.io) that loaded on all pages in May is now gone — confirmed 0 matches on homepage and about page. This reduces JS weight and third-party dependency. If this was a recent deployment, it's working correctly. No action needed.

FIRST PRINCIPLE

The site audit exists because AI citation value compounds on structure, not volume. Every fix in this report either makes Magenta more callable by AI search engines or removes friction from the conversion path for human readers. The 4 new posts (66 total) and clean nav reorganization show the content engine working — the schema and mobile polish are the next compounding layer.

a.

--
Alan Soon / Founder & Chief Editor / Magenta Debrief / https://magentadebrief.com/
