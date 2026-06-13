#!/usr/bin/env python3
"""
Migrate Bear notes export to Tolaria-compatible Markdown with YAML frontmatter.
Prototype: processes Quotes and Story Scouts.

Usage:
  python3 migrate.py <source_dir> <dest_dir>
  python3 migrate.py ../hermes-tolaria/ ./notes/
"""

import re
import os
import sys
import shutil
from datetime import datetime
from pathlib import Path


def extract_frontmatter(text):
    """Extract title (H1) and tags from Bear export."""
    lines = text.split("\n")
    title = ""
    tags = []
    body_start = 0

    # H1 on line 1
    if lines and lines[0].startswith("# "):
        title = lines[0][2:].strip()
        body_start = 1

    # Tags on line 2 (or line 1-3)
    for i in range(min(3, len(lines))):
        line = lines[i].strip()
        found = re.findall(r'(?<!\\)#([\w/-]+)', line)
        if found:
            tags.extend(found)

    # Remove escaped tags from body
    cleaned_lines = []
    for line in lines[body_start:]:
        cleaned_lines.append(re.sub(r'\\#(\w)', r'#\1', line))

    body = "\n".join(cleaned_lines).strip()
    return title, tags, body


def classify_file(filename, tags, title):
    """Determine Tolaria type from filename pattern and tags."""
    lower = filename.lower()

    # Quotes
    if lower.startswith("quotes -"):
        return "Quote"

    # Story scouts
    if "story scout" in lower or "story-scout" in lower:
        return "Story-Scout"

    # Slugs newsletters (published issues, not scouts)
    if lower.startswith("slugs ") and "scout" not in lower:
        return "Media-Analysis"

    # Coaching
    if lower.startswith("coaching -"):
        if "email" in lower or "contract" in lower or "brief" in lower:
            return "Project-Note"
        return "Coaching-Session"

    # Grant radar
    if "radar" in lower and ("grant" in lower or "skillsfuture" in lower or "caas" in lower):
        return "Grant-Radar"

    # Aviation / flight
    if any(t in tags for t in ["flight", "flight-training", "flying", "aviation"]):
        return "Aviation-Reference"
    if any(kw in lower for kw in ["flight", "aviation", "pilot", "aircraft", "engine", "aeroviation",
                                   "circuit", "engine", "radio call", "ctaf", "right of way",
                                   "altimeter", "cloud cover", "vmc", "v-speed", "squawk",
                                   "taf ", "metar", "check ", "checks ", "poh", "rpl ", "rpc ",
                                   "raaus", "casa", "atc ", "ga aircraft", "msl", "agv"]):
        return "Aviation-Reference"

    # RAAus / CASA exam notes
    if any(kw in lower for kw in ["raaus", "casa", "rpl", "rpc", "uapl", "uabto"]):
        return "Aviation-Reference"

    # Drone
    if any(kw in lower for kw in ["drone", "dronefly", "uav", "uas", "caas"]):
        return "Aviation-Reference"
    
    # Meeting / call notes — date patterns in filenames with names
    if re.search(r'\d{4}.*call|call.*\d{4}|— \w+ \d|– \w+ \d', lower):
        return "Meeting-Note"
    if any(kw in lower for kw in ["call with", "meeting", "call —", "call -", "briefing",
                                   "conversation", "catch-up", "catch up", "kickoff",
                                   " — ", " – "]) and not any(kw in lower for kw in ["story", "scout"]):
        # Likely a meeting or partnership note
        return "Meeting-Note"

    # Personal notes - date-only filenames, personal tags
    if any(t in tags for t in ["personal"]):
        return "Personal-Note"
    if re.match(r'^\d{1,2}\s\w+\s\d{4}', lower) or re.match(r'^\w+,\s+\w+\s+\d{1,2}', lower):
        return "Personal-Note"

    # Splice / magazine projects
    if any(kw in lower for kw in ["splice", "dronefly"]):
        return "Project-Note"
    
    # Media analysis — Brian Morrissey, The Rebooting, industry publications
    if any(kw in lower for kw in ["the rebooting", "brian morrissey", "press gazette",
                                   "media operator", "nieman", "axios", "politico",
                                   "ben thompson", "stratechery", "platformer"]):
        return "Media-Analysis"
    
    # CUNY lectures
    if "cuny" in lower:
        return "Media-Analysis"

    # Book summary / podcast notes with "(Author)" or "by Author" pattern
    if re.search(r'\([A-Z][a-z]+ [A-Z][a-z]+\)', title) or re.search(r'\([A-Z][a-z]+\)', title):
        return "Personal-Note"

    # Coaching-related content (not client sessions — frameworks, reflections)
    if any(t in tags for t in ["coaching"]):
        return "Coaching-Session"
    if any(kw in lower for kw in ["coach", "mentor", "icf "]):
        return "Coaching-Session"

    # Grants
    if any(t in tags for t in ["grants"]):
        return "Grant-Radar"
    if "grant" in lower:
        return "Grant-Radar"

    # Startup / business frameworks (no tags)
    if any(kw in lower for kw in ["startup", "founder", "venture", "pitch",
                                   "fundraising", "revenue ", "sales", "marketing",
                                   "business ", "bootstrapping", "mvp"]):
        return "Project-Note"

    # Personal reflections
    if any(kw in lower for kw in ["reflection", "journal", "diary", "birthday",
                                   "what i", "letter to"]):
        return "Personal-Note"

    # CUNY lectures, school sessions
    if any(kw in lower for kw in ["school of splice", "beta ", "sos "]):
        return "Project-Note"

    # Catch-all: anything still unmatched gets Note type
    return "Note"


def extract_quote_attribution(body, title):
    """Extract attribution from a quote file."""
    # Pattern: quote text — Author
    match = re.search(r'—\s*(.+)$', title, re.MULTILINE)
    if match:
        return match.group(1).strip()
    
    # Try body patterns: "..." — Author
    for line in body.split("\n"):
        line = line.strip()
        match = re.search(r'[—–-]\s*(.+)$', line)
        if match and len(match.group(1)) < 100:
            return match.group(1).strip().rstrip('.')
    
    return ""


def extract_date_from_body(body, tags):
    """Try to extract a date from the body or tags."""
    # Bear tag patterns
    for tag in tags:
        # date tag: e.g. 2023-07-04
        match = re.match(r'(\d{4}-\d{2}-\d{2})', tag)
        if match:
            return match.group(1)

    # Inline date patterns: **July 4, 2023** or "Mon, October 30th, 2023"
    date_patterns = [
        r'\*\*(\w+ \d{1,2},? \d{4})\*\*',
        r'(\w+,? \w+ \d{1,2}(?:th|st|nd|rd)?,? \d{4})',
        r'^(\d{1,2} \w+ \d{4})',
    ]
    for pattern in date_patterns:
        match = re.search(pattern, body)
        if match:
            date_str = match.group(1).strip()
            # Try to parse common formats
            for fmt in ["%B %d, %Y", "%B %d %Y", "%d %B %Y", "%A, %B %d, %Y", "%A %B %d, %Y"]:
                try:
                    return datetime.strptime(date_str, fmt).strftime("%Y-%m-%d")
                except ValueError:
                    continue
    return ""


def extract_source_url(body):
    """Extract Bear-style URL: - URL: <https://...> or Bare URL."""
    match = re.search(r'URL:\s*<([^>]+)>', body)
    if match:
        return match.group(1)
    match = re.search(r'(?:Best link|Source):\s*\[([^\]]+)\]\(([^)]+)\)', body)
    if match:
        return match.group(2)
    return ""


def transform_file(src_path, dest_dir):
    """Read a Bear file, classify it, and write a Tolaria-compatible note."""
    try:
        with open(src_path, "r", encoding="utf-8", errors="replace") as f:
            text = f.read()
    except Exception as e:
        print(f"  ERROR reading {src_path}: {e}")
        return

    title, tags, body = extract_frontmatter(text)
    if not title:
        # Fallback: use filename without extension
        title = Path(src_path).stem

    note_type = classify_file(src_path.name, tags, title)
    if note_type is None:
        print(f"  SKIP (no type match): {src_path.name}")
        return None

    # Build frontmatter
    frontmatter = {}
    frontmatter["type"] = note_type
    if tags:
        frontmatter["tags"] = tags

    # Type-specific extractions
    if note_type == "Quote":
        attribution = extract_quote_attribution(body, title)
        if attribution:
            frontmatter["attribution"] = attribution

    if note_type in ("Story-Scout", "Coaching-Session", "Meeting-Note", "Grant-Radar", "Personal-Note"):
        date_val = extract_date_from_body(body, tags)
        if date_val:
            frontmatter["date"] = date_val

    if note_type in ("Media-Analysis", "Project-Note"):
        url = extract_source_url(body)
        if url:
            frontmatter["source_url"] = url

    if note_type == "Story-Scout":
        # Extract recommendation from summary section
        match = re.search(r'\*\*Scout recommendation:\*\*(.+?)(?:\n|$)', body)
        if match:
            frontmatter["recommendation"] = match.group(1).strip()
        # Extract scout date from title
        date_match = re.search(r'(\w+ \d{1,2},? \d{4})', title)
        if date_match:
            for fmt in ["%B %d, %Y", "%B %d %Y"]:
                try:
                    frontmatter["scout_date"] = datetime.strptime(
                        date_match.group(1), fmt
                    ).strftime("%Y-%m-%d")
                    break
                except ValueError:
                    continue

    if note_type == "Coaching-Session":
        # Extract client name from title after "Coaching - "
        client = title.replace("Coaching - ", "").strip()
        if client:
            frontmatter["client"] = client

    # Generate filename: slugified title
    slug = re.sub(r'[^\w\s-]', '', title.lower())
    slug = re.sub(r'[-\s]+', '-', slug).strip('-')
    # Truncate absurdly long filenames
    if len(slug) > 80:
        slug = slug[:80].rstrip('-')
    dest_filename = f"{slug}.md"

    # Strip tags line from body for Tolaria (tags now in frontmatter)
    body_lines = body.split("\n")
    cleaned_lines = []
    for line in body_lines:
        # Remove standalone tag-only lines and URL: <...> lines (moved to frontmatter)
        stripped = line.strip()
        if re.match(r'^#[\w/-]+(?:\s+#[\w/-]+)*$', stripped):
            continue
        if re.match(r'^-?\s*URL:\s*<[^>]+>', stripped):
            continue
        cleaned_lines.append(line)
    
    clean_body = "\n".join(cleaned_lines).strip()

    # Write out: prepend the H1 back to the body
    full_body = "# " + title + "

" + clean_body if title else clean_body

    yaml_lines = ["---"]
    for key, val in frontmatter.items():
        if isinstance(val, str):
            yaml_lines.append(f"{key}: {val}")
        elif isinstance(val, list):
            yaml_lines.append(f"{key}:")
            for item in val:
                yaml_lines.append(f"  - {item}")
    yaml_lines.append("---")

    output = "\n".join(yaml_lines) + "\n\n" + full_body

    dest_path = dest_dir / dest_filename
    # Avoid overwriting: append -2, -3 etc.
    counter = 1
    while dest_path.exists():
        counter += 1
        stem = Path(dest_filename).stem
        dest_path = dest_dir / f"{stem}-{counter}.md"

    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(output)

    rel = os.path.relpath(dest_path, dest_dir.parent)
    print(f"  OK: {src_path.name} → {rel}")
    return dest_path


def process_batch(src_dir, dest_dir, filters=None):
    """Process all Bear files matching optional filename filters."""
    src = Path(src_dir)
    dest = Path(dest_dir)
    dest.mkdir(parents=True, exist_ok=True)

    processed = 0
    skipped = 0

    for f in sorted(src.iterdir()):
        if not f.name.endswith(".md"):
            continue
        if filters and not any(fn in f.name.lower() for fn in filters):
            continue

        result = transform_file(f, dest)
        if result:
            processed += 1
        else:
            skipped += 1

    print(f"\nDone: {processed} notes created, {skipped} skipped")
    return processed, skipped


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Migrate Bear notes to Tolaria vault")
    parser.add_argument("source", help="Source directory of Bear .md files")
    parser.add_argument("dest", help="Destination directory for Tolaria notes")
    parser.add_argument("--filter", nargs="+", help="Only process files matching these substrings")
    args = parser.parse_args()

    process_batch(args.source, args.dest, args.filter)
