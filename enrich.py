#!/usr/bin/env python3
"""
Enrich the vault: retype misfiled notes, add relationships, archive old content.
Run from hermes-tolaria-vault/ directory.
"""

import json
import os
import re
import shutil
from pathlib import Path

NOTES_DIR = Path("notes")
BACKUP_DIR = Path("notes_backup")

# === PATTERNS FOR RETYPING ===

aviation_kw = ["flight", "aviation", "pilot", "aircraft", "aeroservice", "aeroviation",
    "engine", "circuit", "radio call", "ctaf", "right of way", "altimeter",
    "cloud cover", "vmc", "v-speed", "squawk", "taf", "metar", "checklist",
    "poh", "rpl", "rpc", "raaus", "casa", "atc", "msl", "agl", "propeller",
    "manifold", "lift equation", "stall", "drag", "airspeed", "piston",
    "swiss cheese", "navigation", "vfr", "g1000", "drone", "uav", "caas",
    "safety culture", "weight and balance"]

meeting_kw = ["call with", "meeting", "briefing", "conversation", "catch-up",
    "catch up", "kickoff", " — ", " – ", "call —", "call -",
    "alex, rishad", "alix, alan", "anita, alan", "rachael + alan",
    "shuwei + alan", "shuwei, suzanne", "fitri-alan",
    "first meeting with", "intro with", "nsc meeting", "quick sync",
    "sos kickoff", "school of splice-", "pat-splice", "jane-splice",
    "johanna-splice", "firetree + splice", "icrc x splice",
    "ims-puma", "pankajfactor", "splice + piano",
    "splice x gni", "splice media aws", "splice china dialogue",
    "usg media support", "bangladesh journalism training",
    "guest speaker at", "kl roundtable", "kl scenario",
    "dw ai berlin", "echos presentation"]

coaching_kw = ["coach", "mentor", "icf", "coaching",
    "clifton strengths", "via character", "scar model",
    "trillion dollar coach", "clean language",
    "the trap of wanting", "the very real dangers",
    "18 key components", "fearless coaching"]

grant_kw = ["grant", "funding", "skillsfuture", "aof", "ifpim",
    "radar", "aijc", "mdif", "osf"]

personal_kw = ["birthday", "love letter", "reflection", "what i know about myself",
    "what i want for myself", "what i've learned", "what is success",
    "things i've learned", "50th birthday", "celebrating my 50th",
    "chiang mai, feb", "italy trip", "scorpio moon", "men at forty",
    "hello friend", "hello from singapore", "first things first",
    "life themes", "dinner with", "my most powerful",
    "now.md", "changelog.md", "things to improve"]

media_kw = ["brian morrissey", "the rebooting", "press gazette", "nieman",
    "axios", "politico", "ben thompson", "stratechery", "platformer",
    "the content trap", "the gutenberg", "the daily me",
    "buzzfeed", "nytimes", "harvard business",
    "cuny", "ucla", "media operator", "jeff jarvis",
    "news is dead", "defining journalism",
    "above-the-line media", "new serp", "media blame",
    "extremely online", "endless media", "packaged media",
    "the hammer of", "the adolescence of", "the intelligence age",
    "apple intelligence", "claude opus", "this is why you're still slow"]

splice_biz_kw = ["splice", "beta ", "school of splice", "dronefly",
    "startup", "founder", "venture", "pitch", "fundraising",
    "revenue", "sales", "marketing ", "business ",
    "mvp", "bootstrapping", "puma", "acquisition",
    "fractals", "flybest", "flycheck", "magenta"]

# === HELPER FUNCTIONS ===

def parse_frontmatter(text):
    """Parse YAML frontmatter from a note."""
    lines = text.split("\n")
    if not lines or not lines[0].strip() == "---":
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
        # List item continuation
        if stripped.startswith("- ") and current_key:
            current_list.append(stripped[2:].strip())
            frontmatter[current_key] = current_list
            continue
        # Multi-line list
        if stripped.startswith("-") and current_key and isinstance(frontmatter.get(current_key), list):
            frontmatter[current_key].append(stripped[1:].strip())
            continue
        # Key: value
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


def serialize_frontmatter(fm):
    """Serialize frontmatter dict back to YAML string."""
    lines = ["---"]
    for key, val in fm.items():
        if isinstance(val, list) and len(val) > 0:
            lines.append(f"{key}:")
            for item in val:
                lines.append(f"  - {item}")
        elif isinstance(val, str):
            lines.append(f"{key}: {val}")
        else:
            lines.append(f"{key}: {val}")
    lines.append("---")
    return "\n".join(lines)


def update_note(filepath):
    """Read, update frontmatter, and write back a note."""
    try:
        with open(filepath, "r") as f:
            text = f.read()
    except Exception as e:
        return {"file": str(filepath), "error": str(e)}
    
    fm, body = parse_frontmatter(text)
    changes = []
    name = filepath.name.lower()
    
    if not fm or "type" not in fm:
        return {"file": str(filepath), "error": "no frontmatter or type"}
    
    original_type = fm["type"]
    new_type = None
    
    # === RETYPING ===
    if original_type == "Note":
        # Check if Readme
        if filepath.stem.lower() == "readme":
            return {"file": str(filepath), "info": "skipe-readme"}
        
        # Check aviation first
        if any(kw in name for kw in aviation_kw):
            new_type = "Aviation-Reference"
        elif any(kw in name for kw in grant_kw):
            new_type = "Grant-Radar"
        elif any(kw in name for kw in coaching_kw):
            new_type = "Coaching-Session"
        elif any(kw in name for kw in meeting_kw):
            new_type = "Meeting-Note"
        elif any(kw in name for kw in personal_kw):
            new_type = "Personal-Note"
        elif any(kw in name for kw in media_kw):
            new_type = "Media-Analysis"
        elif any(kw in name for kw in splice_biz_kw):
            new_type = "Project-Note"
        
        if new_type:
            fm["type"] = new_type
            changes.append(f"retyped: Note → {new_type}")
    
    # === ADD RELATIONSHIPS ===
    current_type = fm.get("type", original_type)
    
    # All coaching notes → Splice
    if current_type == "Coaching-Session" and "belongs_to" not in fm:
        fm["belongs_to"] = "Splice Media"
        changes.append("added belongs_to: Splice Media")
    
    # All aviation notes → Magenta
    if current_type == "Aviation-Reference":
        rels = fm.get("related_to", [])
        if isinstance(rels, str):
            rels = [rels]
        if not any("Magenta" in r for r in rels):
            if not rels:
                fm["related_to"] = ["Magenta Debrief"]
            else:
                rels.append("Magenta Debrief")
                fm["related_to"] = rels
            changes.append("added related_to: Magenta Debrief")
    
    # Grant radars → ventures
    if current_type == "Grant-Radar":
        if "belongs_to" not in fm:
            fm["belongs_to"] = "Magenta Debrief"
            changes.append("added belongs_to: Magenta Debrief")
        rels = fm.get("related_to", [])
        if isinstance(rels, str):
            rels = [rels]
        if not any("Dronefly" in r for r in rels):
            if not rels:
                fm["related_to"] = ["Dronefly.sg"]
            else:
                rels.append("Dronefly.sg")
                fm["related_to"] = rels
            changes.append("added related_to: Dronefly.sg")
    
    # Story scouts → Slugs
    if current_type == "Story-Scout":
        rels = fm.get("related_to", [])
        if isinstance(rels, str):
            rels = [rels]
        if not any("Slugs" in r for r in rels):
            if not rels:
                fm["related_to"] = ["Slugs"]
            else:
                rels.append("Slugs")
                fm["related_to"] = rels
            changes.append("added related_to: Slugs")
    
    # === ARCHIVE OLD NOTES ===
    is_2021_splice = original_type in ("Project-Note", "Meeting-Note") and (
        "2021" in name and "splice" in name
    )
    is_superseded_grant = filepath.stem in [
        "sg-grants-radar-20-apr-2026",
        "caas-skillsfuture-radar-20-apr-2026",
        "slugs-story-scout-april-8-2026"
    ] or name.endswith("-april-8-2026.md")
    
    if is_2021_splice or is_superseded_grant or (
        filepath.stem in [
            "firetree-splice-june-16-2021", "icrc-x-splice-may-12-2021",
            "ims-puma-splice-june-10-2021", "alex-rishad-alan-june-17-2021",
            "pat-splice-may-20-2021", "pankajfactordaily-alansplice-june-17-2021",
            "jane-splice-june-3-2021", "anita-alan-july-6-2021",
            "johanna-splice-july-15-2021"
        ]
    ):
        if "status" not in fm:
            fm["status"] = "archived"
            changes.append("archived (status: archived)")
    
    if not changes:
        return {"file": str(filepath), "status": "unchanged"}
    
    # Write back
    output = serialize_frontmatter(fm) + "\n" + body
    with open(filepath, "w") as f:
        f.write(output)
    
    return {"file": str(filepath), "status": "updated", "changes": changes}


def merge_duplicates():
    """Merge duplicate -2.md files into their originals."""
    merged = []
    files = list(NOTES_DIR.glob("*.md"))
    seen = {}
    
    for f in sorted(files):
        stem = f.stem
        # Check if this is a -2.md variant
        m = re.match(r'(.+)-(\d+)$', stem)
        if m:
            base = m.group(1)
            # Find the original
            orig = NOTES_DIR / f"{base}.md"
            alt = NOTES_DIR / f"{base}-alt.md"
            if orig.exists():
                # Append content to original
                try:
                    with open(f) as sf:
                        extra = sf.read()
                    with open(orig) as of:
                        original_text = of.read()
                    
                    # Only merge if they're truly different
                    if extra != original_text:
                        with open(orig, 'a') as of:
                            of.write("\n\n<!-- Merged from duplicate -->\n\n")
                            of.write(extra)
                    
                    # Remove duplicate
                    os.remove(f)
                    merged.append(f"{f.name} → {orig.name}")
                except Exception as e:
                    merged.append(f"ERROR merging {f.name}: {e}")
    
    return merged


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    print("=== Step 1: Backing up notes/ → notes_backup/ ===")
    if BACKUP_DIR.exists():
        shutil.rmtree(BACKUP_DIR)
    shutil.copytree(NOTES_DIR, BACKUP_DIR)
    print(f"Backed up {len(list(BACKUP_DIR.glob('*.md')))} files")
    
    print("\n=== Step 2: Enriching notes ===")
    results = {"updated": [], "unchanged": 0, "errors": []}
    for f in sorted(NOTES_DIR.glob("*.md")):
        if f.stem in ("vault-landscape-brief",):
            continue
        result = update_note(f)
        if result.get("status") == "updated":
            results["updated"].append(result)
        elif result.get("status") == "unchanged":
            results["unchanged"] += 1
        else:
            results["errors"].append(result)
    
    print(f"Updated: {len(results['updated'])} notes")
    print(f"Unchanged: {results['unchanged']} notes")
    print(f"Errors: {len(results['errors'])}")
    
    # Show sample changes
    for r in results["updated"][:10]:
        print(f"  {Path(r['file']).name}: {', '.join(r['changes'])}")
    if len(results["updated"]) > 10:
        print(f"  ... and {len(results['updated'])-10} more")
    
    print("\n=== Step 3: Merging duplicates ===")
    merged = merge_duplicates()
    print(f"Merged: {len(merged)} files")
    for m in merged[:15]:
        print(f"  {m}")
    
    print("\n=== Stats ===")
    total = len(list(NOTES_DIR.glob("*.md")))
    print(f"Total notes after enrichment: {total}")
    
    # Count types
    type_counts = {}
    for f in sorted(NOTES_DIR.glob("*.md")):
        with open(f) as fh:
            text = fh.read()
        fm, _ = parse_frontmatter(text)
        t = fm.get("type", "unknown")
        type_counts[t] = type_counts.get(t, 0) + 1
    
    for t, c in sorted(type_counts.items(), key=lambda x: -x[1]):
        print(f"  {t}: {c}")
    
    # Count relationships
    rel_count = 0
    for f in sorted(NOTES_DIR.glob("*.md")):
        with open(f) as fh:
            text = fh.read()
        fm, _ = parse_frontmatter(text)
        if "belongs_to" in fm or "related_to" in fm:
            rel_count += 1
    print(f"\nNotes with relationships (belongs_to / related_to): {rel_count}")
    print(f"Archived notes: {sum(1 for f in NOTES_DIR.glob('*.md') if 'status: archived' in open(f).read())}")
