---
type: Note
_icon: terminal
_color: magenta
_sidebar_label: Magenta Theme Pipeline
---

# Magenta theme pipeline setup — June 2026

Magenta Debrief runs on managed Ghost (Synaps Media). The theme is a custom Casper-derived Handlebars theme at `github.com/flyingsotong/magenta-theme` (private repo). Previously developed via Antigravity (Gemini AI) on MacBook — zipped on Mac, uploaded manually to Ghost Admin.

## New pipeline (Hermes agent on VPS)

| Step | What |
|------|------|
| 1 | Hermes agent edits theme files at `/root/workspace/magenta-theme/` on VPS |
| 2 | Changes pushed to `git@github.com:flyingsotong/magenta-theme.git` via SSH deploy key |
| 3 | Agent zips the theme: `zip -r theme.zip . -x ".*" -x "__MACOSX/*"` |
| 4 | Agent uploads to Ghost Admin API: `POST /ghost/api/admin/themes/upload/` with field `file` |
| 5 | Ghost validates and activates the theme — site goes live |

## Keys and access

- **SSH deploy key** at `/root/.ssh/theme-deploy-key` — added to GitHub repo as deploy key with write access
- **Ghost Content API key** in `/root/.env` as `GHOST_CONTENT_KEY`
- **Ghost Admin API key** in `/root/.env` as `GHOST_ADMIN_KEY` — from Ghost Admin > Settings > Integrations > Theme Bot
- Admin API auth: JWT signed with hex-decoded secret, audience `/admin/`, expiry 300s, header `Authorization: Ghost {token}`

## Critical gotchas (from experience)

1. **`.claude` directory** silently breaks Ghost zip validation. Always exclude dotfiles from zip
2. **`{{asset}}` whitespace** — a stray space like `{{asset " css/screen.css"}}` causes 404 on stylesheet
3. **Handlebars comments** cannot wrap block helpers — delete lines outright instead of `{{!-- {{#get}}...{{/get}} --}}`
4. **Ghost caches** — after tag changes, re-save post in Ghost Admin to invalidate page cache

## Theme design system

Swiss Typographic — stark, high-contrast, data-heavy. Inter font (400/500/700/800/900). NO drop shadows, NO rounded corners, NO dashboard/cockpit aesthetic. Color palette: Canvas #f8fafc, Ink #0f172a, Accent #c026d3, Muted #475569. All CSS in screen.css (no inline `<style>` since v2.5.5).

## Status

- [x] Git access (SSH deploy key)
- [x] Ghost Admin API key
- [x] Upload endpoint verified (200 OK with field `file`)
- [x] Repo cloned at `/root/workspace/magenta-theme/`

Last updated: 22 June 2026
