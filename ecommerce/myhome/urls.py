from myhome import views
from django.urls import path, include

urlpatterns =[
    path('home/', views.home , name = 'home'),
     path('add-to-cart/<int:product_id>/', views.add_to_cart_view, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('cart/update/<int:product_id>/', views.update_cart_view, name='update_cart'),
    path('cart/remove/<int:product_id>/', views.remove_from_cart_view, name='remove_from_cart'),
]