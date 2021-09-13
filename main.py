
import json

from flask import Flask, request

from create_discount_code import create_discount_code_model
from discount_code_model import DiscountCodeModel
from discount_model import DiscountModel
from mock_services.authenticate import require_brand, require_user
from parse_requests import get_discount_model_for_get_discount_codes_req
from webhook import call_webhook_when_user_generated_code

app = Flask(__name__)

@app.route('/')
def test():
    return 'Ok'


# requests to '/create-discount-codes' is expected to have:
#
# *** headers ***
# content-type: application/json
# (required) brand_auth_token: <str>
# ---
# The "brand_auth_token" is supposed to be some token
# that a brand-user-account can be authenticated with
# (jwt, for instance).
# For now, it can be any of the keys in the
# dictionary 'token_to_brand', which can be found in
# file mock_service/authenticate.py
#
# *** body ***
# name: <the name of the discount, which discount-codes can be associated with>
# num_codes: <the number of codes which can be generated for this discount. Defaults to 0>
# webhook_url: <a url that is notified when a user has generated a discount-code>
@app.route('/create-discount-codes', methods = ['POST'])
def create_codes():
    brand = require_brand(request, 'create-discount-codes')
    discount_model = DiscountModel.from_json(request.data)
    print("discount_model", discount_model.webhook_url)
    discount_model.brand_id = brand['id']
    created_discount = DiscountModel.save(discount_model)
    return created_discount.__dict__


# requests to '/get-discount-code' is expected to have:
#
# *** headers ***
# content-type: application/json
# (required) user_auth_token: <str>
# ---
# The "user_auth_token" is supposed to be some token
# that a user-account can be authenticated with, similarly
# to brand_auth_token.
# For now, it can be any of the keys in the
# dictionary 'token_to_user', which can be found in
# file mock_service/authenticate.py
#
# *** body ***
# (required) discount_id: <the id for the discount, which discount-codes are associated with>
@app.route('/get-discount-code', methods = ['GET', 'POST'])
def get_code():
    user = require_user(request, 'get-discount-code')
    discount_model = get_discount_model_for_get_discount_codes_req(request)
    exsisting_discount_code = DiscountCodeModel.fetch(discount_model.id, user['id'])

    if exsisting_discount_code:
        return { 'discount-code': exsisting_discount_code.code }

    if not discount_model.there_are_discount_codes_left():
        raise Exception("there are no discount codes left")

    new_discount_code_model = create_discount_code_model(user, discount_model)
    DiscountCodeModel.save(new_discount_code_model)

    # this shuold ideally be done anachronistically - but i do not have the
    # time to implement that
    call_webhook_when_user_generated_code(discount_model, new_discount_code_model)

    return { 'discount-code': new_discount_code_model.code }


if __name__ == '__main__':
    app.run(host='0.0.0.0', port="5000", debug=True)
