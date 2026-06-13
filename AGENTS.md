# Tolaria Vault — Agent Protocol

This vault is Alan Soon's personal and work knowledge base, organized using an extended Portent model.

## Core Rules

- Model reality first. Do not use folders as the main source of meaning; use types and relationships.
- Every durable note should answer: **what is this?** (type) and **what will this be useful for?** (relationships).
- Prefer existing types before creating new ones.
- Keep archived material searchable but hidden from active views by default.
- Alan uses all lowercase "a." as his sign-off in email.
- Alan is in Singapore (GMT+8).

## Note Format

Every note should have YAML frontmatter with at minimum a `type` field:

```yaml
---
type: <VaultType>
tags:
  - relevant-tag
related_to:
  - "[[linked-note-title]]"
---
```

### Story-Scout specific fields

```yaml
---
type: Story-Scout
scout_date: 2026-04-11
recommendation: "#1 is the essay pick because..."
---
```

### Quote specific fields

```yaml
---
type: Quote
attribution: Person Name
---
```

### Coaching-Session specific fields

```yaml
---
type: Coaching-Session
client: Client Name
session_date: 2023-07-04
---
```

### Media-Analysis specific fields

```yaml
---
type: Media-Analysis
source_url: https://example.com/article
publication: Publication Name
author: Author Name
---
```

## Types

### PORT types (actionable — things to do)

- **Project**: Bounded effort that produces an output. Has beginning and end. Cannot be completed in one sitting.
- **Operation**: Recurring work that can be completed in one sitting. Belongs to a responsibility.
- **Responsibility**: Long-running area of accountability with no natural end date. Measured by indicators or KPIs.

### ENTP types (knowledge artifacts)

- **Event**: Something that happened, retainable in long-term memory.
- **Note**: A durable knowledge artifact. Use broad category.
- **Topic**: An area of interest or conceptual lens. No performance expectations.
- **Person**: A real-world person or AI agent treated as an actor.

### Vault-specific types (extending Portent)

- **Quote**: A single attributed quote. Fields: `attribution`.
- **Story-Scout**: Weekly Slugs story curation with 5 ranked candidates. Fields: `scout_date`, `recommendation`.
- **Coaching-Session**: Coaching session record. Fields: `client`, `session_date`.
- **Media-Analysis**: Industry analysis or strategy note. Fields: `source_url`, `publication`, `author`.
- **Aviation-Reference**: Flight training, POH, or regulation material. Fields: `category`, `source`.
- **Meeting-Note**: Call or meeting notes. Fields: `date`, `participants`.
- **Grant-Radar**: Grant opportunity tracking. Fields: `radar_date`, `region`.
- **Project-Note**: Business planning and strategy artifacts. Fields: `status`, `url`.
- **Personal-Note**: Personal journal and reflections. Fields: `date`.

## Relationships

- **`belongs_to`** — primary context, ownership, or composition. Most objects should have at most one primary parent.
- **`related_to`** — secondary usefulness or association without ownership. Many-to-many.
- Inverse of `belongs_to` is `has` / `contains` / `children`. Inverse of `related_to` is `referred_by` / backlinks.

## Lifecycle

- **Captured**: Recorded but not yet actionable. Lives in inbox or temporary surface.
- **Organized**: Clear title + type + enough relationships to explain future use. Appears in normal views.
- **Archived**: No longer useful in active work, but still useful as memory. Searchable, hidden from active views.

## File Layout

Notes live at the vault root with slugified filenames. Type definitions live in the same directory with their original filenames. Saved views live in `views/`. This vault is a Tolaria portent vault.
