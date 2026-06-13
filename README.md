# Hermes → Tolaria Vault

This vault is Alan Soon's knowledge base, migrated from Bear notes into a Tolaria-compatible structure. It is local-first, Git-first, and Markdown-based.

## Structure

The vault extends Portent conventions with types that match Alan's actual notes.

### Types

| Type | Purpose |
|---|---|
| **Quote** | A single attributed quote |
| **Story-Scout** | Slugs weekly story curation (5 ranked candidates) |
| **Coaching-Session** | Coaching session record per client |
| **Media-Analysis** | Industry analysis, strategy, journalism research |
| **Aviation-Reference** | Flight training, POH, regulations |
| **Meeting-Note** | Call or meeting notes |
| **Grant-Radar** | Grant opportunity tracking |
| **Project-Note** | Business planning, strategy documents |
| **Personal-Note** | Journal, reflections, diary |
| **Topic** | Area of interest or conceptual lens |
| **Person** | A real-world person or agent |
| **Project** | Bounded effort with an output (Portent) |
| **Operation** | Recurring work, one sitting (Portent) |

### Relationships

- **`belongs_to`** — primary context or parent
- **`related_to`** — secondary association without ownership

### Lifecycle

- **Captured** — recorded but not yet structured
- **Organized** — typed, linked, retrievable
- **Archived** — searchable but hidden from active views

## Migration

Migrated from Bear (1,016 files) using `migrate.py`. Bear inline `#tags` are extracted to YAML frontmatter. No metadata was lost since Bear exports none.

## For Agent Use

See `AGENTS.md` for the protocol this agent follows when creating or editing vault notes.
