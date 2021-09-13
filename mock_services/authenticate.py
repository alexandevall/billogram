
token_to_users = {
    'u1': {
        "username": "Per",
        'id': "some_user_id_1",
        'can_use_services': set(["get-discount-code"])
    },
    'u2': {
        "username": "Stina",
        'id': "some_user_id_2",
        'can_use_services': set(["get-discount-code"])
    },
    'u3': {
        "username": "Mohammed",
        'id': "some_user_id_3",
        'can_use_services': set(["view_discount_code"])
    },
}

token_to_brand = {
    'b1': {
        "id": "some_brand_id_1",
        'name': "Nike",
        'can_use_services': set(["create-discount-codes"])
    },
    'b2': {
        "id": "some_brand_id_2",
        'name': "Addidas",
        'can_use_services': set(["create-discount-codes"])
    },
    'b3': {
        "id": "some_brand_id_3",
        'name': "Puma",
        'can_use_services': set()
    }
}


def require_user(req, service):
    user_auth_token = req.headers.get('user_auth_token')
    user = token_to_users.get(user_auth_token)

    if not user:
        raise Exception('not logged in')

    if service in user['can_use_services']:
        return user
    else:
        raise Exception('cannot access this service')

def require_brand(req, service):
    brand_auth_token = req.headers.get('brand_auth_token')
    brand = token_to_brand.get(brand_auth_token)

    if not brand:
        raise Exception('not logged in')

    if service in brand['can_use_services']:
        return brand
    else:
        raise Exception('cannot access this service')
