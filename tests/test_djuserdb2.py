import pytest 

from django.contrib.auth.models import User

'''
@pytest.fixture()
def user_1(db):
    return User.objects.create_user("test-user")


@pytest.mark.django_db
def test_set_check_password(user_1):
    user_1.set_password("new-password")
    assert user_1.check_password("new-password") is True

'''

'''

@pytest.mark.django_db
def test_set_check_username1(user_2):
    assert user_2.username == "test-user" , "username does not match"

@pytest.mark.django_db
def test_set_check_username2(user_2):
    assert user_2.username == "test-user" , "username does not match"

'''

# def test_new_user(new_user):
#     print(new_user.first_name)
#     assert new_user.first_name == "Myname" , "first_name does not match"


# def test_new_staff_user(new_staff_user):
#     print(new_staff_user.is_staff)
#     assert new_staff_user.is_staff

# testing using factory 
'''
@pytest.mark.django_db
def test_new_build_user(user_factory):
    user = user_factory.build()
    count = User.objects.all().count()
    print(count)
    print(user.username)
    assert True


@pytest.mark.django_db
def test_new_create_user(user_factory):
    user = user_factory.create()
    count = User.objects.all().count()
    print(count)
    print(user.username)
    assert True 

'''

