import urllib.request
import bibtexparser
from bibtexparser.bparser import BibTexParser
import yaml
import os

# 1. Settings
DBLP_URL = "https://dblp.org/pid/17/7594.bib"
OUTPUT_FILE = "_data/publications.yml"
os.makedirs("_data", exist_ok=True)

def clean_text(text):
    """
    Cleans LaTeX formatting from DBLP (e.g., 'Jean{-}Luc' -> 'Jean-Luc')
    """
    if not text: return ""
    
    # 1. Remove curly braces { } used for protection
    text = text.replace('{', '').replace('}', '')
    
    # 2. Fix common accents (expand this list if you see more issues)
    replacements = {
        '\\"o': 'ö', '\\"a': 'ä', '\\"u': 'ü',
        "\\'e": 'é', "\\'a": 'á',
        '\\v{c}': 'č', '\\v{s}': 'š', '\\v{z}': 'ž',
        '\\c{c}': 'ç', '\\ss': 'ß'
    }
    for latex, char in replacements.items():
        text = text.replace(latex, char)
        
    return text

def fetch_and_convert():
    print(f"Fetching from {DBLP_URL}...")
    try:
        with urllib.request.urlopen(DBLP_URL) as response:
            bibtex_str = response.read().decode('utf-8')
    except Exception as e:
        print(f"Error fetching: {e}")
        return

    # Use standard v1 parser for maximum compatibility
    parser = BibTexParser(common_strings=True)
    library = bibtexparser.loads(bibtex_str, parser=parser)
    entries = library.entries

    # Sort: Year (descending) -> Title
    entries.sort(key=lambda x: (x.get('year', '0000'), x.get('title', '')), reverse=True)

    # Clean every field in every entry
    for entry in entries:
        for key, value in entry.items():
            if isinstance(value, str):
                # Clean LaTeX artifacts and remove newlines
                clean = clean_text(value)
                entry[key] = clean.replace('\n', ' ').strip()

    # Save
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as file:
        yaml.dump(entries, file, default_flow_style=False, sort_keys=False, allow_unicode=True)
    
    print(f"Saved {len(entries)} publications.")

if __name__ == "__main__":
    fetch_and_convert()