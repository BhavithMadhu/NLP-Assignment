from nltk.tokenize import sent_tokenize, word_tokenize

with open("foodie.txt", "r", encoding="utf-8") as file:
    text = file.read()

print("Sentences:\n")
print(sent_tokenize(text))

print("\nWords:\n")
print(word_tokenize(text))