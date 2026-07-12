from nltk.tokenize import word_tokenize
from nltk import FreqDist
from string import punctuation

with open("foodie.txt", "r", encoding="utf-8") as file:
    text = file.read().lower()

words = word_tokenize(text)

words = [word for word in words if word not in punctuation]

fdist = FreqDist(words)

print(fdist.most_common(20))