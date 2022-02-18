from asyncio.windows_events import NULL
import json, ssl
from socket import if_indextoname
from pathlib import Path
import os
from urllib import response
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



print (len(color.color_name)* " _")

def input_function():
    while(True):
        letter = input("Choose letters to guess a word related to a color")

        special_characters = "!@#$%^&*()-+?_=,<>/"
        s=input()

        

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
    
    for letter in color.color_name:
        if letter in color.color_name:
            Temp+= letter
        else: 
            Temp+="_"
    print (Temp)

#while (True):
    #print (steps[0])
    #get input

def stepcounter():
    while(True):
        if my_List.append          
