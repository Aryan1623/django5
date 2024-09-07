"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from myhome import views as the_views
from user_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', the_views.home, name='home'),
    path('user/', include('user_app.urls')),
    path('add-to-cart/<int:product_id>/', the_views.add_to_cart_view, name='add_to_cart'),
    path('cart/', the_views.view_cart, name='view_cart'),
    path('cart/update/<int:product_id>/', the_views.update_cart_view, name='update_cart'),
    path('cart/remove/<int:product_id>/', the_views.remove_from_cart_view, name='remove_from_cart'),
]
