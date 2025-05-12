import json # comes with Python (we don't need to install pip
import requests
import sys

#run in console -> python itunes.py Weezer
if len(sys.argv) != 2:
    sys.exit()

# Python code that is pretending to be a web browser to store a response from an API

response = requests.get("https://itunes.apple.com/search?entity=song&limit=10&term=" + sys.argv[1])

# docs.python.org/3/library/json.html
"""
A library that allows to manipulate JSON data or printing them in a readable way.
"""
#print(response.json())
#print(json.dumps(response.json(), indent=3))

json_response = response.json()

for el in json_response['results']:
    print(el['trackName'])