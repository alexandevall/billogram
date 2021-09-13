import json

import requests

url = 'http://127.0.0.1:5000/get-discount-code'

def get_code(user_auth_token, discount_id):
    headers = {
        'content-type': 'application/json',
        'user_auth_token': user_auth_token
        }
    body = { 'discount_id': discount_id }
    json_body = json.dumps(body)
    response = requests.get(url, data=json_body, headers=headers)
    try:
        print("response-json", response.json())
    except:
        print("could not get json in response")

get_code("u2", "<id of discount - use a filename in database/Discount/>")
print("gotten_code")
