import wikipediaapi

# Initialize Wikipedia API
wiki_wiki = wikipediaapi.Wikipedia('en')

# Entity lookup list (for simplicity)
entities = ["Apple Inc.", "Apple", "Python (programming language)", "Python (genus)"]

# Disambiguate and print results
for entity in entities:
    page = wiki_wiki.page(entity)
    if page.exists():
        print(f"{entity}: {page.summary[:60]}...")
    else:
        print(f"{entity}: No Wikipedia page found.")
