""" URL Shortener API """
from random import choice
import string
from urllib.parse import urlparse

def gen_short_uri(num_of_chars: int)->str:
    """Function to generate short_id of specified number of characters"""
    return ''.join(choice(string.ascii_letters+string.digits) for _ in range(num_of_chars))


def parse_base_url(starting_url : str)->str:
    """Function to create the shorter url"""
    sections = urlparse(starting_url)
    shorter_url =(sections.scheme + "://" + sections.netloc)
    return shorter_url
