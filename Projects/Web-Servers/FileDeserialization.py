import json
import os
from pathlib import Path
from Color import Color

#  Locate and open file
myPath = Path(__file__).parents[0]
myFilePath = os.path.join(myPath, 'random_color.json')
data = open(myFilePath,)
 
# deserializing the data
data = json.load(data)
color:Color = Color(**data)

# Print data from the object
print(f"ID: {color.id}")
print(f"UID: {color.uid}")
print(f"Hex Value: {color.hexValue}")
print(f"Color Name: {color.colorname}")
print(f"hsl value: {color.hslvalue}")
print(f"hsla value: {color.hslavalue}")
print("Others expected...")