from django.shortcuts import render

from .models import Product


def index(request):
    """This function renders the 'index.html' template when the 'home' view is accessed.

    :param request:

    """
    products = Product.objects.all()
    return render(request, "index.html", {"products": products})


def about(request):
    """This function renders the 'about.html' template when the 'about' view is accessed.

    :param request:

    """
    return render(request, "about.html")
