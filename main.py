""" URL Shortener API """
from fastapi import FastAPI
from gen_short import gen_short_uri

app = FastAPI()

@app.get("/api-1.0/")
async def shorten(base_url:str):
    mini = gen_short_uri(5)
    domain = "https://127.0.0.1/"
    return {
        "Shortened_Url": domain + mini,
        "base_url" : base_url
        }
