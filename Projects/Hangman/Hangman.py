import json, ssl
import urllib.request
from Color import Color

# This is discouraged but it will avoid certificate validation (prevents error)
ssl._create_default_https_context = ssl._create_unverified_context

# This is the URL from which we will request the data
colorURL = "https://random-data-api.com/api/color/random_color"

# Execute HTTP Request
req = urllib.request.Request(colorURL)
requestData = json.loads(urllib.request.urlopen(req).read())

# It enables the objects in the class Color to be used in this code
color:Color = Color(**requestData)

# my_List is a list that compiles all of the wrong letters.
my_List = [""]

# steps is the amount of steps that there are until the the player loses.
steps = ["""
    +----------------+
    |                |
    |
    |
    |
    |
    |
    |
    |
    \__________________""",
    """
    +----------------+
    |                |
    |              👁👄👁
    | 
    |
    |
    |
    |
    |
    \__________________""", 
    """
    +----------------+
    |                |
    |              👁👄👁
    |                |
    |
    |
    |
    |
    |
    \__________________""",
    """
    +----------------+
    |                |
    |              👁👄👁
    |               /|
    |
    |
    |
    |
    |
    \__________________""",
    """
    +----------------+
    |                |
    |              👁👄👁
    |               /|\\
    |
    |
    |
    |
    |
    \__________________""",
    """
    +----------------+
    |                |
    |              👁👄👁
    |               /|\\
    |               / 
    |
    |
    |
    |
    \__________________""",
     """
    +----------------+
    |                |
    |               X👄X
    |               /|\\
    |               / \\
    |
    |
    |
    |
    \__________________"""]
print(steps[0])

#print (color.color_name)

# it prints the amount of letters in the word in underscores, _.
print (len(color.color_name)* " _")

# It validates if the letter chosen is under one character and if it as a letter.
def input_function():
    while(True):
        letter = input("Choose letters to guess a word related to a color ")

        special_characters = "!@#$%^&*()-+?_=,<>/"
        
        # It invalidates inputs that are more than 1 character, is a digit, is a space, and is a special character
        if(len(letter)!= 1):
            print("ERROR input a letter, no more than one character")
            continue
        if (letter.isdigit()):
            print("ERROR input a letter, not a digit")
            continue
        if (letter.isspace()):
            print (("ERROR input a letter, not a space"))
            continue
        if  (letter in special_characters):
            print("ERROR input a letter, not a special character")
            continue

        my_List.append(letter)
        return letter

print(input_function())

# This function that prints the word with the letters added by the player, if it was not a part of the letters in the word, then it stays the same. 
def printword ():
    Temp:str=""
    for letter in color.color_name:
        if letter in my_List:
            Temp+= letter
        else: 
            Temp+="_"
    print (Temp)

def getErrors():
    # Every time it runs, it detects if a letter that was not in the color name and adds +1 to the amount of errors
    error = 0

    for letter in my_List:
        if (letter not in color.color_name):
            error += 1
    if error == 7:
        print("GAME OVER, you absolute buffoon the word was")
        print (color.color_name)
    return error

# After the player answers the first letter, the game restarts the function that validates the letters, the one that prints the words, and if the steps are the same as the amount of errors
while (True):
    input_function()
    print (steps[getErrors()]) 
        
    if my_List == 7:
        requestData = json.loads(urllib.request.urlopen(req).read())
        color:Color = Color(**requestData)
        my_List.clear()
        print(steps[0])
        print (len(color.color_name)* " _")
