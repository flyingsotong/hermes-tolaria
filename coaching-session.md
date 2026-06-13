---
type: Type
_icon: users
_color: green
_sidebar_label: Coaching
_order: 30
_pinned_properties:
  - client
  - session_date
---

# Coaching-Session

A coaching session record — client observations, coach reflections, and ICF-relevant notes.

## Properties

- **client**: The person being coached
- **session_date**: Date of the session
- **status**: Active, Paused, Completed

## Suggested

- `belongs_to` — a coaching engagement or responsibility
- `related_to` — topics, frameworks, or readings referenced
