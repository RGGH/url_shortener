""" Test the path shortener & base url parser """
from functions import gen_short_url, parse_base_url

EXAMPLE = "https://meta.stackexchange.com/questions/118594/data-explorer-truncates-links-after-380-characters"

def test_gen_short_url():
    """ test the short path function """
    short = len(gen_short_url(5))
    assert short == 5

def test_parse_base_url():
    """ test the short path function """
    small_url=parse_base_url(EXAMPLE)
    assert len(small_url) == 30
    