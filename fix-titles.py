#!/usr/bin/env python3
"""
Repair: add H1 titles back to notes. The migration script extracted
the H1 from Bear files but never wrote it into the output.
"""

import os
import re
from pathlib import Path

BEAR_DIR = Path("/root/workspace/hermes-tolaria")
NOTES_DIR = Path("/root/workspace/hermes-tolaria-vault/notes")


def bear_title(filepath):
    """Extract H1 from a Bear .md file."""
    try:
        with open(filepath) as f:
            first = f.readline().strip()
        if first.startswith("# "):
            return first
    except Exception:
        pass
    return None


def slug_from_bear_name(name):
    """Replicate migrate.py's slug logic."""
    lower = name.lower()
    title = Path(name).stem
    slug = re.sub(r'[^\w\s-]', '', title.lower())
    slug = re.sub(r'[-\s]+', '-', slug).strip('-')
    if len(slug) > 80:
        slug = slug[:80].rstrip('-')
    return slug


def parse_frontmatter(text):
    """Parse YAML frontmatter."""
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
    
    frontmatter = {}
    current_key = None
    current_list = []
    
    for line in lines[1:end_idx]:
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("- ") and current_key:
            current_list.append(stripped[2:].strip())
            frontmatter[current_key] = current_list
            continue
        if ":" in stripped and not stripped.startswith("-"):
            if current_key and current_list:
                frontmatter[current_key] = current_list
                current_list = []
            parts = stripped.split(":", 1)
            current_key = parts[0].strip()
            val = parts[1].strip()
            if val:
                frontmatter[current_key] = val
            else:
                current_list = []
    
    if current_key and current_list:
        frontmatter[current_key] = current_list
    
    body = "\n".join(lines[end_idx+1:])
    return frontmatter, body


# Build index: bear slug → bear h1
bear_map = {}
for f in sorted(BEAR_DIR.glob("*.md")):
    if f.name == "README.md":
        continue
    slug = slug_from_bear_name(f.name)
    h1 = bear_title(f)
    if h1 and slug:
        bear_map[slug] = h1
        # Also store full name for fallback matching
        bear_map[f.name.lower().replace('.md','')[:80]] = h1

print(f"Bear files indexed: {len(bear_map)}")

fixed = 0
skipped = 0
multi_h1_bear = 0

for note_file in sorted(NOTES_DIR.glob("*.md")):
    with open(note_file) as f:
        text = f.read()
    
    fm, body = parse_frontmatter(text)
    
    # Check if body already has an H1
    first_line = body.strip().split("\n")[0] if body.strip() else ""
    if first_line.startswith("# "):
        skipped += 1
        continue
    
    # Try to find matching Bear title
    slug = note_file.stem
    title = None
    
    # Direct match by slug
    if slug in bear_map:
        title = bear_map[slug]
    else:
        # Try prefix matching
        for bs, bt in bear_map.items():
            if slug.startswith(bs) or bs.startswith(slug):
                title = bt
                break
    
    if not title:
        # Fallback: reconstruct from filename
        name = note_file.stem.replace('-', ' ').title()
        # Handle coaching notes specially
        if fm.get("client"):
            name = f"Coaching - {fm['client']}"
        elif fm.get("type") == "Story-Scout" and fm.get("scout_date"):
            name = f"Slugs Story Scout — {fm['scout_date']}"
        elif fm.get("type") == "Grant-Radar":
            name = f"Grant Radar — {note_file.stem}"
        title = f"# {name}"
    
    # Prepend H1 to body
    new_body = title + "\n" + body
    new_text = text[:text.index("---", 2)+3] + "\n" + new_body
    
    with open(note_file, "w") as f:
        f.write(new_text)
    
    fixed += 1
    if fixed <= 5:
        print(f"  {note_file.name}: {title}")

print(f"\nFixed: {fixed} notes, Already had H1: {skipped}")
