import json
from os import walk
from pathlib import Path


class DatabaseModel:
    def __init__(self):
        self.discount_dir = "database/Discount"
        self.discount_code_dir = "database/DiscountCode"

    def file_path_for_discount(self, id):
        return "{}/{}".format(self.discount_dir, id)

    def file_path_for_discount_code(self, discount_id, user_id):
        return "{}/{}/{}".format(self.discount_code_dir, discount_id, user_id)

    def open_file(self, path):
        content = ""
        try:
            with open(path, 'r') as f:
                content = f.read()
        except IOError:
            return None
        return content

    def write_file(self, path, content):
        f = open(path, "w")
        f.write(content)
        f.close()

    def fetch_discount(self, id):
        json_str = self.open_file(
            self.file_path_for_discount(id)
        )
        return json_str

    def fetch_discount_code_for_user(self, discount_id, user_id):
        json_str = self.open_file(
            self.file_path_for_discount_code(discount_id, user_id)
        )
        return json_str

    def fetch_codes_for_discount(self, discount_id):
        result = []
        path = "{}/{}".format(self.discount_code_dir, discount_id)
        user_ids = []
        for (_, _, filenames) in walk(path):
            user_ids = filenames
            break
        for user_id in user_ids:
            result.append(self.fetch_discount_code_for_user(discount_id, user_id))
        return result

    def save_discount(self, discount_model):
        path = self.file_path_for_discount(discount_model.id)
        json_str = json.dumps(discount_model.__dict__)
        self.write_file(path, json_str)

    def save_dicount_code(self, discount_code_model):
        path = self.file_path_for_discount_code(
            discount_code_model.discount_id,
            discount_code_model.user_id)

        directory = "{}/{}".format(
            self.discount_code_dir,
            discount_code_model.discount_id)

        json_str = json.dumps(discount_code_model.__dict__)

        # make sure the directory for the discount exist
        Path(directory).mkdir(parents=True, exist_ok=True)

        self.write_file(path, json_str)
