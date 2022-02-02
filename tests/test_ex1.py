import pytest

'''
@pytest.mark.slow
def test_example():
    print("test1")
    assert 1 == 1
 
    
def test_example1():
    assert 1 == 2

'''
""" 
A pattern for writing tests : 
-> Arrange
In this state ,we need to prepare any state we will need to
perform the action you want to try.does the test require 
any objects or special setting, db , do we need to connect to
our api.
The arrange state is trying to prepare in readiness to then 
perform the action.
-> Act
also called action
In this, we are calling a method or function or may be calling
a rest api or interacting a web page.
ex : Typically the act step should elicit some sort of response.
like http response.
-> Assert
In this case ,we want to assert expected outcomes.
now we can take the response from action /act the second
phase and we can test it against known expected putcome.
"""

""" 
What are pytest fixtures ?
-> pytest fixtures are just functions.
-> Run before/after each test function to which the fixtures
is applied.

"""


