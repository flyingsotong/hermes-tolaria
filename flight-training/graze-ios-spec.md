# Graze — iOS spec

## Context

I write my notes in Markdown. They live in a git repo — `flyingsotong/hermes-tolaria`. That's 1,000+ notes: coaching sessions, aviation references, media analysis, personal writing. Git is the source of truth. It's portable. It has history. It's not going anywhere.

The problem: reading these notes on an iPhone is a kludge. GitHub Mobile renders markdown but won't search inside files. Working Copy does git properly but shows raw markdown. Obsidian needs a sync plugin. Bear — the app I actually enjoy reading in — is a walled garden with no git awareness.

I want one app that does what Bear does for reading (beautiful typography, dark sidebar, folder navigation, full-text search) but sources its content from a git repo instead of a proprietary database. No sync dashboard. No cloud service. The repo IS the database.

Graze is that app. Read-only for v1. If it works well, I ship it to the App Store. Editing and two-way sync come in v2.

The spec below is written to be fed to an LLM (Deepseek on my Mac) to build as a native SwiftUI app. It covers architecture, UI design, data models, git integration, search, rendering, and every edge case I can think of.

## What this is

A **read-only Bear clone that reads off a GitHub repo.** The goal: beautiful markdown reading on iPhone, sourced from a git repo. Zero sync dashboard. Zero proprietary cloud. The repo is the database. Start with reading (v1); editing can follow (v2).

Name: **Graze**. Short, verb-ish, no vowels-as-service-naming. Implies browsing/skimming — which is the primary use case.

---

## Product scope

### v1 — Reader (App Store target)

- Clone a GitHub repo, read all `.md` files rendered like Bear
- Browse notes by folder structure (sidebar)
- Full-text search across all notes
- Offline — everything cloned locally, works without network
- Pull-to-refresh = `git pull`
- Bookmark/favorite notes
- Dark/light mode
- Open any public repo by URL
- Private repo support (GitHub PAT via Settings → access token)
- No editing. No creating notes. No writing back.

### v2 — Editor (future)

- Edit notes in-place
- Commit and push changes back to the repo
- Create new notes
- Two-way sync with conflict resolution
- iCloud backup of local state

### v2.5+ — Author platform

- Multi-repo support (pin 3-5 repos, swipe between them)
- Share sheet → save web content as markdown note
- Custom repo (not just GitHub — GitLab, Codeberg, self-hosted)
- Apple Intelligence integration (summarize notes, find related)

---

## Architecture

### Pattern: MVVM + repository pattern

```
┌────────────────────────────────────────┐
│ SwiftUI Views                           │
│  ├── ContentView (split nav)           │
│  ├── FolderSidebar                      │
│  ├── NoteList                           │
│  ├── NoteReader                         │
│  ├── SearchView                         │
│  └── SettingsView                       │
├────────────────────────────────────────┤
│ ViewModels                              │
│  ├── RepoViewModel (clone, pull, index) │
│  ├── NotesViewModel (list, search)      │
│  ├── ReaderViewModel (render, cache)    │
│  └── SettingsViewModel                  │
├────────────────────────────────────────┤
│ Services                                │
│  ├── GitService (clone, pull, status)   │
│  ├── IndexService (scan, parse, FTS)    │
│  ├── RenderService (markdown → AttrStr) │
│  └── CacheService (pre-rendered notes)  │
├────────────────────────────────────────┤
│ Data Store                              │
│  ├── SwiftData models (metadata index)  │
│  └── FileManager (raw .md on disk)      │
└────────────────────────────────────────┘
```

### Key design decisions

**Why clone to disk instead of API-only?** Offline reading. GitHub API paginates, rate-limits, and doesn't give you content search. A local clone is instant and works on a plane.

**Why SwiftData for metadata and FileManager for content?** Notes can be huge (hundreds of KB of markdown). SwiftData doesn't handle large text well. Store metadata (title, path, modified date, frontmatter) in SwiftData; store raw content on disk. Render on demand.

**Why not Core Data?** SwiftData is the modern SwiftUI-native persistence layer. For a new app targeting iOS 18+, there's no reason to use Core Data.

---

## UI/UX design spec

### Bear's signature design language (what to copy)

| Element | Bear | Graze |
|---------|------|-------|
| Sidebar | Left panel, dark fill, folder tree | Same. Dark fill (`Color(.systemGroupedBackground)` in dark mode, custom dark gray `#1C1C1E` in light mode) |
| Typography | Custom serif-ish font for reading, SF for UI | System fonts: `.serif` for note body, SF for everything else |
| Note background | Warm off-white with subtle texture | `Color(red: 0.98, green: 0.97, blue: 0.95)` in light mode |
| Note list | Clean rows: title, date, 2-line preview | Same. No thumbnails, no tags-on-row clutter |
| Selected state | Light blue highlight in sidebar | Same. `Color.accentColor.opacity(0.12)` |
| Navigation | Three-column on iPad, stack on iPhone | Same via `NavigationSplitView` |
| Search bar | Minimal, blends into nav bar | `.searchable()` modifier, scoped to current folder or all notes |
| Markdown rendering | Clean, unthemed, no GitHub-style boxing | Same. Inline code uses subtle gray background — never a full-width block background |
| Link handling | Tappable, opens in in-app Safari | `.environment(\.openURL, OpenURLAction { … })` → `SFSafariViewController` |
| Images | Rendered inline from `![alt](path)` | Load from cloned repo's file tree. Lazy. Respect viewport width |
| Empty state | Gentle, not empty-box-with-ghost-icon | "No notes yet. Pull to refresh." in subtitle gray |

### Screen-by-screen breakdown

#### 1. Onboarding (first launch only)

Single-screen, no carousel, no account creation.

- Title: "Graze"
- Subtitle: "Read your Markdown notes from any GitHub repo"
- Text field: repo URL (placeholder: `flyingsotong/hermes-tolaria`)
- Toggle: "Private repo" → shows access token field
- Button: "Clone"
- Progress indicator during clone
- No sign-in. No email. No cloud. Just a repo URL.

#### 2. ContentView — main interface

**iPhone (compact):**
```
┌─────────────────────┐
│ [< Back]  Folder ▾   │  ← NavigationStack. Title = current folder
│         [🔍]         │
├─────────────────────┤
│ Note List            │
│ ┌──────────────────┐ │
│ │ Readme           │ │  ← Filename without .md
│ │ 2 lines preview… │ │
│ ├──────────────────┤ │
│ │ Ground School    │ │
│ │ 2 lines preview… │ │
│ ├──────────────────┤ │
│ │ Practice Exam    │ │
│ │ 2 lines preview… │ │
│ └──────────────────┘ │
└─────────────────────┘
        ↓ tap note
┌─────────────────────┐
│ [< flight-training]  │  ← Back to folder list
├─────────────────────┤
│ Rendered markdown   │  ← ScrollView, full typography
│                     │
│ # Heading           │
│                     │
│ Body text here…     │
└─────────────────────┘
```

**iPad (regular):**
```
┌──────┬──────────────────────────────────┐
│Sidebar│ Note List        │ Note Reader   │
│      │                  │               │
│ flight│ Study Roadmap   │ # XC Study    │
│  -xc/│ Ground School   │               │
│ notes│ Practice Exam   │ Full text     │
│      │ VFRG Extracts   │ here…         │
│      │                  │               │
└──────┴──────────────────┴───────────────┘
```

Sidebar folders come from the repo's directory structure. Only show folders that contain `.md` files. Sort folders first, then loose `.md` files, alphabetically.

#### 3. Reader view

This is the whole point of the app. Gets the most attention.

**Typography scale:**
- H1: 28pt, bold, `system(.serif)`
- H2: 22pt, semibold
- H3: 18pt, medium
- Body: 17pt, regular
- Code: 15pt, `system(.monospaced)`, background `#F5F5F5` (light) / `#2C2C2E` (dark), padding 4pt, corner radius 4pt
- Blockquotes: 17pt, italic, left border 3pt `Color.accentColor`, padding 12pt left, subtle gray fill
- Lists: native indentation, bullet = `•` at 17pt

**Reader chrome (toolbar, visible on scroll-up, hidden on scroll-down):**
- Back button (left)
- Note title (center, truncates)
- Bookmark toggle (right, filled star if bookmarked)
- Share button (right, standard iOS share sheet → exports rendered note as PDF/Markdown)

**Swipe gestures on reader:**
- Swipe right from left edge → back (standard iOS)
- Swipe left → next note (if navigated from list)
- Pinch to adjust text size (persists per-user in `@AppStorage`)

#### 4. Search

Activated from the `.searchable()` modifier.

- Searches note titles AND body content
- Results ranked: title match > heading match > body match
- Shows folder path in result subtitle
- Tapping a result opens that note in the reader
- Search scope: current folder / all notes (segmented control under search bar)

Implementation: full-text search via SQLite FTS5 on a local `content` table. Build the FTS index on clone and update incrementally on pull.

#### 5. Settings

- Repo URL (changeable, triggers re-clone)
- Access token (for private repos)
- Text size: Aa slider (default: 17pt, range: 13-24pt)
- Font: Serif / Sans-serif
- Appearance: System / Light / Dark
- Pull on launch: toggle
- Bookmarked notes count → tappable to see list
- Clear cache
- Version, credits, GitHub link

---

## Data model

### SwiftData schema

```swift
@Model
final class RepoConfig {
    var url: String              // "flyingsotong/hermes-tolaria"
    var localPath: String        // /Documents/repos/hermes-tolaria
    var accessToken: String?     // GitHub PAT, stored in Keychain not SwiftData
    var lastPulledAt: Date?
    var cloneStatus: CloneStatus // .idle, .cloning, .ready, .failed
}

@Model
final class NoteMetadata {
    var title: String            // First H1, or filename without .md
    var fileName: String         // "x-country-navigation-2.md"
    var relativePath: String     // "flight-training/xc/"
    var modifiedAt: Date         // From git log / file mtime
    var preview: String          // First 140 chars of body (strip markdown)
    var wordCount: Int
    var frontmatter: [String: String]? // YAML frontmatter parsed to dict
    var isBookmarked: Bool
    var lastOpenedAt: Date?
}

enum CloneStatus: Codable {
    case idle
    case cloning(progress: Double)  // 0.0...1.0
    case ready
    case failed(String)            // Error message
}
```

### Frontmatter parsing

Many notes have YAML frontmatter (e.g. Tolaria notes with `type`, `tags`, `related_to`). Parse this and surface:

- **Title**: If frontmatter has `title`, use it. Otherwise use the first H1.
- **Tags**: Show as subtle chips at the top of the reader view
- **Type**: Show as a badge (e.g. "Aviation-Reference") in the note list row

---

## Git integration

### Library: SwiftGit2

[SwiftGit2](https://github.com/SwiftGit2/SwiftGit2) is a Swift wrapper around libgit2. More modern than ObjectiveGit. Actively maintained.

### Operations

**Clone:**
```swift
let repo = try Repository.clone(
    from: URL(string: "https://github.com/\(owner)/\(name).git")!,
    to: localURL,
    credentials: credentials  // nil for public, PAT for private
)
```

Progress callback → updates `CloneStatus.cloning(progress)` → shown in UI as progress bar.

**Pull:**
```swift
let remote = try repo.remote(named: "origin")
try repo.fetch(remote: remote, credentials: credentials)
let localBranch = try repo.localBranch(named: "main")
let remoteBranch = try repo.remoteBranch(named: "origin/main")
try repo.merge(remoteBranch, into: localBranch)
```

Pull on: app launch (if `pullOnLaunch` toggle is on), manual pull-to-refresh in note list, background refresh (BGAppRefreshTask, iOS-scheduled, not guaranteed).

**Conflict handling (v1):**
- If `git pull` results in a merge conflict → abort merge, `git reset --hard HEAD`, show banner "Pull failed — local changes detected. Tap to reset." Since v1 is read-only, there are no local changes to lose — reset is always safe.

### Indexing after pull

After clone or pull:
1. Walk the repo directory for all `.md` files (exclude `.git/`, hidden dirs)
2. Diff against existing SwiftData index (by relativePath + modifiedAt)
3. New files: parse, insert metadata, index body in FTS5
4. Modified files: update metadata, re-index
5. Deleted files: remove from SwiftData + FTS5

---

## Search architecture

### SQLite FTS5 (lightweight, built into iOS)

On clone/first index, create an FTS5 virtual table:

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS note_content USING fts5(
    relative_path UNINDEXED,
    title,
    body,
    content='note_metadata',
    content_rowid='rowid'
);
```

FTS5 supports: prefix queries (`xc*`), phrase queries (`"cross country"`), boolean (`fuel AND weather NOT radio`). All standard search bar patterns.

### Search flow

1. User types in `.searchable()` field
2. `.debounce(for: .milliseconds(300))` before querying
3. Query FTS5 with `MATCH` + `snippet()` for result highlights
4. Return ranked list: title match first (higher weight), then body match
5. Display: title (bold, with highlight), snippet (with `**` around match), folder path

---

## Rendering

### Markdown → AttributedString

Use `MarkdownUI` (SwiftUI-native, actively maintained) for initial rendering. Fallback: native `AttributedString(markdown:)` from iOS 18 for simpler notes.

For v1, `MarkdownUI` is the pragmatic choice:
- Handles all CommonMark (headings, lists, code blocks, tables, blockquotes, links, images)
- Themeable — we define a `BearTheme` that matches the typography spec above
- Handles image loading from local file paths (key for repos with `attachments/` folders)

**Image loading:** When markdown contains `![](attachments/diagram.png)`, resolve relative to the cloned repo root. That is: `\(repo.localPath)/\(note.relativePath)/attachments/diagram.png`. Load asynchronously, show placeholder while loading.

### Pre-rendering cache

Rendering large notes can be slow. On first open, render to `AttributedString` and cache in `NSCache` keyed by `relativePath + modifiedAt`. Subsequent opens are instant.

---

## Offline architecture

- Full repo is cloned locally. All notes are on disk.
- No network needed for reading, searching, or browsing.
- Pull-to-refresh is the only network operation.
- If no network during pull: show "No connection" banner (not a blocking alert)

---

## File structure (Xcode project)

```
Graze/
├── GrazeApp.swift                    // @main, app delegate
├── ContentView.swift                 // Split navigation host
├── Models/
│   ├── RepoConfig.swift              // SwiftData model
│   ├── NoteMetadata.swift            // SwiftData model
│   └── CloneStatus.swift             // Enum
├── ViewModels/
│   ├── RepoViewModel.swift           // Clone, pull, status
│   ├── NotesViewModel.swift          // List, search, index
│   └── ReaderViewModel.swift         // Render, cache, bookmark
├── Views/
│   ├── Onboarding/
│   │   └── RepoSetupView.swift
│   ├── Sidebar/
│   │   └── FolderSidebar.swift
│   ├── Notes/
│   │   ├── NoteListView.swift
│   │   └── NoteRowView.swift
│   ├── Reader/
│   │   ├── NoteReaderView.swift
│   │   └── ReaderToolbar.swift
│   ├── Search/
│   │   └── SearchResultsView.swift
│   └── Settings/
│       └── SettingsView.swift
├── Services/
│   ├── GitService.swift              // Clone, pull, status via SwiftGit2
│   ├── IndexService.swift            // Scan .md files, parse metadata
│   ├── FTSService.swift              // SQLite FTS5 wrapper
│   ├── RenderService.swift           // Markdown → AttributedString
│   └── CacheService.swift            // NSCache wrapper
├── Utilities/
│   ├── KeychainHelper.swift          // Secure PAT storage
│   ├── FrontmatterParser.swift       // YAML → Dict
│   └── FileTreeWalker.swift          // Recursive .md discoverer
└── Resources/
    ├── Assets.xcassets
    └── Graze.intentdefinition        // Siri Shortcuts (v2)
```

---

## Key Swift packages

| Package | Purpose | Why |
|---------|---------|-----|
| [SwiftGit2](https://github.com/SwiftGit2/SwiftGit2) | Git operations | Swift-native libgit2 wrapper. Clone, pull, status |
| [MarkdownUI](https://github.com/gonzalezreal/swift-markdown-ui) | Markdown rendering | SwiftUI-native, themeable, handles images |
| [Yams](https://github.com/jpsim/Yams) | YAML parsing | For frontmatter. libYAML under the hood, fast |
| Nothing else | Keep it lean | No analytics, no crash reporting, no network layer beyond git |

---

## App Store considerations

### What Apple wants

- **No web-wrapper feel.** Must use native UI. This rules out PWA/WKWebView approaches. SwiftUI all the way.
- **Privacy nutrition label:** Zero data collected. No analytics, no crash reporting, no third-party SDKs. "Data Not Collected" across all categories.
- **No mandatory account.** No sign-in. You can open any public repo without credentials. Private repos need a PAT entered in Settings.
- **Onboarding must be skippable.** Not applicable here — onboarding IS the repo URL field. But it's one screen, then you're reading.

### Privacy manifest

```xml
<!-- PrivacyInfo.xcprivacy -->
<key>NSPrivacyTracking</key>
<false/>
<key>NSPrivacyCollectedDataTypes</key>
<array/>  <!-- Empty: nothing collected -->
<key>NSPrivacyAccessedAPITypes</key>
<array>
    <!-- File timestamp APIs: used for checking .md file modification times -->
    <dict>
        <key>NSPrivacyAccessedAPIType</key>
        <string>NSPrivacyAccessedAPICategoryFileTimestamp</string>
        <key>NSPrivacyAccessedAPITypeReasons</key>
        <array>
            <string>0A2A.1</string>  <!-- Accessing file timestamps within the app's own container -->
        </array>
    </dict>
</array>
```

### Screenshots

Show the app with a **real repo full of well-written notes.** Do not ship screenshots with lorem ipsum. The whole value prop is "beautiful markdown from YOUR notes." Use the Tolaria repo as the demo content — it has hundreds of notes, multiple folders, diverse content types. Choose 3-4 visually rich notes (headings, lists, code blocks, images) for the screenshots.

---

## Edge cases and pitfalls

### Repo size
- A repo with 10,000+ `.md` files will be slow to clone and index
- Show progress during clone and during initial index (separate steps)
- First index: scan all files, create FTS5 index. Show "Indexing… (1,243/5,000)" progress
- After first index: incremental (diff-based, fast)

### Binary files
- Ignore: images are loaded lazily on render, not pre-cached
- PDFs/audio/video: show as tappable link, opens in ShareSheet → Files/Preview

### Non-markdown files
- Ignore everything that isn't `.md`
- `.Rmd` (R Markdown), `.mdx` (MDX): not supported in v1. Track as feature request

### Frontmatter edge cases
- Malformed YAML: skip frontmatter, use filename as title
- `title` field is `""`, skip it, fall back to first H1
- No H1 in body: use filename without `.md`

### Git edge cases
- Repo URL is wrong: show "Repository not found" error with link to GitHub
- Private repo, no token: show "Authentication required" with link to Settings
- Token expired/revoked: show "Token invalid. Update in Settings." banner
- Repo has no `.md` files: show "No Markdown notes found in this repo" empty state
- Repo uses `master` instead of `main`: detect default branch from remote
- Submodules: skip them (don't recurse). Warn if detected.
- Very large repo (5GB+): warn before cloning. Offer shallow clone option (`--depth 1`).

### Network
- Cloning on cellular: warn if on cellular data (iOS API: `CTTelephonyNetworkInfo`)
- No network at launch: show cached notes (last pulled state). Banner: "Offline — showing notes from [date]"
- Background pull fails: retry once, then silently skip. Don't alert.

### iOS-specific
- Background pull: `BGAppRefreshTaskRequest` can pull and re-index, but iOS may not grant time. Don't rely on it for freshness — pull on launch is the reliable path.
- App termination during clone: resume on next launch. Check `.git/HEAD` existence to detect incomplete clone, delete partial and restart.
- Storage full: `clone()` throws. Catch, show "Not enough storage. Free up space and try again."

### Accessibility
- Dynamic Type: support all sizes. Reader view adjusts text scale with system setting.
- VoiceOver: all navigation elements labeled. Reader view reads content in reading order.
- Reduce motion: disable scroll-hide/show animations on reader toolbar.

---

## What to build first (MVP order)

1. **Repo cloning + file tree** — prove git works, prove notes are on disk
2. **Markdown rendering** — prove a note looks good
3. **Navigation** — folder sidebar + note list + reader flow
4. **Search** — FTS5 index + `.searchable()` UI
5. **Offline + caching** — pull-to-refresh, last-pulled timestamp
6. **Bookmarks** — SwiftData boolean + bookmark list
7. **Settings** — repo URL, token, text size, appearance
8. **Onboarding** — polish the first-launch screen last (once the core works)

---

## Why this wins against alternatives

| Competitor | Reading experience | Git awareness | Offline | Search |
|-----------|-------------------|---------------|---------|--------|
| GitHub Mobile | Good | Yes | No | Filenames only |
| Working Copy | Raw md | Yes | Yes | No |
| Obsidian | Good | No (sync plugin) | Yes | Yes |
| Bear | Excellent | No | Yes | Yes |
| **Graze** | Excellent | **Yes** | Yes | Yes |

The gap is real. No one combines Bear-quality reading with git-native sync. Graze fills it.
