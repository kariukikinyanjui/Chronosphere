from django.shortcuts import render
from .models import Product

def index(request):
    """
    This function renders the 'index.html' template when the 'home' view is accessed.
    """
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})