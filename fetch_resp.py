""" URL Shortener API """

# see also : pip install short_url
# 'uvicorn main:app --reload'
# gunicorn -w 4 myapp:app

import re
import requests
import json
#from gen_short import json_url_lookup

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

# Request shortened version from endopoint and display on CLI
response = requests.get(PREFIX_URL+"create-short/",params=payload)
json_data = response.json()
print(f"\nShortened URL =  {json_data['shortened_url']}\n")

shorter_url = json_data['shortened_url']


# Store the shot and long urls in a dictionary
dictionary = {
    "short_url": shorter_url ,
    "long_url": input_url,
}

# Serializing json
json_object = json.dumps(dictionary)

# Writing to sample.json
with open("app/map_urls.json","a", encoding="utf-8") as outfile:
    outfile.write(json_object)
    outfile.write('\n')

# Ask user for short link to visit, make API call - map it to long url
to_visit = input(">>> Enter Short URL to visit and press ENTER <<<\n")
print(f"\nYou want to visit {to_visit}, \nrequesting via the full link: \n")


payload = {
    'short_url': to_visit
    }

# longer = json_url_lookup(to_visit)
# print(longer)

print(PREFIX_URL+"visit-short/")
print(payload)

response = requests.get(PREFIX_URL+"visit-short/",params=payload)

response = (response.content)

# print with decode to remove the b'
print(f"Here is your original, LONGER url : {response.decode('utf-8')}")
