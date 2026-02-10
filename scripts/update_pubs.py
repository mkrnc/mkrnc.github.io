import urllib.request
import bibtexparser
import yaml
import os

# 1. Settings
DBLP_URL = "https://dblp.org/pid/17/7594.bib"
OUTPUT_FILE = "_data/publications.yml"

# Ensure _data directory exists
os.makedirs("_data", exist_ok=True)

def fetch_and_convert():
    print(f"Fetching from {DBLP_URL}...")
    
    # 2. Download the data
    try:
        with urllib.request.urlopen(DBLP_URL) as response:
            bibtex_str = response.read().decode('utf-8')
    except Exception as e:
        print(f"Error fetching data: {e}")
        return

    # 3. Parse BibTeX
    library = bibtexparser.parse_string(bibtex_str)
    entries = library.entries

    # 4. Clean and Sort
    # Sort by year (descending), then by title
    entries.sort(key=lambda x: (x.get('year', '0000'), x.get('title', '')), reverse=True)

    # Optional: Clean up keys if needed (e.g., removing messy newlines)
    for entry in entries:
        for key, value in entry.items():
            if isinstance(value, str):
                entry[key] = value.strip()

    # 5. Save as YAML
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as file:
        yaml.dump(entries, file, default_flow_style=False, sort_keys=False, allow_unicode=True)
    
    print(f"Successfully saved {len(entries)} publications to {OUTPUT_FILE}")

if __name__ == "__main__":
    fetch_and_convert()