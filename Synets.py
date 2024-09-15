import nltk
from nltk.corpus import wordnet

# Download WordNet data (run this once)
nltk.download('wordnet')

# Words to analyze
words = ["cat", "dog", "piano"]

# Analyze each word
for word in words:
    synsets = wordnet.synsets(word)
    print(f"Word: {word}")
    for synset in synsets[:1]:  # Just take the first synset for simplicity
        print(f"  Definition: {synset.definition()}")
    print("-" * 20)
