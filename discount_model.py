import json
import uuid

from database_model import DatabaseModel
from discount_code_model import DiscountCodeModel


class DiscountModel:
    def __init__(self):
        self.id = ""
        self.brand_id = ""
        self.name = ""
        self.webhook_url = ""
        self.num_codes = 0

    @staticmethod
    def from_json(json_str):
        d = json.loads(json_str)
        print("d", d)
        model = DiscountModel()
        model.id = d.get('id') or model.id
        model.brand_id = d.get('brand_id') or model.brand_id
        model.name = d.get('name') or model.name
        model.webhook_url = d.get('webhook_url') or model.webhook_url
        model.num_codes = d.get('num_codes') or model.num_codes
        return model

    @staticmethod
    def save(discount_model):
        discount_model.id = str(uuid.uuid4())
        db = DatabaseModel()
        db.save_discount(discount_model)
        return discount_model

    @staticmethod
    def fetch(id):
        db = DatabaseModel()
        json_str = db.fetch_discount(id)
        if (json_str):
            return DiscountModel.from_json(json_str)
        return None

    def get_codes(self):
        code_models = []
        db = DatabaseModel()
        json_str_list = db.fetch_codes_for_discount(self.id)
        for json_str in json_str_list:
            code_models.append(
                DiscountCodeModel.from_json(json_str)
            )
        return code_models

    def there_are_discount_codes_left(self):
        generated_codes = self.get_codes()
        return len(generated_codes) < self.num_codes
