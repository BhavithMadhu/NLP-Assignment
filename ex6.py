import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from string import punctuation

nltk.download("stopwords")

with open("foodie.txt", "r", encoding="utf-8") as file:
    text = file.read().lower()

words = word_tokenize(text)

stop_words = set(stopwords.words("english"))

filtered = [
    word for word in words
    if word not in stop_words and word not in punctuation
]

print(filtered)