# Sentences to parse
sentences = [
    "She walk to the park yesterday",
    "He jump over the fence"
]

# FSM for handling past tense
for sentence in sentences:
    words = sentence.split()
    converted_sentence = []
    
    for word in words:
        if word == "walk":
            word = word + "ed"
        elif word == "jump":
            word = word + "ed"
        converted_sentence.append(word)
    
    print(f"Original Sentence: '{sentence}'")
    print(f"Converted Sentence: {' '.join(converted_sentence)}")
    print("-" * 40)
