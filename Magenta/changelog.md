# Magenta changelog

Agent-driven changes to magentadebrief.com — theme, SEO, content, analytics infrastructure. Ordered newest first.

---

## 2026-07-01 — Directory monetization: GoFly outreach + infrastructure complete

### GoFly pitch sent
- First featured listing test deployed: Anne-Maree at GoFly Aviation (warm lead — 80 visits already)
- AU$149/month test price, one month, no commitment
- Homepage partner callout, partner page deliverables, and per-school click attribution all in place as backing infrastructure

### Partner page updated
- "Featured directory listing" section rewritten with concrete deliverables: pinned-to-top placement, expanded profile, "Featured" badge, direct Website/Email links, AI discoverability via structured data, per-school click attribution
- Intro paragraph updated with conversion stats: "over 200 qualified inquiries"

### Homepage partner callout deployed
- Replaced "We need your help" charity framing with "For flight schools — get featured" commercial callout
- Links to /partner-with-us/ with Umami event tracking

### GSC snapshot (vs June 24 baseline)
- 85 clicks/week (stable — June 24 was 96 PV/week from Google; within norm)
- 7,043 impressions/week at 1.21% CTR (June 24: ~1,600 imp/week at 1.5% CTR — impression volume WAY up but CTR dilution suggests broader query reach)
- AU: 16 clicks at 1.43% CTR (was 2.0% — slipped but more impressions means broader ranking)
- US: 23 clicks at 1.10% CTR (was 0.5% — CTR DOUBLED. Meta fixes + WingFlex review may be improving wrong-audience clicks into actual interest)
- SG: 6 clicks at 0.77% CTR (was highest-converting — snippet failure still bleeding Singapore guide: 2 clicks from 581 impressions)
- Thailand: 6 clicks at 2.82% CTR (meta rewrite is working — best CTR of any major market)
- Directory: 5 clicks from 513 impressions at 0.97% CTR — the snippet failure is real. Page 7.4 avg position with zero-click meta description
- WingFlex DAP 500 now appearing in GSC: 1 click, 18 impressions, position 4.8 (7 days post-publish)

### Per-school click attribution confirmed working
- `directory.js` already tracks `RAAus School Link Click` events with school name + URL in Umami `event_data` table
- 213 total clicks across 100 unique schools since launch. 19 schools active in last 30 days
- Top school: Adelaide Biplanes (8 clicks). Top recent: Ballarat Flight Training (2 clicks, June 30)
- Report script at `/root/scripts/school-click-report.py` — supports `--top N`, `--active-only`, `--json`

### Key insight
Meta rewrites are still propagating (7 days since June 24 deploy). Impression volume jumped dramatically (more queries matching) but CTR diluted — suggesting Google is testing the pages against more query types. Structured data (June 29) hasn't had time to affect rankings yet. The real test is mid-July.

---

## 2026-06-29 — Structured data: directory + guide FAQ schemas

### RAAus directory: ItemList + EducationalOrganization JSON-LD
- Injected 138-school ItemList JSON-LD (49.4KB) via Ghost `codeinjection_foot`
- Each school gets `EducationalOrganization` with name, address, phone, URL, geo coordinates
- Makes directory machine-readable for AI crawlers without breaking human UX
- Post body strips `<script>` tags, hence `codeinjection_foot` approach

### FAQPage schema: Singapore & Thailand guides
- Added 5 `<details>` FAQ toggles to each guide
- Theme auto-generates FAQPage JSON-LD from `<details>` elements
- Guides had zero structured data previously despite 3,748 combined impressions

### Audit false positives confirmed
- `data-lat`/`data-lng`: all 138 rows have valid coordinates (audit reported empty)
- Page weight: JS lazy-load (30-row batch) already handles directory rendering
- Periodic verification: weekly RAAus diff cron already exists (`bc8c8842a725`)

---

## 2026-06-26 — WingFlex DAP 500 review published + metadata fixes

### Meta/SEO fixes post-publish
- **Meta title:** replaced garbled "An autopilot panel with missing by keyboard bindings" with H1 text "a dedicated GA autopilot panel at US$139 let down by basic keyboard bindings"
- **OG title + description:** set (were None — social previews were bare)
- **Product + Review JSON-LD:** injected via codeinjection_head — `offers` (US$139), `reviewRating` (3.2/5), `brand` (WingFlex). Ghost's auto-schema omits price
- **Tags:** verified `Simulation` + `#hardware-review` both present → theme auto-schema triggers correctly
- **Pending from Alan:** product photos (currently zero images in body)
- **Images added 26 Jun:** feature image (DSC06024-EDIT.webp) + 2 body images (DSC06024-EDIT-1.webp, DSC06022.webp)
- **feature_image_alt** set (191-char limit on Ghost), **feature_image_caption** set, **body image alts** set via lexical JSON editing (HTML roundtrip doesn't persist alt in Ghost 6.x)

### GEO audit on publish
- **Schema fix:** Original codeinjection had `offers` on Product (triggers Merchant listings in GSC — critical error) and was nested Review-inside-Product. Replaced with correct structure: top-level Review → itemReviewed → Product with aggregateRating + image, NO offers, NO review back-ref. Matches review-schema-fix.md template.
- **12/13 GEO signals present:** H1/H2 structure, price in text (US$139), rating in text (3.2/5), product name, brand, category all explicit. robots.txt allows AI crawlers. FAQ schema is the only missing signal (no Q&A content on this review — acceptable).

### Editorial audit findings (reference)
- New sections "Who should wait" and "What would change the verdict quickly" are good evolutions worth standardizing across all hardware reviews
- Missing vs prior reviews: no "About this review" section (disclosure at end instead of up front), no structured "What this is" specs block, no "Setup and first-use reality" section
- Structure drift from MOZA/Virpil/PU Air template — section ordering diverged

## 2026-06-25 — Investigations + infrastructure fixes

### Slugs scout email: smtplib → himalaya
- Switched email delivery from raw Python `smtplib` to `himalaya message send -a splice` (raw MIME)
- Reason: intermittent `[Errno 32] Broken pipe` from Gmail SMTP dropping connections mid-send
- himalaya handles SMTP reconnection internally. Patched in slugs-scout skill.

### Referrals investigated
- **goflyaviation.com.au** (4 PV to RPL cost page): Existing relationship — GoFly Online (Anne-Maree). No new signal.
- **Reddit** (12 PV across 8 pages): Cannot trace specific thread — Reddit strips referrer path. Diversity suggests recommendation thread or user profile links.

---

## 2026-06-24 — Analytics infrastructure + SEO overhaul

### Google Search Console access
- Service account `hermes-gsc@polar-program-474914-j7` created in Google Cloud
- Added as Full user on `sc-domain:magentadebrief.com` (domain property)
- Key stored at `/root/.hermes/gsc-service-account.json`, path in `/root/.env` as `GSC_SERVICE_ACCOUNT_KEY`
- Queryable via Python + `googleapiclient.discovery.build('searchconsole', 'v1')`
- **Key finding**: June on track for ~1,530 pageviews (new all-time high). Google search surging — 96 PV/week, up 4x from ~100/month historical. AU best-converting search market (2.0% CTR), US worst (0.5% CTR from 4,474 impressions).

### Theme fix: meta descriptions now rendering
- `default.hbs` had no meta_description output in `<head>` — `{{ghost_head}}` on line 77 handles it, but our manual `{{meta_description}}` was flagged by Ghost validator as redundant
- Removed duplicate line, `{{ghost_head}}` confirmed handling all SEO tags (meta description, OG, Twitter cards, canonical URL, structured data)
- Theme v2 deployed via Admin API (git push → zip → JWT upload)

### Meta titles + descriptions: 18 posts optimized
- Tier 1 (10 posts, ~1,250 combined monthly impressions): ground school guide, midlife flying, Warbirds canceled, Avalon 2027, CASA exams, aviation events, Lite Air, radio calls, six things before training, first dollar
- Tier 2 (7 posts, ~3,600 combined monthly impressions): Tobii Eye Tracker 5, SG flight schools, RPL cost SG vs AU, AU flight school guide, PU Air GNS 530, Octavi IFR-1, Desktop Pilot TPM
- Plus: Honeycomb Foxtrot (was 2,605 impressions at 0.2% CTR — worst performer)
- All set via Ghost Admin API: `PUT /ghost/api/admin/posts/{id}/` with JWT auth
- Character limits enforced: 60 title, 145 description. Sentence case throughout.

### Feature image alt text: 14 posts
- Every post with a feature image now has descriptive `feature_image_alt` text
- Set via Admin API. Derived from post content — specific image descriptions (product photos, school aircraft, scenic shots)

### What we learned
- `{{ghost_head}}` handles meta description, OG, Twitter cards, canonical, structured data — never duplicate it
- Ghost 6.47. Admin API supports `og_title`, `og_description`, `twitter_title`, `twitter_description` per-post (currently unused — falls back to meta_title/description, which is fine)
- Tag pages get search impressions but most have null meta — future opportunity
- Brand-spam queries ("braun flight stick review", "bosch flight stick review") pollute GSC impressions at position 1 with 0% CTR
