
id_to_brands  = {
    'some_brand_id_1': {
        'name': "Nike",
    },
    'some_brand_id_2': {
        'name': "Addidas",
    },
    'some_brand_id_3': {
        'name': "Puma",
    }
}

def get_brand_for_id(id):
    return id_to_brands.get(id)
