import re
text = '''
Once upon a time, there was a young boy named Peter.
He lived in a small village.
One day, he decided to explore the nearby forest.'''

sentences=re.split(r's[.!?]\s+',text.strip())
print(sentences)
if text.endswith(('.','!','?')):
    print("coherent")
else:
    print("Not coherent")
