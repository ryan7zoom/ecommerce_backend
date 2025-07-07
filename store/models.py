from django.db import models
from django.contrib.auth.models import User

# Product category (e.g., Electronics, Clothing)
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Category name, must be unique
    slug = models.SlugField(max_length=100, unique=True) # URL-friendly version of name

    def __str__(self):
        return self.name  # Show category name in admin or shell

# Product for sale (e.g., iPhone, T-Shirt)
class Product(models.Model):
    name = models.CharField(max_length=200)                # Product name
    description = models.TextField()                        # Detailed product description
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price (e.g., 299.99)
    image = models.ImageField(upload_to='product/', blank=True, null=True)  # Product image
    stock = models.PositiveIntegerField(default=0)         # How many available in stock
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')  # Link to category
    created_at = models.DateTimeField(auto_now_add=True)   # When product was added
    updated_at = models.DateTimeField(auto_now=True)       # Last update time

    def __str__(self):
        return self.name  # Show product name

# Customer order (e.g., Ryan’s order #1024)
class Order(models.Model):
    # Possible order statuses
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('placed', 'Placed'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Who placed the order
    name = models.CharField(max_length=200)                   # Name for shipping (could be different from user)
    address = models.TextField()                               # Shipping address
    phone = models.CharField(max_length=20)                    # Contact phone number
    total = models.DecimalField(max_digits=10, decimal_places=2)  # Total order price
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')  # Order status
    created_at = models.DateTimeField(auto_now_add=True)       # When order was created

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"  # Example: "Order #1024 by ryan123"

# Each item inside an order (e.g., 2 x T-Shirts)
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')  # Which order this belongs to
    product = models.ForeignKey(Product, on_delete=models.CASCADE)                     # Product ordered
    quantity = models.PositiveIntegerField()                                          # How many units ordered
    price = models.DecimalField(max_digits=10, decimal_places=2)                      # Price per unit at purchase time

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"  # Example: "T-Shirt x 2"
