from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse
from django.contrib import messages

def cart_summary(request):
    """
    View to display the cart summary page.

    :param request: HTTP request object
    :return: Rendered cart summary page with cart products, quantities, and total
    """
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants
    totals = cart.cart_total()
    return render(request, "cart_summary.html", {"cart_products": cart_products, "quantities": quantities, "totals": totals})


def cart_add(request):
    """
    View to add a product to the cart.

    :param request: HTTP request object
    :return: JsonResponse with the updated cart quantity or error message
    """
    cart = Cart(request)

    # Check if the request is a POST request
    if request.POST.get('action') == 'post':
        # Get product ID and quantity from the request
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        # Lookup product in the database
        product = get_object_or_404(Product, id=product_id)

        # Add product to the cart
        cart.add(product=product, quantity=product_qty)

        # Get updated cart quantity
        cart_quantity = cart.__len__()

        # Return JsonResponse with the updated cart quantity
        response = JsonResponse({'qty': cart_quantity})
        messages.success(request, "Product Added To Cart...")
        return response


def cart_delete(request):
    """
    View to delete a product from the cart.

    :param request: HTTP request object
    :return: JsonResponse with the ID of the deleted product or error message
    """
    cart = Cart(request)

    # Check if the request is a POST request
    if request.POST.get('action') == 'post':
        # Get product ID from the request
        product_id = int(request.POST.get('product_id'))

        # Delete product from the cart
        cart.delete(product=product_id)

        # Return JsonResponse with the ID of the deleted product
        response = JsonResponse({'product': product_id})
        messages.success(request, "Item Deleted From Shopping Cart...")
        return response


def cart_update(request):
    """
    View to update the quantity of a product in the cart.

    :param request: HTTP request object
    :return: JsonResponse with the updated quantity or error message
    """
    cart = Cart(request)

    # Check if the request is a POST request
    if request.POST.get('action') == 'post':
        # Get product ID and new quantity from the request
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        # Update the product quantity in the cart
        cart.update(product=product_id, quantity=product_qty)

        # Return JsonResponse with the updated quantity
        response = JsonResponse({'qty': product_qty})
        messages.success(request, "Your Cart Has Been Updated...")
        return response
