""" Test Main App """
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_read_main():
    """ Test the 'is API reachable' function in main """
    response = client.get("/api-1.0/test")
    assert response.status_code == 200
    assert response.json() == {"check" : "API OK"}


def test_shorten():
    """ Test API is working with shorten method """
    response = client.get("/api-1.0/create-short")
    assert response.status_code == 405


def test_example_url():
    """ Test with example url of known length """
    test_url = "http://127.0.0.1:8000/api-1.0/test"
    resp = client.get(test_url)
    assert len(resp.content) == 18
    
