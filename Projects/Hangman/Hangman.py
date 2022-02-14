from asyncio.windows_events import NULL
import json, ssl
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

        if(len(letter)!= 1):
            print("ERROR, input a letter")
            continue
        if (letter.isdigit()):
            print("ERROR, input a letter")
            continue