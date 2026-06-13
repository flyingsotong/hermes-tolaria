---
type: Type
_icon: compass
_color: blue
_sidebar_label: Story Scouts
_order: 20
_pinned_properties:
  - scout_date
  - recommendation
---

# Story-Scout

A weekly Slugs story curation with five ranked candidates. Each candidate is assessed against rupture strength, cross-industry freshness, generalizability, and source quality.

## Properties

- **scout_date**: Date of the scout session (e.g. 2026-04-11)
- **recommendation**: Which candidate is the essay pick and why

## Suggested

- `belongs_to` — the Slugs newsletter (when published)
- `related_to` — topics, trends, or people referenced
