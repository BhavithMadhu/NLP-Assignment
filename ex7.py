from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from string import punctuation

ps = PorterStemmer()

with open("foodie.txt", "r", encoding="utf-8") as file:
    text = file.read().lower()

words = word_tokenize(text)

stemmed = [
    ps.stem(word)
    for word in words
    if word not in punctuation
]

print(stemmed)