from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import customform
from django.contrib.auth.views import LogoutView
from django.contrib.auth import logout

def register(request):
    if request.method == "POST":
        register_form = customform(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, "New Account Created")
            return redirect('login')
    else:
        register_form = customform()
    return render(request, 'register.html',{'register_form': register_form})

def custom_logout_view(request):
    if request.method == 'POST' or request.method == 'GET':
        logout(request)
        return redirect('home')  # Redirect to home page after logout
    else:
        return redirect('home')
