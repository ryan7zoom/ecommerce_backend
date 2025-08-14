import pytest
from decimal import Decimal
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from store.models import Product, Order, OrderItem

@pytest.mark.django_db
def test_product_list_api(authenticated_api_client, create_test_products):
    url = reverse('product-list')
    response = authenticated_api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data['results']) == 2
    assert response.data['results'][0]['name'] == 'Laptop'

@pytest.mark.django_db
def test_product_create_api(authenticated_api_client, create_test_categories, staff_user):
    authenticated_api_client.force_authenticate(user=staff_user)

    url = reverse('product-list')
    category = create_test_categories[0]
    product_data = {
        'name': 'New Smartphone',
        'description': 'Latest model smartphone',
        'price': '699.99',
        'stock': 25,
        'category': category.id
    }

    response = authenticated_api_client.post(url, product_data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert Product.objects.count() == 1

    product =  Product.objects.first()
    assert product.name == 'New Smartphone'
    assert product.price == Decimal('699.99')
    assert product.category == category

@pytest.mark.django_db
def test_product_create_forbidden_for_regular_user(api_client, create_test_categories):
    url = reverse('product-list')
    category = create_test_categories[0]
    product_data = {
        'name': 'Unauthorized Product',
        'description': 'This should not be created',
        'price': '199.99',
        'stock': 10,
        'category': category.id
    }

    response = api_client.post(url, product_data, format='json')
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert Product.objects.count() == 0

