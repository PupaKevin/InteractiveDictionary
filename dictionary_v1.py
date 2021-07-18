import json

data = json.load(open("data.json"))


def translate(word):
    if word in data:
        return data[word]
    else:
        return "word doesn't exist"


word = input("Enter Word: ")

print(translate(word))
