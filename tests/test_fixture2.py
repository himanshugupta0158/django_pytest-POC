'''import pytest 

@pytest.fixture
def yield_fixture():
    # execute first before every test/function/method
    print("Start test phase")
    yield 6
    # execute last after every test/function/method
    print("End test phase")
    

def test_example1(yield_fixture):
    print('run-example-1')
    assert yield_fixture == 6
    
def test_example2(yield_fixture):
    print('run-example-2')
    assert yield_fixture == 6
    
'''