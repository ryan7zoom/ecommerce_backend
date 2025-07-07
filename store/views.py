# Import shortcuts to render templates, get an object or show 404 error, and redirect users
from django.shortcuts import render, get_object_or_404, redirect

# Import models to access Products, Categories, Orders, and OrderItems in the database
from .models import Product, Category, Order, OrderItem

# Decorator to restrict views to POST requests only (security for form actions)
from django.views.decorators.http import require_POST

# Decorators to require user login or check if user is staff (admin)
from django.contrib.auth.decorators import login_required, user_passes_test

# Django's authentication functions to handle login, logout, and user authentication
from django.contrib.auth import authenticate, login, logout

# Import User model to create and manage users
from django.contrib.auth.models import User

# Import messaging framework to display flash messages like 'Order placed!'
from django.contrib import messages


# Show all products and categories on homepage (like Amazon main page)
def product_list(request):
    products = Product.objects.all()          # All products (e.g., Laptop, Phone)
    categories = Category.objects.all()       # All categories (e.g., Electronics)
    return render(request, 'store/product_list.html', {'products': products, 'categories': categories})

# Show details for one product (e.g., Laptop)
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)   # Find product by ID (pk)
    if request.method == "POST":
        quantity = int(request.POST.get('quantity', 1))  # How many to add (default 1)
        cart = request.session.get('cart', {})           # Get current session cart
        if str(pk) in cart:
            cart[str(pk)] += quantity                     # Increase quantity if already in cart
        else:
            cart[str(pk)] = quantity                       # Add new product to cart
        request.session['cart'] = cart                     # Save cart back to session
        return redirect('cart_view')                       # Redirect to cart page
    return render(request, 'store/product_detail.html', {'product': product})

# Show the cart page with items user added
def cart_view(request):
    cart = request.session.get('cart', {})                 # Get cart from session
    products = Product.objects.filter(pk__in=cart.keys())  # Get products in cart
    cart_items = []
    total = 0
    for product in products:
        qty = cart[str(product.pk)]                         # Quantity of this product
        subtotal = product.price * qty                       # Price * quantity
        total += subtotal                                    # Add to total cost
        cart_items.append({'product': product, 'quantity': qty, 'subtotal': subtotal})
    return render(request, 'store/cart.html', {'cart_items': cart_items, 'total': total})

# Update cart (increase, decrease, remove products)
@require_POST  # Only allow POST for safety
def update_cart(request):
    product_id = str(request.POST.get('product_id'))  # Product to update (by ID)
    action = request.POST.get('action')                # What to do: increase, decrease, remove
    cart = request.session.get('cart', {})

    if product_id in cart:
        if action == 'increase':
            cart[product_id] += 1       # Add one more of the product
        elif action == 'decrease':
            cart[product_id] -= 1       # Remove one
            if cart[product_id] <= 0:
                del cart[product_id]    # Remove from cart if zero or less
        elif action == 'remove':
            del cart[product_id]        # Remove all of this product

    request.session['cart'] = cart   # Save updated cart
    return redirect('cart_view')     # Go back to cart page

# Handle user login (Ryan or Saba logging in)
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']       # Get username from form
        password = request.POST['password']       # Get password from form
        user = authenticate(request, username=username, password=password)  # Check user/pass
        if user is not None:
            login(request, user)                   # Log in user
            return redirect('product_list')       # Go to homepage
        else:
            return render(request, 'store/login.html', {'error': 'Invalid username or password.'})
    return render(request, 'store/login.html')

# Handle user logout
def logout_view(request):
    logout(request)                    # End user session
    return redirect('product_list')   # Go to homepage

# Handle new user registration (Saba creating account)
def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']   # Get desired username
        password = request.POST['password']   # Get desired password

        if User.objects.filter(username=username).exists():
            # Show error if username already exists
            return render(request, 'store/register.html', {'error': 'Username already exists. Please choose another.'})

        user = User.objects.create_user(username=username, password=password)  # Create user
        login(request, user)                   # Log in right after registering
        return redirect('product_list')       # Go to homepage
    return render(request, 'store/register.html')

# Checkout page for placing orders (Saba buying items)
@login_required
def checkout_view(request):
    cart = request.session.get('cart', {})                 # Get cart
    products = Product.objects.filter(pk__in=cart.keys())  # Get products in cart
    cart_items = []
    total = 0
    for product in products:
        qty = cart[str(product.pk)]                         # Quantity
        subtotal = product.price * qty                       # Price * qty
        total += subtotal                                    # Add to total
        cart_items.append({'product': product, 'quantity': qty, 'subtotal': subtotal})

    if request.method == 'POST':
        name = request.POST['name']         # Shipping name
        address = request.POST['address']   # Shipping address
        phone = request.POST['phone']       # Contact phone

        # Create new Order in DB with status pending
        order = Order.objects.create(
            user=request.user,
            name=name,
            address=address,
            phone=phone,
            total=total,
            status='pending'
        )

        # Create OrderItems for each product in cart
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item['product'],
                quantity=item['quantity'],
                price=item['product'].price
            )

        request.session['cart'] = {}  # Clear cart after order
        return render(request, 'store/checkout_success.html', {'order': order})

    # Show checkout form and summary
    return render(request, 'store/checkout.html', {'cart_items': cart_items, 'total': total})

# Show logged-in user's past orders (e.g., Saba's orders)
@login_required
def order_history_view(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')  # Get user's orders newest first
    return render(request, 'store/order_history.html', {'orders': orders})

# Admin-only: Mark an order as paid (simulate payment)
@user_passes_test(lambda u: u.is_staff)
def mark_order_paid(request, order_id):
    order = get_object_or_404(Order, id=order_id)  # Get order by ID
    if request.method == 'POST':
        order.status = 'placed'   # Mark order as placed/paid
        order.save()
        return redirect('order_history')
    return render(request, 'store/mark_paid_confirm.html', {'order': order})
