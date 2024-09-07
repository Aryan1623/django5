from .models import Cart, CartItem, Product

def get_or_create_cart(user):
    cart, created = Cart.objects.get_or_create(user=user)
    return cart

def add_to_cart(user, product_id, quantity=1):
    cart = get_or_create_cart(user)
    product = Product.objects.get(id=product_id)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not created:
        cart_item.quantity += quantity
    cart_item.save()

def remove_from_cart(user, product_id):
    cart = get_or_create_cart(user)
    cart_item = CartItem.objects.filter(cart=cart, product_id=product_id).first()

    if cart_item:
        cart_item.delete()

def update_cart_item(user, product_id, quantity):
    cart = get_or_create_cart(user)
    cart_item = CartItem.objects.filter(cart=cart, product_id=product_id).first()

    if cart_item:
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
        else:
            cart_item.delete()