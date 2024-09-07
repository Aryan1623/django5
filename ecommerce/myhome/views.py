from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product, CartItem
from .cart_utils import add_to_cart, remove_from_cart, update_cart_item

# Home view
def home(request):
    return render(request, 'home.html')

# Add to cart view
@login_required
def add_to_cart_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)  # Ensure product exists
    add_to_cart(request.user, product_id)
    return redirect('view_cart')

# View cart view
@login_required
def view_cart(request):
    cart_items = CartItem.objects.filter(cart__user=request.user)
    total = sum(item.get_total_price() for item in cart_items)
    return render(request, 'cart/view_cart.html', {'cart_items': cart_items, 'total': total})

# Update cart item quantity view
@login_required
def update_cart_view(request, product_id):
    if request.method == 'POST':
        try:
            quantity = int(request.POST.get('quantity', 1))
            if quantity < 1:
                quantity = 1  # Set minimum quantity to 1
        except ValueError:
            quantity = 1  # Handle invalid input
        update_cart_item(request.user, product_id, quantity)
    return redirect('view_cart')

# Remove from cart view
@login_required
def remove_from_cart_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)  # Ensure product exists
    remove_from_cart(request.user, product_id)
    return redirect('view_cart')


