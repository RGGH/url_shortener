""" URL Shortener API """
from random import choice
import string
from urllib.parse import urlparse
import json

def gen_short_url(num_of_chars: int)->str:
    """Function to generate short_id of specified number of characters"""
    return ''.join(choice(string.ascii_letters+string.digits) for _ in range(num_of_chars))


def parse_base_url(starting_url : str)->str:
    """Function to create the shorter url"""
    sections = urlparse(starting_url)
    shorter_url =(sections.scheme + "://" + sections.netloc)
    return shorter_url

def json_url_lookup(shortened_url:str)->str:
    """Function to return the longer url from the shorter url"""
    d = [json.loads(line) for line in open("app/map_urls.json","r",encoding="utf-8") if shortened_url in line]
    long_url = (d[0]['long_url'])
    
    print(long_url)
    return long_url
