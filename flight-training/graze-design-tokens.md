# Graze — Design tokens (from Hermes WebUI Reader theme)

## Source

These tokens are extracted from the Hermes Agent WebUI "Reader" theme that Alan uses daily (`~/.hermes/dashboard-themes/reader.yaml`). The theme prioritizes: readability, no visual noise, comfortable density. Everything here maps directly to SwiftUI/CSS values.

## Palette

```swift
// Asset catalog color set — define these as named colors

extension Color {
    // Canvas — the deepest background
    static let grazeBackground   = Color(hex: "#0d1117")  // GitHub dark
    static let grazeBackgroundRGB = (0.051, 0.067, 0.090) // for UIColor
    
    // Surface — cards, sidebar, elevated areas
    static let grazeSurface      = Color(white: 1.0, opacity: 0.03)  // rgba(255,255,255,0.03)
    static let grazeSurfaceHover = Color(white: 1.0, opacity: 0.06)
    
    // Text
    static let grazeTextPrimary   = Color(hex: "#d4d4d4")
    static let grazeTextSecondary = Color(hex: "#8b949e")  // GitHub muted
    static let grazeTextTertiary  = Color(hex: "#6e7681")
    
    // Borders
    static let grazeBorder        = Color(white: 1.0, opacity: 0.06)
    static let grazeBorderStrong  = Color(white: 1.0, opacity: 0.10)
    
    // Accent — unchanged from Hermes default
    // The WebUI uses a teal/blue accent. For Graze, use system accent
    // or a warm subtle blue: #58a6ff (GitHub link blue)
    static let grazeAccent        = Color(hex: "#58a6ff")
    
    // Code blocks
    static let grazeCodeBackground = Color(white: 1.0, opacity: 0.05)
    static let grazeCodeText       = Color(hex: "#e6edf3")
    
    // Blockquotes
    static let grazeBlockquoteBackground = Color(white: 1.0, opacity: 0.02)
    static let grazeBlockquoteBorder     = Color(hex: "#58a6ff")
    
    // Warm glow vignette — extremely subtle
    // In the WebUI this is a radial gradient overlay
    // For iOS: skip this. It's a web-specific effect.
}
```

## Typography

```swift
// Font definitions for SwiftUI

extension Font {
    // iOS system fonts map to the same stack as WebUI's system-ui
    
    static let grazeTitle    = Font.system(.title, design: .default).weight(.bold)
    // ~28pt on iOS, equivalent to WebUI H1
    
    static let grazeHeading  = Font.system(.title2, design: .default).weight(.semibold)
    // ~22pt, WebUI H2
    
    static let grazeSubhead  = Font.system(.title3, design: .default).weight(.medium)
    // ~18pt, WebUI H3
    
    static let grazeBody     = Font.system(.body, design: .default)
    // 17pt — matches WebUI baseSize: "17px"
    
    static let grazeBodyMono = Font.system(.body, design: .monospaced)
    // 17pt mono — for inline code and code blocks. WebUI fontMono: ui-monospace
    
    static let grazeCaption  = Font.system(.caption, design: .default)
    // ~12pt, metadata, dates, folder paths
}
```

### Line height

```swift
// SwiftUI doesn't have a direct line-height property.
// Use .lineSpacing() on Text views:

Text(note.body)
    .lineSpacing(4)  // 17 * 1.65 = 28.05, minus default ~24 = ~4pt extra
    
// More precise approach with UIKIt:
// NSAttributedString paragraph style: 
//   lineHeightMultiple = 1.65
//   or minimumLineHeight = 28, maximumLineHeight = 28
```

### Letter spacing

WebUI uses `0` (default). Graze: no override. Use system default tracking.

## Layout & spacing

```swift
enum GrazeSpacing {
    static let xs: CGFloat     = 4
    static let sm: CGFloat     = 8    // 0.5rem — matches WebUI radius
    static let md: CGFloat     = 12
    static let lg: CGFloat     = 16
    static let xl: CGFloat     = 24
    static let xxl: CGFloat    = 32
    
    // Reader content
    static let readerHorizontal: CGFloat = 16   // left/right padding
    static let readerVertical: CGFloat   = 20   // top/bottom padding
    static let paragraphGap: CGFloat     = 12   // between paragraphs
    static let headingTop: CGFloat       = 24   // space before H2/H3
    static let headingBottom: CGFloat    = 8    // space after heading
    
    // Note list
    static let rowHeight: CGFloat        = 64
    static let rowPadding: CGFloat       = 16
    static let previewLines: Int         = 2
}
```

## Corner radius

```swift
extension CGFloat {
    static let grazeRadius: CGFloat = 8  // 0.5rem at default 16px base
    // Use this for cards, code blocks, input fields
    // Never use 0 (square) — too harsh for a reading app
    
    static let grazeRadiusTight: CGFloat = 4  // inline code, small badges
}
```

## Notes on the WebUI aesthetic

### What makes the Reader theme look good:

1. **No noise.** No background images, no grain overlay, no decorative elements. Just color.
2. **Subtle separators.** Borders at 6% white opacity — you barely see them, but the eye registers the division.
3. **High contrast on content, low contrast on chrome.** Text is #d4d4d4 on #0d1117 (contrast ratio ~12:1). Sidebar and toolbar elements are muted.
4. **Dark canvas, not black canvas.** #0d1117 has a hint of blue — it's GitHub's dark color. Pure black (#000000) feels harsh and OLED-crushy.
5. **Comfortable density.** The "comfortable" setting means things have room to breathe. Icons and text aren't crammed.
6. **System fonts.** Nothing decorative. The typography's job is to disappear.
7. **Consistent 0.5rem radius.** Every element with a border has the same radius. Nothing is fully rounded (pill) or fully square.

### What to NOT copy (web-specific, not mobile-appropriate):

- **Warm glow vignette.** This is a CSS radial gradient that creates a subtle spotlight effect in the center of the page. On mobile, the viewport is too small for this to feel intentional — it looks like a screen defect.
- **SVG noise grain.** The WebUI has an optional noise overlay. Even at 0 opacity (Reader theme), this is a web thing. Skip.
- **mix-blend-mode effects.** These only work in CSS compositing. Skip.
- **Hover states.** The WebUI has hover effects on every interactive element. On iOS, use `.onTapGesture` highlights and context menus instead. No hover.

## Dark/light mode

The Reader theme is dark-only. For Graze, support both:

```swift
// Light mode equivalents
extension Color {
    // Light mode overrides (define in asset catalog with light/dark variants)
    static let grazeBackgroundLight  = Color(hex: "#fafafa")  // near-white
    static let grazeTextPrimaryLight = Color(hex: "#1a1a2e")  // near-black
    static let grazeSurfaceLight     = Color(black: 1.0, opacity: 0.03)
    static let grazeBorderLight      = Color(black: 1.0, opacity: 0.08)
}
```

But the default — and the initial App Store screenshots — should be dark mode. It's what Alan uses and what looks distinctive.

## Summary: the 11-word design brief

> Dark (#0d1117), no noise, system fonts at 17px/1.65, comfortable spacing.
