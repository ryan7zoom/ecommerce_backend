import pytest
from store.models import Category, Product, Order, OrderItem
from decimal import Decimal

@pytest.mark.django_db
class TestCategoryModel:

    def test_category_creation(self):
        category = Category.objects.create(name='Electronics', slug='electronics')
        assert category.name == 'Electronics', f"Expected name 'Electronics', got '{category.name}'"
        assert category.slug == 'electronics', f"Expected slug 'electronics', got '{category.slug}'"
        assert str(category) == 'Electronics'

    def test_category_name_unique(self):
        Category.objects.create(name='Electronics', slug='electronics')
        with pytest.raises(Exception):
            Category.objects.create(name='Electronics', slug='electronics-2')

@pytest.mark.django_db
class TestProductModel:
    def test_product_creation(self, create_test_categories):
        category = create_test_categories[0]

        product = Product.objects.create(
            name='Django for beginners',
            description='A good fucking book is what it is.',
            price=Decimal('29.99'),
            stock=50,
            category=category
        )

        assert product.name == 'Django for beginners'
        assert product.description == 'A good fucking book is what it is.'
        assert product.price == Decimal('29.99')
        assert product.stock == 50
        assert product.category == category

        assert product.created_at is not None
        assert product.updated_at is not None
        assert str(product) == 'Django for beginners'

        
@pytest.mark.django_db
class TestOrderModel:
    def test_order_creation(self, test_user):
        order = Order.objects.create(
            user=test_user,
            name='Test Customer',
            address='123 Test Street',
            phone='123-456-789',
            total=Decimal('59.97')
        )
        assert order.user == test_user
        assert order.name == 'Test Customer'
        assert order.address == '123 Test Street'
        assert order.phone == '123-456-789'
        assert order.total == Decimal('59.97')
        expected_str = f"Order #{order.id} by {test_user.username}"
        assert str(order) == expected_str



@pytest.mark.django_db
class TestOrderItemModel:
    def test_order_item_creation(self, create_test_order, create_test_products):
        order = create_test_order
        product = create_test_products[0]
        order_item = OrderItem.objects.create(
            order=order,
            product=product,
            quantity=2,
            price=Decimal('15.50')
        )
        assert order_item.order == order
        assert order_item.product == product
        assert order_item.quantity == 2
        assert order_item.price == Decimal('15.50')
        expected_str = f"{order_item.product.name} x {order_item.quantity}"
        assert str(order_item) == expected_str

    def test_order_item_relationship(self, create_test_order, create_test_products):
        order = create_test_order
        product = create_test_products[0]

        order_item = OrderItem.objects.create(
            order=order,
            product=product,
            quantity=3,
            price=product.price,
        )

        assert order_item in order.items.all()
        items_in_order = list(order.items.all())
        assert len(items_in_order) >= 1
        assert order_item in items_in_order
        assert order_item.order == order
        assert order_item.product == product

    