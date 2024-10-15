import requests
from tokeninfo import gettokeninfo

symbol, price = gettokeninfo()

soulurl = 'http://171.171.171.1:11434/api/generate'
model = 'Soul_v0A3'

prompt = f"token {symbol}, priced {price}."

data = {
    "model": model,
    "prompt": prompt
}

response = requests.post(soulurl, json=data)