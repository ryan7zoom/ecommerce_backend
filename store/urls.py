from django.urls import path
from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

urlpatterns = [
    # Homepage showing list of all products
    path('', views.product_list, name='product_list'),

    # Product details page (e.g., product with ID 5)
    path('product/<int:pk>/', views.product_detail, name='product_detail'),

    # View the current user's shopping cart
    path('cart/', views.cart_view, name='cart_view'),

    # Endpoint to update cart items (add/remove/change quantity)
    path('cart/update/', views.update_cart, name='update_cart'),

    # Login page for users like Ryan or Saba
    path('login/', views.login_view, name='login'),

    # Logout user and end session
    path('logout/', views.logout_view, name='logout'),

    # Registration page for new users
    path('register/', views.register_view, name='register'),

    # Checkout page to place orders
    path('checkout/', views.checkout_view, name='checkout'),

    # View past orders made by logged-in user
    path('orders/', views.order_history_view, name='order_history'),

    path('orders/<int:order_id>/mark_paid/', views.mark_order_paid, name='mark_order_paid'),

]
