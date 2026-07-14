with open("foodie.txt", "r", encoding="utf-8") as file:
    text = file.read()

print(text.lower())