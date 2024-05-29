from django.shortcuts import render
from .models import Product

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