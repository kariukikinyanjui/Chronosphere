from .cart import Cart

def cart(request):
    """
    Returns a dictionary containing a single key-value pair. The key is 'cart' and the value is an instance of the Cart class initialized with the given request object.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        dict: A dictionary containing a single key-value pair. The key is 'cart' and the value is an instance of the Cart class initialized with the given request object.
    """
    return {'cart': Cart(request)}