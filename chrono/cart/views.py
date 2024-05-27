from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse
from django.contrib import messages

def cart_summary(request):
    """
    This View displays the cart summary page.

    :param request: The HTTP request object
    :return: It returns a rendered cart_summary_page that has cart products, quantities, and total
    """
    cart = Cart(request) # Initialize the shopping cart
    cart_products = cart.get_prods # Retrieve cart products and their details
    quantities = cart.get_quants  # Retrieve quantities of products in the cart
    totals = cart.cart_total() # Calculate the total cost of the items in the cart
     # Render the cart summary page with the cart details
    return render(request, "cart_summary.html", {"cart_products": cart_products, "quantities": quantities, "totals": totals})


def cart_add(request):
    """
    View that adds a product to the cart.

    :param request: The HTTP request object
    :return: Gives a JsonResponse with the updated cart quantity or error message
    """
    cart = Cart(request)

    # Fetches the cart and Check if the request is POST request
    if request.POST.get('action') == 'post':
        # Fetches product ID and quantity from the request
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        # Looksup product in the database
        product = get_object_or_404(Product, id=product_id)
        # Puts the product to the cart
        cart.add(product=product, quantity=product_qty)
        # Gets the new cart quantity
        cart_quantity = cart.__len__()
        # Return JsonResponse with the updated cart quantity
        response = JsonResponse({'qty': cart_quantity})
        messages.success(request, "Watch Added To Cart...")
        return response


def cart_delete(request):
    """
    View that deletes a product from the cart.

    :param request: The HTTP request object
    :return: gives a JsonResponse with the ID of the deleted product or error message
    """
    cart = Cart(request) # Initialize the shopping cart
    # Check whether the request is a POST request
    if request.POST.get('action') == 'post':
        # Gets product Identity from the request
        product_id = int(request.POST.get('product_id'))
        # Deletes product from the cart
        cart.delete(product=product_id)
        # Returns the JsonResponse with the ID of the deleted product
        response = JsonResponse({'product': product_id})
        messages.success(request, "Watch Removed From Shopping Cart...")
        return response


def cart_update(request):
    """
    View to update the quantity of a product in the cart.

    :param request: HTTP request object
    :return: JsonResponse with the updated quantity or error message
    """
    cart = Cart(request) # Initialize the shopping cart
    # Check if the request is a POST request
    if request.POST.get('action') == 'post':
        # Get product ID and new quantity from the request
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        # Puts the product quantity in the cart
        cart.update(product=product_id, quantity=product_qty)
        # Gives JsonResponse with the updated quantity
        response = JsonResponse({'qty': product_qty})
        messages.success(request, "Cart Has Been Updated...")
        return response
