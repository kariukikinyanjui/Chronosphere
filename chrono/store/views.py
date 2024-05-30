from django.shortcuts import render, redirect
from .models import Product, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm



def index(request):
    """
    Renders the 'index.html' template and returns the rendered HTML as a response.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML response.
    """
    products = Product.objects.all()
    return render(request, 'index.html',{'products': products})

def about(request):
    """
    Renders the 'about.html' template and returns the rendered HTML as a response.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML response.
    """
    return render(request, 'about.html', {})

def login_user(request):
    """
    Renders the 'login.html' template and returns the rendered HTML as a response.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML response.
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged in!')
            return redirect('index')
        else:
            messages.success(request, 'Error logging in. Please try again.')
            return redirect('login')
    else:
        return render(request, 'login.html', {})

def logout_user(request):
    """ 
    Logs out the user and redirects to the index page.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML response.
    """
    logout(request)
    messages.success(request, 'You have been logged out!')
    return redirect('index')

def register_user(request):
    """
    Renders the 'register.html' template and returns the rendered HTML as a response.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML response.
    """
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You have successfully registered!')
            return redirect('index')
        else:
            messages.error(request, 'Unable to register your account at this time. Please try again later.')
            return redirect('register')
    else:
        return render(request, 'register.html', {'form': form})
    

def product(request, pk):
    """
    Retrieves a specific product from the database based on the given primary key and renders the 'product.html' template with the product as a context variable.

    Parameters:
        request (HttpRequest): The HTTP request object.
        pk (int): The primary key of the product to retrieve.

    Returns:
        HttpResponse: The rendered HTML response containing the 'product.html' template with the product as a context variable.
    """
    product = Product.objects.get(id=pk)
    return render(request, 'product.html',{'product': product})

def category(request, abc):
    """
    Retrieves products from the database based on the given category and renders the 'category.html' template with the products as a context variable.

    Parameters:
        request (HttpRequest): The HTTP request object.
        abc (str): The category to filter products by.

    Returns:
        HttpResponse: The rendered HTML response containing the 'category.html' template with the products as a context variable.
    """
    abc = abc.replace('-', ' ')
    try:
        category = Category.objects.get(name=abc)
        products = Product.objects.filter(category=category)
        return render(request, 'category.html', {'products': products, 'category': category, 'products': products})
    except:
        messages.success(request, 'Category does not exist')
        return redirect('index')