import spacy
nlp=spacy.load("en_core_web_sm")
sentence = "Barack Obama was the 44th President of the United States, and he was born in Honolulu, Hawaii."
doc=nlp(sentence)
for ent in doc.ents:
    print(ent.text,":",ent.label_)
