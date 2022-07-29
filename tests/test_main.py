""" x """

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_shorten():
    """ Test API is working with shorten method """
    response = client.get("/api-1.0/create-short")
    assert response.status_code == 422


def test_example_url():
    """ Test with example url of known length """
    test_url = "http://127.0.0.1:8000/api-1.0/test"
    resp = client.get(test_url)
    assert len(resp.content) == 18
    


