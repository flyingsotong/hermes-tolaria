#!/usr/bin/env python3
"""Extract dates from note bodies and filenames into frontmatter."""

import re
import os
from pathlib import Path
from datetime import datetime

NOTES_DIR = Path("notes")

DATE_PATTERNS = [
    (r'\*\*(\w+ \d{1,2},? \d{4})\*\*', ["%B %d, %Y", "%B %d %Y"]),
    (r'\*\*(\w+ \d{1,2})\*\*,? (\d{4})', ["%B %d %Y"]),
    (r'\*\*(\d{1,2} \w+ \d{4})\*\*', ["%d %B %Y"]),
    (r'(?:^|\n)(\w+, \w+ \d{1,2}(?:th|nd|st|rd)?,? \d{4})', ["%A, %B %d, %Y", "%A %B %d, %Y", "%a, %B %d, %Y"]),
    (r'(?:^|\n)(\w+ \d{1,2}(?:th|nd|st|rd)?,? \d{4})', ["%B %d, %Y", "%B %d %Y"]),
]

MONTHS = r'(january|february|march|april|may|june|july|august|september|october|november|december)'

def parse_date(text):
    """Try to parse a date string from body text."""
    for pattern, fmts in DATE_PATTERNS:
        m = re.search(pattern, text, re.IGNORECASE)
        if not m:
            continue
        if m.lastindex == 2:
            date_str = f"{m.group(1).strip()} {m.group(2).strip()}"
        else:
            date_str = m.group(1).strip()
        # Clean ordinal suffixes
        date_str = re.sub(r'(\d+)(th|nd|st|rd)', r'\1', date_str)
        for fmt in fmts:
            try:
                return datetime.strptime(date_str, fmt).strftime("%Y-%m-%d")
            except ValueError:
                continue
    return None


def filename_date(name):
    """Try to extract a date from the filename slug."""
    name = name.replace('-', ' ').lower()
    # Full month name patterns
    m = re.search(rf'({MONTHS}) (\d{{1,2}}),? (\d{{4}})', name)
    if m:
        try:
            return datetime.strptime(f"{m.group(1)} {m.group(2)} {m.group(3)}", "%B %d %Y").strftime("%Y-%m-%d")
        except ValueError:
            pass
    # ISO-style dates (2026-04-11)
    m = re.search(r'(\d{4})-(\d{1,2})-(\d{1,2})', name)
    if m:
        try:
            d = datetime(int(m.group(1)), int(m.group(2)), int(m.group(3)))
            if 2020 <= d.year <= 2027:
                return d.strftime("%Y-%m-%d")
        except ValueError:
            pass
    return None


def parse_frontmatter(text):
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        return {}, text
    end_idx = -1
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end_idx = i
            break
    if end_idx == -1:
        return {}, text
    fm = {}
    current_key = None
    for line in lines[1:end_idx]:
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("- ") and current_key:
            if isinstance(fm.get(current_key), list):
                fm[current_key].append(stripped[2:])
            else:
                fm[current_key] = [stripped[2:]]
            continue
        if ":" in stripped:
            parts = stripped.split(":", 1)
            current_key = parts[0].strip()
            val = parts[1].strip()
            if val:
                fm[current_key] = val
    body = "\n".join(lines[end_idx+1:])
    return fm, body


def serialize_frontmatter(fm):
    lines = ["---"]
    for key, val in fm.items():
        if isinstance(val, list):
            lines.append(f"{key}:")
            for item in val:
                lines.append(f"  - {item}")
        else:
            lines.append(f"{key}: {val}")
    lines.append("---")
    return "\n".join(lines)


added = 0
for f in sorted(NOTES_DIR.glob("*.md")):
    with open(f) as fh:
        text = fh.read()
    
    fm, body = parse_frontmatter(text)
    
    # Skip if already has a date field
    if any(k in fm for k in ["date", "session_date", "scout_date", "radar_date"]):
        continue
    
    # Try body first
    d = parse_date(body)
    if not d:
        d = filename_date(f.stem)
    if not d:
        continue
    
    # Determine which date field based on type
    t = fm.get("type", "")
    if t == "Coaching-Session":
        fm["session_date"] = d
    elif t == "Story-Scout":
        fm["scout_date"] = d
    elif t == "Grant-Radar":
        fm["radar_date"] = d
    else:
        fm["date"] = d
    
    output = serialize_frontmatter(fm) + "\n" + body
    with open(f, "w") as fh:
        fh.write(output)
    
    added += 1
    if added <= 5:
        print(f"  {f.name}: {d}")

print(f"\nAdded dates to {added} notes")
