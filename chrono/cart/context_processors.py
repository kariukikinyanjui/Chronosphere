from .cart import Cart

# Fetches the cart from the session
def cart(request):
	"""
	Returns a dictionary containing a single key-value pair. The key is 'cart' and the value is an instance of the Cart class initialized with the given request object.

	:param request: The HTTP request object.
	:type request: django.http.HttpRequest
	:return: A dictionary containing a single key-value pair. The key is 'cart' and the value is an instance of the Cart class initialized with the given request object.
	:rtype: dict
	"""
	return {'cart': Cart(request)}
