# Magenta changelog

Agent-driven changes to magentadebrief.com — theme, SEO, content, analytics infrastructure. Ordered newest first.

---

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
