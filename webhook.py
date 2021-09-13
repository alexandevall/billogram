import json

import requests


def call_webhook_when_user_generated_code(discount_model, discount_code_model):
    if not discount_model.webhook_url:
        return

    headers = { 'content-type': 'application/json' }
    body = {
        'user_id': discount_code_model.user_id,
        'discount_code': discount_code_model.code,
        'discount_id': discount_model.id
         }

    json_body = json.dumps(body)
    requests.post(
        discount_model.webhook_url,
        data=json_body,
        headers=headers)
