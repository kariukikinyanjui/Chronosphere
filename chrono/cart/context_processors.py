from .cart import Cart

# This context processor ensures our cart can work on all pages of the site
def cart(request):
	# Return the default data from our Cart
	return {'cart': Cart(request)}
