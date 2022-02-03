import pytest 

'''
def test_new_user(create_newuser):
    print(create_newuser.username)
    assert True
    
'''
def test_product(db, product_factory):
    product = product_factory.create()
    print(product.description)
    assert True
    
