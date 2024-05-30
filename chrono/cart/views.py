from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse

def cart_summary(request):
    """
    Renders the 'cart_summary' template and returns the rendered HTML as a response.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML response.
    """
    return render(request, 'cart_summary.html', {})



def cart_update(request):
    """
    Renders the 'cart_update' template and returns the rendered HTML as a response.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML response.
    """
    pass


def cart_delete(request):
    """
    Renders the 'cart_delete' template and returns the rendered HTML as a response.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML response.
    """
    pass

def cart_add(request):
    """
    Renders the 'cart_add' template and returns the rendered HTML as a response.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML response.
    """
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product)

        cart_quantity = cart.__len__()

        response = JsonResponse({'qty': cart_quantity}) 
        return response      
