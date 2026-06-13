# Tolaria Vault — Agent Protocol

This vault is Alan Soon's personal and work knowledge base (1,001 notes, migrated from Bear). Uses an extended Portent model with 10 types and explicit graph relationships.

## Core Rules

- Model reality first. Use types and relationships, not folders, as the source of meaning.
- Every durable note needs: **what is it?** (type) and **what is it useful for?** (relationships).
- Prefer existing types before creating new ones.
- Always include an H1 (`# Title`) as the first line of the note body. Tolaria uses the first H1 as the note title.
- Keep archived material searchable but hidden from active views by default.
- Alan is in Singapore (GMT+8). Email sign-off is all lowercase "a."

## Types in Use

| Type | Count | Key Fields |
|------|-------|-----------|
| **Coaching-Session** | 155 | `client`, `session_date`, `belongs_to: Splice Media` |
| **Meeting-Note** | 129 | `date`, `participants` |
| **Aviation-Reference** | 123 | `category`, `source`, `related_to: Magenta Debrief` |
| **Personal-Note** | 113 | `date` |
| **Project-Note** | 72 | `status`, `url` |
| **Quote** | 46 | `attribution` |
| **Media-Analysis** | 23 | `source_url`, `publication`, `author` |
| **Grant-Radar** | 11 | `radar_date`, `region`, `belongs_to: Magenta Debrief`, `related_to: Dronefly.sg` |
| **Story-Scout** | 8 | `scout_date`, `recommendation`, `related_to: Slugs` |
| **Note** | 320 | Catch-all for uncategorized clippings and references |

## Note Format

```yaml
---
type: Coaching-Session
client: Nadia Trinidad
session_date: 2023-07-04
belongs_to: Splice Media
tags:
  - coaching/clients
---

# Coaching - Nadia Trinidad
```

## Relationships Already Applied

- **All coaching sessions** → `belongs_to: Splice Media`
- **All aviation references** → `related_to: Magenta Debrief`
- **All grant radars** → `belongs_to: Magenta Debrief` + `related_to: Dronefly.sg`
- **All story scouts** → `related_to: Slugs`
- **19 old notes** → `status: archived`

When creating new notes, add the appropriate relationship links.

## Lifecycle

- **Captured**: Raw, no structure yet. Lives in inbox or as Note type.
- **Organized**: Has type + relationships. Appears in normal views.
- **Archived**: `status: archived`. Not in active views but searchable.
