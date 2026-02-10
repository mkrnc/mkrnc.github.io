import urllib.request
import bibtexparser
import yaml

# Fetch from DBLP
url = "https://dblp.org/pid/17/7594.bib"
response = urllib.request.urlopen(url)
bib_database = bibtexparser.loads(response.read().decode('utf-8'))

# Clean up data (optional) and Sort
entries = bib_database.entries
entries.sort(key=lambda x: x.get('year', '0000'), reverse=True)

# Save to _data/publications.yml
with open('_data/publications.yml', 'w') as file:
    yaml.dump(entries, file)