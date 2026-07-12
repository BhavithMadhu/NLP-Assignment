from nltk.tokenize import word_tokenize
from string import punctuation

with open("foodie.txt", "r", encoding="utf-8") as file:
    text = file.read().lower()

words = word_tokenize(text)

filtered = [word for word in words if word not in punctuation]

print(filtered)