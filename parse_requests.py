import json

from discount_model import DiscountModel


def get_discount_model_for_get_discount_codes_req(req):
    body = json.loads(req.data)

    discount_id = body.get('discount_id')
    if not discount_id:
        raise Exception('discount_id is a required argument when getting a discount-code')

    discount_model = DiscountModel.fetch(discount_id)
    if not discount_model:
        raise Exception('cannot find discount with id "{}'.format(discount_id))

    return discount_model
