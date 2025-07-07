from django.contrib import admin
from .models import Product, Category
from .models import Order, OrderItem

# Register Product and Category models to show in Django admin
admin.site.register(Product)
admin.site.register(Category)

# Inline display for OrderItem inside Order admin (like showing items in one order)
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0  # No extra empty rows when adding items

# Custom admin panel for Orders
class OrderAdmin(admin.ModelAdmin):
    # Columns to show in the order list (order ID, user, status, total price, date)
    list_display = ('id', 'user', 'status', 'total', 'created_at')
    
    # Filters on the right to quickly filter by status, date, or user
    list_filter = ('status', 'created_at', 'user')
    
    # Search box to find orders by user’s username or order ID
    search_fields = ('user__username', 'id')
    
    # Show order items inline inside order details page
    inlines = [OrderItemInline]
    
    # Allow changing order status directly from the list view
    list_editable = ('status', )

# Register Order model with the custom OrderAdmin class
admin.site.register(Order, OrderAdmin)

# Register OrderItem separately (can be edited individually if needed)
admin.site.register(OrderItem)
