'''
API Flask
'''
from flask import *
from flask_ngrok import run_with_ngrok
from fastapi import FastAPI
import nest_asyncio
from pyngrok import ngrok
import uvicorn

app = Flask(__name__)


@app.route('/index')
def home():
    return 'Hello World'


run_with_ngrok(app)
app.run()

app = FastAPI()


@app.get('/index')
async def home():
    return "Hello World"


ngrok_tunnel = ngrok.connect(8000)
print(
    'Public URL:https://docs.google.com/spreadsheets/d/e/2PACX-1vR0dWHCZjcG96JzSkuV3UW5R5K-Fhlr-ZH0P9FSbXIlommHrGTlNek_RRmiCgQnvYbgx-A3Qo9JqGUg/pubhtml',
    ngrok_tunnel.public_url)
nest_asyncio.apply()
uvicorn.run(app, port=8000)
