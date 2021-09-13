
from discount_code_model import DiscountCodeModel
from mock_services.brand import get_brand_for_id


def create_discount_code(brand_name, user_name, discount_id):
    return '{}-thinks-{}-is-awesome-{}'.format(
        brand_name,
        user_name,
        discount_id
    )

def create_discount_code_model(user, discount_model):
    brand = get_brand_for_id(discount_model.brand_id)
    new_code = create_discount_code(brand["name"], user["username"], discount_model.id)

    new_code_model = DiscountCodeModel()
    new_code_model.discount_id = discount_model.id
    new_code_model.code = new_code
    new_code_model.user_id = user['id']

    return new_code_model
