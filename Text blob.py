from textblob import TextBlob
sentences = [
    "I love this product! It's amazing.",
    "The weather is terrible today."
]
for sentence in sentences:
    blob=TextBlob(sentence)
    sentiment=blob.sentiment.polarity
    if sentiment<0:
        print("Bad")
    elif sentiment>0:
        print("Good")
    else:
        print("Average")
