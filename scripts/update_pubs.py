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

def is_arxiv(entry):
    """Checks if an entry is from ArXiv/CoRR based on Journal name."""
    journal = entry.get('journal', '').lower()
    return 'corr' in journal or 'arxiv' in journal

def get_arxiv_link(entry):
    """Extracts the likely ArXiv link from a CoRR entry."""
    # In DBLP, the Arxiv link is usually in 'ee' or 'url'
    if 'arxiv.org' in entry.get('ee', ''): return entry['ee']
    if 'arxiv.org' in entry.get('url', ''): return entry['url']
    # Fallback: if it is a CoRR entry, return the url/ee even if not explicitly saying arxiv
    return entry.get('ee') or entry.get('url')

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
    
    # Dictionary for merging: { normalized_title: entry_dict }
    merged_entries = {}

    # Sort input by year so we generally process newer stuff first, 
    # but we need to handle the ArXiv vs Journal merge regardless of order.
    library.entries.sort(key=lambda x: x.get('year', '0000'), reverse=True)

    for entry in library.entries:
        # 1. Clean data
        for key, value in entry.items():
            if isinstance(value, str):
                entry[key] = clean_text(value).strip()

        # 2. Normalize title (remove non-alphanumeric)
        raw_title = entry.get('title', '')
        norm_title = re.sub(r'[^a-z0-9]', '', raw_title.lower())
        
        # 3. Create Short Authors (M. Krnc)
        if 'author' in entry:
            authors = entry['author'].split(' and ')
            short_authors_list = []
            for a in authors:
                parts = a.strip().split()
                if len(parts) >= 2:
                    initials = "".join([f"{p[0]}." for p in parts[:-1]])
                    short_authors_list.append(f"{initials} {parts[-1]}")
                else:
                    short_authors_list.append(a)
            entry['short_authors'] = ", ".join(short_authors_list)

        # 4. Merging Logic
        if norm_title in merged_entries:
            existing = merged_entries[norm_title]
            
            new_is_arxiv = is_arxiv(entry)
            old_is_arxiv = is_arxiv(existing)

            if old_is_arxiv and not new_is_arxiv:
                # CASE A: We have a CoRR placeholder, but now we found the REAL Journal paper.
                # Action: Replace the placeholder with the Real paper, but keep the CoRR link.
                arxiv_url = get_arxiv_link(existing)
                entry['arxiv_url'] = arxiv_url
                merged_entries[norm_title] = entry # Overwrite!
                
            elif not old_is_arxiv and new_is_arxiv:
                # CASE B: We have the Real Journal paper, and now found the CoRR version.
                # Action: Keep the Real paper, just add the link.
                existing['arxiv_url'] = get_arxiv_link(entry)
                
            else:
                # CASE C: Two real papers or two ArXiv papers? 
                # Keep the existing one (since we sorted by year desc, likely the newer/better one)
                pass
        else:
            # First time seeing this title
            if is_arxiv(entry):
                entry['is_arxiv_only'] = True
                entry['arxiv_url'] = get_arxiv_link(entry)
            merged_entries[norm_title] = entry

    # Convert to list and sort final result
    final_list = list(merged_entries.values())
    final_list.sort(key=lambda x: x.get('year', '0000'), reverse=True)

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as file:
        yaml.dump(final_list, file, default_flow_style=False, sort_keys=False, allow_unicode=True)
    
    print(f"Saved {len(final_list)} unique publications.")

if __name__ == "__main__":
    process_publications()