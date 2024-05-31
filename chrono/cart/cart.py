from store.models import Product
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

    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)

        if product_id in self.cart:
            pass
        else:
            #self.cart[product_id] = {'price': str(product.price)}
            self.cart[product_id] = int(product_qty)

        self.session.modified = True

    def __len__(self):
        """
        Returns the length of the cart attribute, which represents the number of items in the cart.

        :return: The length of the cart attribute.
        :rtype: int
        """
        return len(self.cart)

    def get_prods(self):
        """
        Returns a list of the keys in the cart attribute.

        :return: A list of the keys in the cart attribute.
        :rtype: list
        """
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        return products
    
    def get_quants(self):
        return quantities
    
    def update(self, product, quantity):
        product_id = str(product)
        product_qty = int(quantity)

        ourcart = self.cart
        ourcart[product_id] = product_qty

        self.session.modified = True

        thing = self.cart
        return thing
    
    def delete(self, product):
        """
        Deletes a product from the cart.

        Args:
            product (Any): The product to be deleted.

        Returns:
            None

        This function takes a product as an argument and deletes it from the cart. 
        It first converts the product to a string using the `str()` function. 
        Then, it checks if the product ID is present in the cart dictionary. 
        If it is, the product is deleted from the cart using the `del` keyword. 
        Finally, the `modified` attribute of the session is set to True to indicate that the session has been modified.
        """
        product_id = str(product)

        if product_id in self.cart:
            del self.cart[product_id]

        self.session.modified = True