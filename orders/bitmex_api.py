import hashlib
import hmac
from urllib.parse import urlparse
import requests
import time


def generate_signature(secret, verb, url, expires, data):
    parsedURL = urlparse(url)
    path = parsedURL.path
    if parsedURL.query:
        path = path + '?' + parsedURL.query
    if isinstance(data, (bytes, bytearray)):
        data = data.decode('utf8')
    message = verb + path + str(expires) + data
    signature = hmac.new(bytes(secret, 'utf8'), bytes(message, 'utf8'), digestmod=hashlib.sha256).hexdigest()
    return signature


def new_order(symbol, side, qty, api_key, api_secret):
    data = '{"symbol":"'+symbol+'","side":"'+side+'","orderQty":'+str(qty)+',"ordType":"Market"}'
    expires = int(round(time.time()) + 5)
    headers = {'content-type' : 'application/json',
                'Accept': 'application/json',
                'X-Requested-With': 'XMLHttpRequest',
                'api-expires': str(expires),
                'api-key': api_key,
                'api-signature': generate_signature(api_secret, 'POST', '/api/v1/order', expires, data)
                }
    r = requests.post('https://testnet.bitmex.com/api/v1/order', headers=headers, data=data)
    return r.text


# def get_order(symbol, api_key, api_secret):
#     data = '{"symbol":"'+symbol+'", "reverse":"true", "count":100,"filter":{"orderID": '+pk+'}}'
#     expires = int(round(time.time()) + 5)
#     headers = {'content-type': 'application/json',
#                'Accept': 'application/json',
#                'X-Requested-With': 'XMLHttpRequest',
#                'api-expires': str(expires),
#                'api-key': api_key,
#                'api-signature': generate_signature(api_secret, 'POST', '/api/v1/order', expires, data)
#                }
#     r = requests.get('https://testnet.bitmex.com/api/v1/order', headers=headers, data=data).json()
#     return r