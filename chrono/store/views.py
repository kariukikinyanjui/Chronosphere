from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

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