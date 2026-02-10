import urllib.request
import bibtexparser
from bibtexparser.bparser import BibTexParser
import yaml
import os
import re

# Settings
DBLP_URL = "https://dblp.org/pid/17/7594.bib"
OUTPUT_FILE = "_data/publications.yml"
os.makedirs("_data", exist_ok=True)

def clean_text(text):
    """Cleans LaTeX formatting and protection braces."""
    if not text: return ""
    text = text.replace('{', '').replace('}', '')
    text = text.replace('\n', ' ')
    
    # Common LaTeX accents
    replacements = {
        '\\"o': 'ö', '\\"a': 'ä', '\\"u': 'ü',
        "\\'e": 'é', "\\'a": 'á', "\\'c": 'ć',
        '\\v{c}': 'č', '\\v{s}': 'š', '\\v{z}': 'ž',
        '\\c{c}': 'ç', '\\ss': 'ß'
    }
    for latex, char in replacements.items():
        text = text.replace(latex, char)
    return text

def abbreviate_author(full_name):
    """Converts 'Matjaž Krnc' -> 'M. Krnc'"""
    if not full_name: return ""
    parts = full_name.split()
    if len(parts) < 2: return full_name # Single name, return as is
    
    # Last name is the last part
    last = parts[-1]
    # Initials for all previous parts (handling hyphenated names like Jean-Florent -> J.-F. is complex, simplifying to J.)
    initials = "".join([f"{p[0]}." for p in parts[:-1]])
    
    return f"{initials} {last}"

def process_publications():
    print(f"Fetching from {DBLP_URL}...")
    try:
        with urllib.request.urlopen(DBLP_URL) as response:
            bibtex_str = response.read().decode('utf-8')
    except Exception as e:
        print(f"Error fetching: {e}")
        return

    parser = BibTexParser(common_strings=True)
    library = bibtexparser.loads(bibtex_str, parser=parser)
    
    # Dictionary to handle merging: { normalized_title: entry_dict }
    merged_entries = {}

    for entry in library.entries:
        # 1. Clean data first
        for key, value in entry.items():
            if isinstance(value, str):
                entry[key] = clean_text(value).strip()

        # 2. Normalize title for comparison (lowercase, remove non-alphanumeric)
        raw_title = entry.get('title', '')
        norm_title = re.sub(r'[^a-z0-9]', '', raw_title.lower())
        
        # 3. Create Short Authors string (e.g. "M. Krnc, J. Doe")
        if 'author' in entry:
            authors = entry['author'].split(' and ')
            short_authors = [abbreviate_author(a.strip()) for a in authors]
            entry['short_authors'] = ", ".join(short_authors)
            # We keep the full 'author' field for the expanded view if needed

        # 4. Merging Logic
        if norm_title in merged_entries:
            existing = merged_entries[norm_title]
            
            # If current entry is arXiv (eprint), just attach its link to the existing one
            if 'journal' in existing and 'arxiv' in entry.get('journal', '').lower():
                 # Existing is journal, new is arxiv. Do nothing but maybe grab link.
                 if 'url' in entry: existing['arxiv_url'] = entry['url']
            
            elif 'journal' in entry and 'arxiv' not in entry.get('journal', '').lower():
                # New entry is a REAL journal, existing might be arxiv. Replace existing!
                # But keep the arxiv link if the old one had it
                old_url = existing.get('url')
                entry['arxiv_url'] = old_url # Assume old was the arxiv version
                merged_entries[norm_title] = entry
            
            else:
                # Both might be arxiv or same tier, keep the one with more info or just first one
                pass
        else:
            # New title
            # Check if this itself is an arxiv paper to label it
            if 'journal' in entry and 'arxiv' in entry['journal'].lower():
                entry['is_arxiv'] = True
                entry['arxiv_url'] = entry.get('url') # store specifically as arxiv link
            
            merged_entries[norm_title] = entry

    # Convert back to list
    final_list = list(merged_entries.values())
    
    # Sort: Year (descending)
    final_list.sort(key=lambda x: x.get('year', '0000'), reverse=True)

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as file:
        yaml.dump(final_list, file, default_flow_style=False, sort_keys=False, allow_unicode=True)
    
    print(f"Saved {len(final_list)} unique publications (merged).")

if __name__ == "__main__":
    process_publications()