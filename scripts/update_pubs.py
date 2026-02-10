import urllib.request
import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import convert_to_unicode, author
import yaml
import os

# 1. Settings
DBLP_URL = "https://dblp.org/pid/17/7594.bib"
OUTPUT_FILE = "_data/publications.yml"

# Ensure _data directory exists
os.makedirs("_data", exist_ok=True)

def clean_dblp_string(text):
    """
    Cleans DBLP specific LaTeX artifacts that standard parsers miss.
    Removes protection brackets like {C}hina or Jean{-}Luc.
    """
    if not text:
        return ""
    # Remove braces used for protection
    text = text.replace('{', '').replace('}', '')
    # Fix common LaTeX accents if the parser missed them
    text = text.replace('\\"o', 'ö').replace("\\'e", 'é') # Add more if needed
    return text

def customizations(record):
    """
    Custom function to clean up the record during parsing.
    """
    # Standard unicode conversion
    record = convert_to_unicode(record)
    # Split authors into a list (optional, but good for control)
    # record = author(record) 
    return record

def fetch_and_convert():
    print(f"Fetching from {DBLP_URL}...")
    
    try:
        with urllib.request.urlopen(DBLP_URL) as response:
            bibtex_str = response.read().decode('utf-8')
    except Exception as e:
        print(f"Error fetching data: {e}")
        return

    # 2. Parse with Customizations
    parser = BibTexParser()
    parser.customization = customizations
    library = bibtexparser.loads(bibtex_str, parser=parser)
    entries = library.entries

    # 3. Deep Cleaning & Sorting
    entries.sort(key=lambda x: (x.get('year', '0000'), x.get('title', '')), reverse=True)

    for entry in entries:
        for key, value in entry.items():
            if isinstance(value, str):
                # 1. Convert to Unicode (handled by parser, but double check)
                # 2. Strip DBLP braces
                cleaned = clean_dblp_string(value)
                # 3. Clean Newlines
                entry[key] = cleaned.strip().replace('\n', ' ')

    # 4. Save as YAML
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as file:
        yaml.dump(entries, file, default_flow_style=False, sort_keys=False, allow_unicode=True)
    
    print(f"Successfully saved {len(entries)} publications to {OUTPUT_FILE}")

if __name__ == "__main__":
    fetch_and_convert()