import json, ssl
from pathlib import Path
import os
from urllib import response
import urllib.request
from Color import Color

# This is discouraged but it will avoid certificate validation (prevents error)
ssl._create_default_https_context = ssl._create_unverified_context

# This is the URL from which we will request the data
colorURL = "https://random-data-api.com/api/color/random_color?size=100"

# Create a list to populate with our data
colors:Color = [] 

# Directory
directory = "responses"
  
# Parent Directory path
parent_dir = Path(__file__).parents[0]
  
# Path
folderPath = os.path.join(parent_dir, directory)

os.mkdir(folderPath)
print("Directory '% s' created" % directory)
  

# loop 100

for e in range(100):

    # Execute HTTP Request
    req = urllib.request.Request(colorURL)
    requestData = json.loads(urllib.request.urlopen(req).read())

    # Loop over JSON items and Deserialize them into python objects
    for r in requestData:  
        #   Deserialize 
        color:Color = Color(**r)
        # Add object to list
        colors.append(color) 
        # Print id
        print(color.id)

        # Path
        filePath = os.path.join(folderPath, f"{color.uid}.json")
        
        with open(filePath,'w') as outlfile:
            json.dump(color.__dict__, outlfile)