from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def index(request):
    """
    This function renders the 'index.html' template when the 'home' view is accessed.
    """
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

def about(request):
    """
    This function renders the 'about.html' template when the 'about' view is accessed.
    """
    return render(request, 'about.html')

def login_user(request):
    """ A function that logs in the user"""
    if request.method == 'POST':
        '''Login user'''
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged in!')
            return redirect('index')
        else:
            messages.success(request, 'Error logging in')
            return redirect('login')
    else:
        return render(request, 'login.html', {})

def logout_user(request):
   """ A function that logs out the user"""
   logout(request)
   messages.success(request, 'You have been logged out!')
   return redirect('index')