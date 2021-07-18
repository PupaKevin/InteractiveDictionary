import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " %
                   get_close_matches(word, data.keys())[0])
        yn = yn.lower()
        if yn == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "n":
            return "word doesn't exist, plese double check "
        else:
            return " WE didn't understand what hte fuck you just said "
    else:
        return "word doesn't exist"


word = input("Enter Word: ")


output = (translate(word))
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
