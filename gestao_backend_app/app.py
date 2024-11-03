from http import HTTPStatus

from fastapi import FastAPI

from gestao_backend_app.schemas import Message

app = FastAPI()

@app.get('/')
def read_root():
    return """
    <html>
        <head>
            <title> Nosso olá mundo!</title>
        </head>
        <body>
            <h1> Olá Mundo </h1>
        </body>
    """