conversation = [
    "Good morning! How's the weather today?",
    "I heard it's going to be sunny and warm.",
    "Could you please send me the report by 3 PM?",
    "Of course, I'll send it over before the deadline.",
    "Do you know where the nearest post office is?",
    "The post office is two blocks down the street."
]

for sentence in conversation:
    if '?' in sentence and 'please' not in sentence:
        act="Question"
    elif "Please" in sentence or "please" in sentence:
        act="Request"
    else:
        act="Statement"
    print(f"{sentence} \n Dialogue_act: {act}")
