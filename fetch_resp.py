""" URL Shortener API """

# see also : pip install short_url

import requests

# 'uvicorn main:app --reload'

test_url = "http://127.0.0.1:8000/api-1.0"

#user_url = input("")
example = "https://meta.stackexchange.com/questions/118594/data-explorer-truncates-links-after-380-characters"

payload = {
    'base_url': example
    }

response = requests.get(test_url,params=payload)
json_data = response.json()
print(json_data['Shortened_Url'])
