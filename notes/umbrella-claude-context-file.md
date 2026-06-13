---
type: Note
---
# Umbrella: Claude context file

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Umbrella** — a macOS SwiftUI family financial planning app for the Osoonovan family. The app is in `PathwayApp/` and targets macOS 14+. Bundle ID: `com.alansoon.umbrella`.

There is also a legacy Next.js web app at the repo root (TypeScript/Node.js) that shares the same SQLite database file but is no longer the primary interface.

## Build & Run

```bash
cd PathwayApp
xcodebuild -project Umbrella.xcodeproj -scheme Umbrella -configuration Debug -destination 'platform=macOS' build
```

To run, open `Umbrella.xcodeproj` in Xcode and press Cmd+R, or launch the built `.app` from DerivedData:
```
~/Library/Developer/Xcode/DerivedData/Umbrella-*/Build/Products/Debug/Umbrella.app
```

There are no tests, no linter, and no separate build scripts.

## Architecture

### Data layer

`AppDatabase.swift` is a singleton (`AppDatabase.shared`) that owns the SQLite connection via GRDB. It auto-runs migrations on launch and exposes typed read/write methods. Views call it directly — there is no intermediate repository or ViewModel layer.

**Database location** (resolved in priority order):
1\. `$PATHWAY_DB_PATH` env var (dev override)
2\. iCloud Drive: `~/Library/Mobile Documents/com~apple~CloudDocs/Umbrella/pathway.db`
3\. Walk up from bundle (Xcode dev mode)
4\. `~/Documents/Pathway/pathway.db`

### Schema (shared with Next.js web app)

| Table | Purpose |
|---|---|
| `people` | Family members — role is `self`, `spouse`, or `dependent` |
| `asset_accounts` | Accounts with type and per-account assumed return % |
| `asset_snapshots` | Time-series values — one row per account per date |
| `income_streams` | Active/inactive income sources with growth rates |
| `scenarios` | Forecast assumptions (spend, inflation, conservative/base/optimistic return rates) |

Asset types: `cash`, `unit_trust`, `stock`, `property`, `cpf_oa`, `cpf_sa`, `cpf_ma`, `cpf_ra`, `pension`, `other`. CPF types have `.isCPF` and property has `.isProperty` computed flags on `AssetType`.

### Forecast engine

The entire projection engine lives in `ForecastView.swift` — there is no separate model file for it. Key design:

- **`project()`** — takes a starting liquid balance, per-person CPF state structs, and property value, and returns `[ForecastPoint]` for one scenario. Called once per scenario in `recompute()`.
- **Scenarios**: `conservative`, `base`, `optimistic`, `myForecast` (weighted-avg of per-account return %s), `noIncome`, `noIncomeLiquid`
- **CPF model**: OA earns 2.5%, SA/MA earns 4%. At age 55, SA closes and a Retirement Account forms (capped at FRS; property owners only need BRS = FRS/2; excess goes to liquid). At age 65, RA balance converts to CPF LIFE annual payout (~7.5% of RA balance p.a.).
- **YOLO**: binary search (40 iterations, auto-expanding upper bound) for max monthly spend that keeps liquid ≥ 0 by the year the longest-lived adult turns 100. Property is deliberately excluded from the success test.
- **Negative liquid**: carried as flat debt (no investment returns on negative balance) — `max(liquid,0) * (1+r) + min(liquid,0) + netFlow`.

### Theming

`Theme.swift` defines all colours as adaptive `Color` values that switch between dark and light at the OS level using `NSColor(name:dynamicProvider:)`. Never use hardcoded hex colours in views — always use a `Theme.*` value. Key additions beyond the standard palette:

- `Theme.yellowText` — bright yellow on dark, burnt orange (`#C05000`) on light; used for stale-date warnings
- `Theme.bgHighlight` / `Theme.borderHighlight` — for selected/highlighted cards

### Navigation

`ContentView.swift` is a `NavigationSplitView` with a custom sidebar (Cmd+1–5 keyboard shortcuts). The five tabs map to: `DashboardView`, `AssetsView`, `IncomeView`, `ForecastView`, `SettingsView`. Dark/light mode preference is stored in `@AppStorage("prefersDarkMode")`.

### View pattern

All views follow the same pattern: `@State` properties for data, an `.onAppear { load() }` call, and a `@MainActor func load()` that calls `AppDatabase.shared.*` inside a `do/catch`. No Combine, no MVVM, no ObservableObject.

## Key decisions / constraints

- **Singapore-specific**: currency is SGD, CPF modelling follows Singapore retirement account law, FRS 2025 base is S$213,000 growing at 3.5% p.a.
- **My Forecast** blends only liquid account return %s (CPF rates are fixed by law, property appreciation is a market fact — neither should be user-adjustable in the forecast blend).
- **Property in forecast**: controlled by `includeProperty` UI toggle for normal scenarios; YOLO always excludes property from its success test (`liquidOnly: true`).
- **No live data**: all account values are manual snapshots. Staleness is flagged visually (>60 days = burnt orange, >90 days = red).
- The app seeds 4 family members on first launch (`v1_seed_family` migration). Do not remove or rename these rows — other data references them by ID.