import pytest
from django.contrib.auth.models import User
from store.models import Category, Product, Order
from django.test import client
from decimal import Decimal
from rest_framework.test import APIClient


@pytest.fixture
def test_user(db):
    return User.objects.create_user(username='test_user', password='pass123')

@pytest.fixture
def staff_user(db):
    return User.objects.create_user(username='staffuser', password='staffpass123', is_staff=True)

@pytest.fixture
def other_user(db):
    return User.objects.create_user(username='otheruser',  password='otherpass123')

@pytest.fixture
def create_test_categories(db):
    category1 = Category.objects.create(name='Electronic', slug='electronic')
    category2 = Category.objects.create(name='Fish', slug='fish')
    return category1, category2

@pytest.fixture
def create_test_products(db, create_test_categories):
    category1, category2 = create_test_categories
    product1 = Product.objects.create(name='Laptop', description='A powerful laptop.', price=999.99, stock=10, category=category1)
    product2 = Product.objects.create(name='Rui', description='A fucking fish.', price=9.99, stock=100, category=category2)
    return product1, product2

@pytest.fixture
def create_test_order(db, test_user):
    order = Order.objects.create(
        user=test_user,
        name='Some Guy',
        address='123 Random Street',
        phone='344-777-888',
        total=Decimal('59.98')
    )
    return order

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def authenticated_api_client(test_user):
    from rest_framework.test import APIClient 
    client = APIClient()
    client.force_authenticate(user=test_user)
    return client


