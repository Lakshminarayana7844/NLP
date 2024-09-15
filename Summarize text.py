import nltk
from nltk.tokenize import sent_tokenize

doc = """Natural language processing (NLP) is a subfield of artificial intelligence (AI) that focuses on the interaction between computers and humans through natural language.
NLP technologies are used to process, analyze, and understand large amounts of natural language data.
One of the primary applications of NLP is sentiment analysis, which determines the sentiment or emotional tone of a piece of text. Sentiment analysis is widely used in social media monitoring, customer feedback analysis, and brand reputation management.
Text summarization is another important NLP task. Extractive summarization involves selecting a subset of sentences from a text to create a shorter version that retains the most critical information. Abstractive summarization, on the other hand, generates a summary by paraphrasing and rephrasing the original text."""

sentence=sent_tokenize(doc)
summary=sentence[:2]
for s in summary:
    print(s)
