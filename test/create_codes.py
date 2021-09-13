import json

import requests

url = 'http://127.0.0.1:5000/create-discount-codes'
webhook_url = 'https://webhook.site/62dd084d-4da1-4d3a-999a-4d6370930a06'

def create_codes(brand_auth_token, name, num_codes):
    headers = {
        'content-type': 'application/json',
        'brand_auth_token': brand_auth_token,

        }
    body = {
        'name': name,
        'num_codes': num_codes,
        'webhook_url': webhook_url
         }
    json_body = json.dumps(body)
    response = requests.post(url, data=json_body, headers=headers)
    print('response', response.json())

create_codes("b1", "En grym kampanj!", 1)
print("created_codes")
