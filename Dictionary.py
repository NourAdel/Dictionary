import json

data = json.load(open("data.json"))


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]


    else:
        print("Couldn't find the word. Please check it again.")
        return


Input = input("Enter the Word: \n ")
output = translate(Input)
print(output)
