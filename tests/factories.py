from unicodedata import category
import factory
from faker import Faker
from django.contrib.auth.models import User
# importing app1 models
from app1 import models


# faker library is used to generate fake data for db in django.

fake = Faker()

# Creating User Model factory using factory
class UserFactory(factory.django.DjangoModelFactory):
    class Meta :
        model = User
    
    username = fake.name()
    is_staff = True

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta :
        model = models.Category
    name = 'django'


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta :
        model = models.Product
    title = 'product_title'
    # re-replicating foreign key data of category
    category = factory.SubFactory(CategoryFactory)
    description = fake.text()
    slug = 'product_slug'
    regular_price = '9.99'
    discount_price = '4.99'
