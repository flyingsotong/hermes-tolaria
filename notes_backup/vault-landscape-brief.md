# Tolaria Vault — Comprehensive Landscape Brief
**Generated:** June 13, 2026  
**Methodology:** 1,016 files analyzed. Bulk stats via shell/python, 100+ individual note reads across all 10 types. Content heuristics, frontmatter analysis, and cross-referencing.

---

## 1. ORPHAN NOTES — Type: Note (the catch-all)

**Count:** 352 notes (34.6% of the corpus)  
**Notes with ONLY `type: Note` (no other frontmatter fields):** 346 of 352 (98.3%)  
**Notes with any additional frontmatter:** 6 of 352

### Content Patterns (heuristic categorization)

| Pattern | Count | Current type | Suggested proper type |
|---------|-------|-------------|---------------------|
| Media/journalism content | ~136 | Note | Media-Analysis, Meeting-Note |
| Book/article summaries | ~110 | Note | Quote, Media-Analysis |
| Personal reflection/philosophy | ~90 | Note | Personal-Note |
| Link/article (general reference) | ~86 | Note | Note (keep) or Project-Note |
| AI/ML content | ~77 | Note | Media-Analysis, Topic |
| Startup/founder advice | ~72 | Note | Project-Note, Personal-Note |
| Meeting/call notes | ~39 | Note | **Meeting-Note** (critical mismatch) |
| Aviation content | ~38 | Note | **Aviation-Reference** (critical mismatch) |
| Coaching-related | ~32 | Note | **Coaching-Session** (critical mismatch) |
| Grant/funding content | ~29 | Note | **Grant-Radar** |
| Splice/Magenta/FlyCheck work | ~23 | Note | Project-Note |
| Twitter/X thread captures | ~22 | Note | Quote or Note |
| Substack/newsletter saves | ~19 | Note | Media-Analysis |

### Key Finding
The `type: Note` bucket is a dumping ground. **~200 notes** in this category clearly belong to other existing types (Meeting-Note, Aviation-Reference, Coaching-Session, Grant-Radar). The most critical misfires:
- **38 aviation notes (CAS, airspeed, weight & balance, radio procedures) filed as `type: Note`** instead of `Aviation-Reference`
- **39 meeting/call summaries filed as `type: Note`** instead of `Meeting-Note`
- **29 grant/funding analyses filed as `type: Note`** instead of `Grant-Radar`
- **32 coaching-related notes filed as `type: Note`** instead of `Coaching-Session`

---

## 2. RICH CLUSTERS — Topics, Themes & People with Most Coverage

### Coaching (157 files, 154 unique clients)

**Tag breakdown:**
- `coaching/clients`: 104 notes
- `coaching`: 108 notes
- `coaching/me`: 13 notes (Alan's self-reflection on coaching practice)

**Geographic distribution of coaching clients:**
- India: 9+
- Singapore: 8+
- China/Hong Kong: 11+
- Malaysia: 4+
- Kenya/Africa: 3+
- Thailand: 2+
- Philippines: 2+
- West Africa: 2+
- Also: Mongolia, Australia, Bangladesh, Nepal, Ukraine

**Notable coaching clients (media professionals):**
- Aidila Razak (Malaysiakini)
- Abhay Regi (The Caravan)
- Beatrice Go (journalist)
- Franz Wild (journalist → entrepreneur)
- Nikita Mandhani (journalist → entrepreneur)
- Bilal Lakhani (paid client)
- Gosia Klimowicz (paid client)
- Plus ~100+ more media professionals across Asia/Africa

**ICF credentialing cluster:** 15+ notes on ICF ACC/PCC requirements, coaching competencies, mentor coaching sessions (SMU modules 2-4), Singapore coaching market analysis.

### Aviation (118 Aviation-Reference + 38 miscategorized Note = ~156 notes)

**Sub-categories detected:**
- Weather/conditions: 123 files with keywords
- Safety/emergency procedures: 106
- Stalls/spins: 78
- Takeoff/landing: 72
- Radio/communications: 49
- Aircraft mechanics: 37
- Navigation/nav logs: 26

**Specific sub-corpus:**
- RAAus materials: 18 files
- Drone/UAV/UABT: 12 files (including dronefly references)
- METAR/weather reports: 6 files
- Cross-country planning: 5+ files

### Splice Media (51 files)

Active and historical covering:
- Beta conference (2021-2024)
- School of Splice program
- Client engagements (ICRC, IMS/Puma, Firetree, MDIF, Facebook/Meta)
- Grant program (AFP, Google)
- Rishad Patel collaboration notes
- Partner relationships across Asia/Africa

### Magenta Debrief / FlyCheck (~10-11 files)

Current active projects:
- `strategic-memo.md` — 14-day RAAus directory partnership acceleration plan
- `now.md` — FlyCheck timeline (submitted Feb 2026, approved on App Store)
- CAAS/SkillsFuture grant radar notes scoped for Magenta Debrief
- Aviation directory strategy notes

### Media Analysis (22 type + ~75 in Note bucket)

**Key authors/sources tracked:**
- Brian Morrissey (The Rebooting): 4+ articles
- Troy Young (People vs Algorithms): 1+ article
- Nieman Lab/Reports: 2+ articles
- CUNY lectures: 3+
- Martin Soler hospitality newsletter

### Slugs Newsletter (13 files)

**Story-Scout notes (9):** Weekly curations April-May 2026. Cross-industry signal detection pattern:
- Aviation safety psychology → newsroom AI error detection
- FAA Part 108 BVLOS rules → redesigned human roles in newsrooms
- Jack Dorsey org chart redesign → middle management in media
- Goldman Sachs AI job displacement data

### Grant Radar (7 files)

- 5 Singapore-specific grant scans (April 2026): CAAS AOF, SkillsFuture, NAC
- 1 IFPIM grant analysis/opinion
- 1 bootstrapping/acquisition interview

### Quotes (45-47 files)

Diverse attributions: Napoleon Bonaparte, Esther Perel, Ted Lasso, Kahlil Gibran, Jeff Bezos, Codie Sanchez, Mary Oliver, Harper Lee, Satya Nadella, Naval Ravikant. 9 quotes have no attribution.

### Personal-Note (111 files)

Mix of genuine journal entries (`8-november-2023-8-hours-to-splice-beta.md`, `a-love-letter-alex-elle.md`) and saved external content incorrectly classified (self-help articles, coaching advice from others, Robin Sharma productivity tips). Approximately 30-40% are genuinely personal; the rest are external content saved for reference.

---

## 3. HIDDEN CONNECTIONS — Cross-Category Links

### Coaching Clients Who Are Also Media Contacts / Splice Network

Nearly ALL coaching clients are journalists or media entrepreneurs — this is the deepest hidden connection. The coaching practice grew directly out of the Splice Media community. Key overlaps:

| Client | Coaching Context | Also Appears In |
|--------|-----------------|-----------------|
| Ankhbayar Tserenvandan | Coaching session | Splice meeting (Lemon Press, Mongolia) |
| Sharada Balasubramanian | Coaching session | Referenced in claude-analysis |
| Ayswarya Murthy | Coaching session | Likely Splice/Beta participant |
| Bhanupriya Rao | RFTW coaching + BehanBox | Splice network |
| Nikita Mandhani | Coaching → entrepreneurship | Claude analysis reference |
| Franz Wild | Coaching → business leader | Claude analysis reference |
| Tim Mak | Call (Meeting-Note: 7-jan-2025) | Substack publisher, could be coaching lead |

**RECOMMENDATION:** Add `belongs_to: Splice Media` or `related_to: "[[Splice Media]]"` to all coaching client notes. The coaching practice is a downstream service of the Splice community.

### Aviation ↔ Grants Connection

The CAAS Aviation Outreach Fund (AOF) and SkillsFuture grants are being actively scouted for:
- **Dronefly.sg:** Singapore drone law education + safety culture
- **Magenta Debrief:** Aviation education content
- **RAAus partnership** (strategic-memo.md): Directory structure discussions

These three threads (grant radar, dronefly, magenta, RAAus) are not explicitly linked in frontmatter but are deeply connected in practice.

### Story-Scout ↔ Current Work

The Story-Scout notes for Slugs explicitly draw on aviation safety concepts (Swiss Cheese model, FAA Part 108, AI copilot human factors) and apply them to journalism — directly bridging Alan's two professional identities (pilot + media operator). These cross-disciplinary translations are the signature of the Slugs newsletter but no frontmatter links them to the Aviation-Reference notes.

### Splice Old Projects ↔ Current Work

Old Splice client engagements (ICRC 2021, IMS/Puma 2021, Firetree 2021, Facebook/Meta 2021) contain contacts, frameworks, and case studies that are still relevant for:
- Current Splice coaching work
- Grant applications (demonstrating track record)
- Media Analysis notes (industry transformation themes)

These are not cross-referenced.

---

## 4. ORPHANED NOTES — Most Disconnected Items

**Definition:** Notes with NO tags AND NO url AND NO relationships (belongs_to/related_to/connections) in frontmatter.

**Count:** 751 notes out of 1,016 (74%) have ONLY a `type` field and nothing else.

**Most critically orphaned (no frontmatter of any kind):**

The following notes from the type:Note bucket have ZERO metadata — no tags, no URL, no relationships, no date:

- `10-best-ideas-from-tim-ferriss.md` — Twitter thread, should have `url:`
- `2026-02-16t022345z.md` — philosophical reflection on AI adoption, no date field despite date in name
- `presentation.md` — completely unidentifiable
- `partnership-opportunities.md` — business-critical, no metadata
- `technical-memo-self-hosted-umami-analytics-server.md` — project documentation, no project link
- `project-youtube-transcriber-api-on-spaceship-vps.md` — self-explanatory but no tags
- `first-day-back-from-europe-intro-with-hon-yuen-leong.md` — meeting notes filed as Note
- Various `meeting.md`, `notes.md`, unnamed drafts

**Pattern:** 74% of the vault has no relational metadata. The vault is a flat file dump with type annotations but virtually no link structure. The AGENTS.md protocol specifies `related_to` and `belongs_to` as core to the model, but they are almost entirely unused.

---

## 5. STRUCTURAL RECOMMENDATIONS

### Notes to Archive (outdated Splice projects, old grant scans)

**Archive candidates (historical Splice client engagements — 2021-2022):**
- `firetree-splice-june-16-2021.md` — One-off meeting, no ongoing relationship
- `icrc-x-splice-may-12-2021.md` — Old ICRC engagement proposal
- `icrc-x-splice-june-16-2021.md` — Follow-up to above
- `ims-puma-splice-june-10-2021.md` — Myanmar media project, 2021
- `alex-rishad-alan-june-17-2021.md` — Facebook/Meta call, 2021
- `pat-splice-may-20-2021.md` — MDIF call, 2021
- `pankajfactordaily-alansplice-june-17-2021.md` — FactorDaily, 2021
- `jane-splice-june-3-2021.md` — Old client call
- `jane-mahoney-private-media-splice-pink-ep-4.md` — Old podcast episode
- `anita-alan-july-6-2021.md` — ICRC follow-up, 2021

**Archive candidates (outdated grant scans — superseded by newer versions):**
- `sg-grants-radar-20-apr-2026.md` — Superseded by sg-grants-radar-27-apr-2026.md
- `caas-skillsfuture-radar-20-apr-2026.md` — Superseded by caas-skillsfuture-radar-27-apr-2026.md
- `slugs-story-scout-april-8-2026.md` — Revised version exists (april-8-2026-revised.md)

### Notes That Need `belongs_to` / `related_to` Added

**High priority (every coaching client note — ~147 notes):**
Add to each coaching-client note:
```yaml
belongs_to: Splice Media
related_to:
  - "[[Splice Media]]"
```

**Medium priority (aviation notes — ~156 files):**
Link to current active projects:
```yaml
related_to:
  - "[[Magenta Debrief]]"
  - "[[Dronefly.sg]]"
```

**Grant radar notes:**
Link to venture:
```yaml
belongs_to: "[[Magenta Debrief]]"
related_to:
  - "[[Dronefly.sg]]"
  - "[[strategic-memo]]"
```

**Story-Scout notes:**
Link to source material:
```yaml
related_to:
  - "[[Aviation-Reference/ai-copilot-role]]"  # etc.
```

### Duplicate / Merge Candidates

| Files | Issue | Action |
|-------|-------|--------|
| `20-commandments-to-not-fck-up-buying-a-business.md` + `-2.md` | Same content, different save | Merge, keep one |
| `240-days-to-raise-creating-for-urgency-and-transparency.md` + `-2.md` | Same content | Merge, keep one |
| `journalism-needs-leaders-who-know-how-to-run-a-business-nieman-reports-laura-kra.md` + `-2.md` | Same article, two saves | Merge |
| `slugs-story-scout-april-8-2026.md` + `-revised.md` | Revision supersedes original | Archive original |
| `sg-grants-radar-20-apr-2026.md` + `-2.md` | Same date, different content? | Investigate — may be different scans |
| `quotes-differentiation-is-survival.md` + `-2.md` | Same quote | Merge |
| `people-are-the-new-brands-no-mercy-no-malice.md` + `-2.md` | Same article | Merge |
| `the-era-of-community-led-growth.md` + `-2.md` | Same article | Merge |
| `why-startups-need-to-focus-on-sales-not-marketing.md` + `-2.md` | Same thread | Merge |
| `debrief-lesson-10`, `-11`, `-12`, `-3` | Flight training debriefs | Keep separate (different lessons) |

### Suggested New Types or Type Splits

1. **`Book-Note`** — Currently ~70-80 book/article summary notes are in `type: Note`. They form a clear cluster (book notes, key takeaways, marginalia). A dedicated type with `author`, `isbn` fields would organize them.

2. **`Twitter-Thread`** — ~22+ notes that are pure Twitter/X thread captures with the original URL. These have no analysis/insight added — they're saved references. A dedicated type would distinguish them from analyzed notes.

3. **`Draft` / `Scratch`** — Several notes are clearly in-progress (untitled, single sentence, timestamp-only filenames like `2026-02-16t022345z.md`). A lifecycle status field (`status: draft`) on any type would solve this without a new type.

4. **Split `Personal-Note`** — The 111 Personal-Note files mix genuine journal entries with saved external content. A `type: Saved-Article` or a `source_url` field requirement on Personal-Note would disambiguate.

5. **`Aviation-Training` vs `Aviation-Reference`** — The current Aviation-Reference type mixes regulatory reference material (POH, CAS definitions) with training debriefs (lesson notes, progress tracking). Consider a `Flight-Lesson` type for training session records.

---

## 6. SYNTHESIS POTENTIAL — Essays, Reports & Summaries

### Ready to Write (sufficient material exists)

**1. "AI in Journalism" — Brief/Report**
- **Source material:** 77+ type:Note files on AI/ML + 22 Media-Analysis + Story-Scout AI themes + CUNY lectures
- **Key angles:** AI job displacement (Goldman Sachs data), AI copilot human factors (aviation crossover), automation in newsrooms, the "audience of one" concept
- **Estimated read length:** 3,000-5,000 words
- **Output format:** Slugs essay + potential Splice report

**2. "Coaching Philosophy & Practice" — Reflection/Method Paper**
- **Source material:** Claude analysis of Alan's coaching, 154 client sessions, ICF credentialing notes, coaching questions bank, philosophy notes (Trillion Dollar Coach, ethical coaching, reframes)
- **Key angles:** The media professional → entrepreneur pipeline, journalistic skills transferable to coaching, the "over-functioning" trap, reframing as core competency
- **Estimated read length:** 2,000-3,000 words
- **Output format:** Personal essay or coaching practice positioning document

**3. "Aviation Safety Thinking for Media Operators" — Slugs Essay Series**
- **Source material:** 118+ Aviation-Reference notes + Story-Scout cross-applications (Swiss Cheese, CRM, startle response, FAA Part 108) + coaching parallels
- **Key angles:** Swiss Cheese model → newsroom error detection, AI copilot → AI co-editor, CRM → newsroom team dynamics, BVLOS rules → editorial autonomy redesign
- **Estimated read length:** 1,500-2,000 words per essay (3-5 essays)
- **Output format:** Slugs series; this is already partially written in Story-Scout notes

**4. "The Splice Decade" — Retrospective / Case Study Collection**
- **Source material:** 51 Splice files spanning 2021-2026, Beta conferences, School of Splice, client engagements (ICRC, IMS, Google, Meta), 8-years-of-splice.md
- **Key angles:** Building a media startup community in Asia, the pivot from consulting to coaching, grant-funded vs revenue-funded models
- **Estimated read length:** 3,000-5,000 words
- **Output format:** Splice blog post or industry talk

**5. "Singapore Media Ecosystem: Grants, Policy & Opportunities" — Briefing**
- **Source material:** 7 Grant-Radar notes + Singapore-specific coaching clients + CAAS/SkillsFuture analysis + Media-Analysis of Singapore context
- **Key angles:** CAAS Aviation Outreach Fund for Magenta Debrief, SkillsFuture for coaching, NAC arts grants, media sustainability funding gap
- **Estimated read length:** 2,000 words
- **Output format:** Internal strategic memo or grant application support

**6. "Startup Wisdom from Twitter Threads" — Curated Collection**
- **Source material:** 22+ Twitter thread captures + 72 startup/founder advice notes + Codie Sanchez / Contrarian Thinking content
- **Key angles:** Business acquisition vs building, MVP frameworks, fundraising tactics, mental models for founders
- **Estimated read length:** 1,500-2,500 words
- **Output format:** Newsletter issue or coaching resource

### Future Potential (needs some additional capture work)

**7. "Coaching Across Cultures: Asia-Pacific Media Professionals"**
Needs: Geographic tagging on all client notes, cross-cultural patterns analysis. Data exists but unaggregated.

**8. "The Transition Architect: From Journalist to Entrepreneur"**
Needs: Synthesis of client journeys (Aidila, Franz, Nikita, Abhay, Sharada), Alan's own transition story, coaching methodology. Rich material exists across coaching notes + Personal-Note + claude-analysis.

**9. "Dronefly.sg: Singapore Drone Law & Safety — Product Brief"**
Needs: The drone/aviation reference material is scattered across Aviation-Reference notes and grant radars. Would benefit from dedicated collection.

---

## SUMMARY STATS

| Metric | Value |
|--------|-------|
| Total notes | 1,016 |
| Types used | 10 (Note, Coaching-Session, Meeting-Note, Aviation-Reference, Personal-Note, Project-Note, Quote, Media-Analysis, Story-Scout, Grant-Radar) |
| Notes with only `type:` field | 751 (74%) |
| Notes with tags | 214 (21%) |
| Notes with url/source_url | ~50 (5%) |
| Notes with relationships | ~0 (notably absent) |
| Notes with dates | ~60 (6%) |
| Duplicate pairs | 18 pairs |
| Coaching clients | 154 unique |
| Unique Quote attributions | ~40 |
| Estimated % correctly typed | ~60% (most Note-catchall files belong elsewhere) |

**Health assessment:** The vault has rich content but minimal structure. The type system is used but relationships (`belongs_to`, `related_to`) are almost entirely absent. The `type: Note` catchall has become a default dumping ground representing 35% of the corpus. The metadata hygiene rate (~26% have more than a type field) means the vault's discoverability is low despite the depth of content.
