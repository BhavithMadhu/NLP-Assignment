from sklearn.feature_extraction.text import TfidfVectorizer

with open("foodie.txt", "r", encoding="utf-8") as file:
    text = file.read()

documents = [line.strip() for line in text.split('.') if line.strip()]

vectorizer = TfidfVectorizer(stop_words='english')

tfidf = vectorizer.fit_transform(documents)

feature_names = vectorizer.get_feature_names_out()

for i, sentence in enumerate(documents):
    print(f"\nSentence {i+1}:")
    scores = tfidf[i].toarray()[0]

    for word, score in zip(feature_names, scores):
        if score > 0:
            print(f"{word:15} {score:.3f}")