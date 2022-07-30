""" URL Shortener API """
from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi import HTTPException
from functions import json_url_lookup, gen_short_url

app = FastAPI()

class Link(BaseModel):
    """ Validate URL(s) as string """
    input_url : Optional[str]
    short_url : Optional[str]

@app.get("/api-1.0/test")
async def api_check()->str:
    """ is API reachable """
    return {
        "check" : "API OK"
        }

@app.post("/api-1.0/create-short")
async def shorten(input_url:Link)->str:
    """ Endpoint takes long url, returns short url plus original url """
    if not input_url:
        raise HTTPException(status_code=404, detail="input_url field is required")
    mini = gen_short_url(5)
    domain = "http://127.0.0.1/"
    return {
        "shortened_url": domain + mini,
        "input_url" : input_url
        }

@app.get("/api-1.0/visit-short")
async def visit_shortened(short_url:Link)->str:
    """ Endpoint takes short url, maps to original url and visits original url"""
    if not short_url:
        raise HTTPException(status_code=404, detail="input_url field is required")
    long_url = json_url_lookup(short_url)
    print(long_url)
    return long_url
