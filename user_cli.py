""" URL Shortener API - a bit like bitly"""

# see also : pip install short_url if you want to *cheat*

import re
import json
import requests

print("."*20)
print("-"*2 + " URL Shortener " + "-"*2)
print("."*20 + "\n")

valid = False

# Ask user for a valid http(s) URL to shorten
while not valid:
    input_url = input("Enter a url to shorten and press ENTER\n")
    REGEX = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(REGEX,input_url)
    if not url:
        print("Not a Valid URL")
    else:
        valid = True

# API Endpoint to shorten URL 
PREFIX_URL = "http://127.0.0.1:8000/api-1.0/"

# User's long URL to shorten
payload = {
    'input_url': input_url
    }

# Request shortened version from endopoint and display back on CLI
response = requests.post(PREFIX_URL+"create-short/",params=payload)
json_data = response.json()
print(json_data)
print(f"\nShortened URL =  {json_data['shortened_url']}\n")

shorter_url = json_data['shortened_url']

# Store the short and long urls in a dictionary
dictionary = {
    "short_url": shorter_url ,
    "long_url": input_url,
}

# Serializing json to write to file
json_object = json.dumps(dictionary)

# Writing to sample.json
with open("map_urls.json","a", encoding="utf-8") as outfile:
    outfile.write(json_object)
    outfile.write('\n')

# Ask user for short link to visit, make API call - map it to long url
to_visit = input(">>> Enter Short URL to visit and press ENTER <<<\n")
print(f"\nYou want to visit {to_visit}, \nrequesting via the full link: \n")

payload = {
    'short_url': to_visit
    }

response = requests.get(PREFIX_URL+"visit-short/",params=payload)
response = (response.content)

# print with decode to remove the b'
print(f"Here is your original, LONGER url :\n {response.decode('utf-8')}")
