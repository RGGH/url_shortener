""" URL Shortener API """

gunicorn -k uvicorn.workers.UvicornWorker main:app