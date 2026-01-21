from app.main import (
    create_table,
    insert_product,
    update_product,
    delete_product,
    get_products
)

def test_crud_operations():
    create_table()

    product_id = insert_product("Apple", 10)
    products = get_products()
    assert ("Apple", 10) in products

    update_product(product_id, 20)
    products = get_products()
    assert ("Apple", 20) in products

    delete_product(product_id)
    products = get_products()
    assert ("Apple", 20) not in products