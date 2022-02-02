'''import pytest

"""
Fixtures are the functions that executes/run either before ,
after or both each test functions to which fixtures is applied.

Importance :
> Fixtures are used to feed data to the tests such as database
connections ,URLs to test and input data.

What is Factory Boy ?
-> Factory boy is the fixture replacement tool.
-> Factories are defined in a nice , clean and readable manner.
-> Easy-to-use factories for complex objects.
-> Class-based approach:
    -> SubFactories
    -> ForeignKey , reverseForeignKey , ManyToMany


"""


# function -> Run once per test
# class    -> Run once per class of test
# module   -> Run once per module
# session  -> Run once per session  


# flagging below fixture

# below fixture will run everytime new function invoke fixture.
@pytest.fixture
def fixture_1():
    print("run-fixture-1")
    return 1


def test_example1(fixture_1):
    print("run-example-1")
    num = fixture_1
    assert num == 1
    
def test_example2(fixture_1):
    print("run-example-2")
    num = fixture_1
    assert num == 1


# below fixture will run only once no-matter how many functions
# invoke it repeateadly 
@pytest.fixture(scope="session")
def fixture_2():
    print("run-fixture-2")
    return 2
    
def test_example3(fixture_2):
    print("run-example-3")
    num = fixture_2
    assert num == 2
    
def test_example4(fixture_2):
    print("run-example-4")
    num = fixture_2
    assert num == 2
    
'''