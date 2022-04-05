# import webbrowser
import requests
# webbrowser.open("https://www.sanignacio.pr/")

res = requests.get("https://www.gutenberg.org/cache/epub/67769/pg67769.txt")
print(len(res.text))
print(res.text[0:300])