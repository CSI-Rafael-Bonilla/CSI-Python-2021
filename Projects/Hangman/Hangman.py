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

color:Color = Color(**requestData)

my_List = [""]

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

print (color.color_name)

print (len(color.color_name)* " _")

def input_function():
    while(True):
        letter = input("Choose letters to guess a word related to a color")

        special_characters = "!@#$%^&*()-+?_=,<>/"
        

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

def printword ():
    Temp:str=""
    int = 0 
    for letter in color.color_name:
        if letter in my_List.append:
            Temp+= letter
        else: 
            Temp+="_"
    print (Temp)

for letter in my_List:
    if (letter not in color.color_name):
        



while (True):
    input_function()
    #print steps()

#while (True):
    #print (steps[0])
    #get input

#def stepcounter():
#    while(True):
#        if (len(my_List.append))

