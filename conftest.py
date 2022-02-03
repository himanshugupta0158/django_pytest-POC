import pytest
from django.contrib.auth.models import User

# for registering factory
from pytest_factoryboy import register
from tests.factories import UserFactory , ProductFactory , CategoryFactory


'''

@pytest.fixture()
def user_2(db):
    user = User.objects.create_user("test-user")
    print('create-user')
    return user



# here we are creating user factory
@pytest.fixture
def new_user_factory(db):
    def create_app_user(
        username : str ,
        password : str = None,
        first_name : str = "firstname",
        last_name : str = "lastname",
        email :str = "test@test.com",
        is_staff : bool = False,
        is_superuser : bool = False,
        is_active : bool = True,          
    ):
        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active = is_active
        )
        return user
    return create_app_user


@pytest.fixture
def new_user(db , new_user_factory):
    return new_user_factory("Test_user" , "password" , "Myname")

@pytest.fixture
def new_staff_user(db , new_user_factory):
    return new_user_factory("Test_user" , "password" , "Myname" , is_staff=True)

'''



# registering factory
register(UserFactory)
register(ProductFactory)
register(CategoryFactory)

@pytest.fixture
def build_newuser(db, user_factory):
    user = user_factory.build()
    return user



@pytest.fixture
def create_newuser(db, user_factory):
    user = user_factory.create()
    return user






