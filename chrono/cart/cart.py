class Cart():
    def __init__(self, request):
        """
        Initializes a new instance of the Cart class.

        Args:
            request (HttpRequest): The HTTP request object.

        Initializes the session attribute with the session from the request object.
        Retrieves the value associated with the key 'session_key' from the session.
        If the key 'session_key' is not present in the session, creates a new empty dictionary
        and assigns it to the key 'session_key' in the session.
        Sets the cart attribute to the retrieved or newly created dictionary.

        """
        self.session = request.session
        cart = self.session.get('session_key')

        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        self.cart = cart

    def add(self, product):
        product_id = str(product.id)

        if product_id not in self.cart:
            pass
        else:
            self.cart[product_id] = {'price': str(product.price)}

        self.session.modified = True