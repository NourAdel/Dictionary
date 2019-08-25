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
        print("did you mean %s? y OR n " % get_close_matches(word, data.keys())[0])
        ans=input()
        if ans == 'y':
            return data[get_close_matches(word, data.keys())[0]]
        elif ans == 'n':
            print("Couldn't find the word. Please check it again.")
            return
        else:
            print("invalid option")
            return


    else:
        print("Couldn't find the word. Please check it again.")
        return


Input = input("Enter the Word: \n ")
output = translate(Input)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
