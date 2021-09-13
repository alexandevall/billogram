import json
from database_model import DatabaseModel

class DiscountCodeModel:
    def __init__(self):
        self.discount_id = ""
        self.code = ""
        self.user_id = ""
        self.brand_user_token = ""

    @staticmethod
    def from_json(json_str):
        d = json.loads(json_str)
        model = DiscountCodeModel()
        model.discount_id = d.get('id') or model.discount_id
        model.code = d.get('code') or model.code
        model.user_id = d.get('user_id') or model.user_id
        model.brand_user_token = d.get('brand_user_token') or model.brand_user_token
        return model

    @staticmethod
    def save(discount_code_model):
        db = DatabaseModel()
        db.save_dicount_code(discount_code_model)
        return discount_code_model

    @staticmethod
    def fetch(discount_id, user_id):
        db = DatabaseModel()
        json_str = db.fetch_discount_code_for_user(discount_id, user_id)
        if (json_str):
            return DiscountCodeModel.from_json(json_str)
        return None
