import json # comes with Python (we don't need to install pip
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

# Python code that is pretending to be a web browser

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])

# docs.python.org/3/library/json.html
"""
A library that allows to manipulate JSON data or printing them in a nicer way.
"""
#print(response.json())
print(json.dumps(response.json(), indent=3))