from sklearn.feature_extraction.text import TfidfVectorizer
sentences = [
    "Artificial intelligence (AI) is a field of computer science.",
    "Machine learning is a subset of AI that focuses on training models to make predictions.",
    "Deep learning is a type of machine learning that uses neural networks with multiple layers.",
    "Neural networks are composed of interconnected nodes called neurons.",
    "Recurrent neural networks (RNNs) are commonly used in natural language processing tasks."
]
vectorizer=TfidfVectorizer()
Tfidf_mat=vectorizer.fit_transform(sentences)
feature_names=vectorizer.get_feature_names_out()
print(feature_names)
