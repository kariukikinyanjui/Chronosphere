from store.models import Product

class Cart():
	def __init__(self, request):
		"""
        Initializes the Cart object.

        :param request: The HTTP request object
        """
		self.session = request.session
		self.request = request
		cart = self.session.get('session_key')

		# Create the cart if it doesn't exist
		if 'session_key' not in request.session:
			cart = self.session['session_key'] = {}
		self.cart = cart

	def db_add(self, product, quantity):
		""" Add product to the cart """
		product_id = str(product)
		product_qty = str(quantity)

		if product_id in self.cart:
			pass
		else:
			#self.cart[product_id] = {'price': str(product.price)}
			self.cart[product_id] = int(product_qty)

		self.session.modified = True


		# Deal with logged in user
		if self.request.user.is_authenticated:
			# Get the current user profile
			current_user = Profile.objects.filter(user__id=self.request.user.id)
			carty = str(self.cart)
			carty = carty.replace("\'", "\"")
			current_user.update(old_cart=str(carty))


	def add(self, product, quantity):
		"""
		Adds a product to the cart.

		:param product: The product to be added.
		:type product: Product
		:param quantity: The quantity of the product to be added.
		:type quantity: int
		""" 
		product_id = str(product.id)
		product_qty = str(quantity)

		if product_id in self.cart:
			pass
		else:
			self.cart[product_id] = {'price': str(product.price)}
			self.cart[product_id] = int(product_qty)

		self.session.modified = True

		# Deal with logged in user
		if self.request.user.is_authenticated:
			current_user = Profile.objects.filter(user__id=self.request.user.id)
			carty = str(self.cart)
			carty = carty.replace("\'", "\"")
			current_user.update(old_cart=str(carty))

	def cart_total(self):
		"""
		Calculate the total cost of the items in the cart.

		Returns:
		    float: The total cost of the items in the cart.

		"""
		product_ids = self.cart.keys()
		products = Product.objects.filter(id__in=product_ids)
		quantities = self.cart
		total = 0

		for key, value in quantities.items():
			# Convert from string to int
			key = int(key)
			for product in products:
				if product.id == key:
					if product.is_sale:
						total = total + (product.sale_price * value)
					else:
						total = total + (product.price * value)
		return total

		#Get the length of the cart and return it
	def __len__(self):
		"""
		Returns the length of the cart.

		Returns:
		    int: The length of the cart.
		"""
		return len(self.cart)

	def get_prods(self):
		"""
		Get the products in the cart.

		Returns:
		    QuerySet: A queryset of Product objects in the cart.
		"""
		product_ids = self.cart.keys()
		products = Product.objects.filter(id__in=product_ids)

		return products

	def get_quants(self):
		"""
		Get the quantities of items in the cart.

		Returns:
		    dict: A dictionary containing the quantities of items in the cart.
		"""
		quantities = self.cart
		return quantities

	def update(self, product, quantity):
		"""
		Updates the quantity of a product in the cart.

		:param product: The product to be updated.
		:type product: str
		:param quantity: The new quantity of the product.
		:type quantity: int
		:return: The updated cart.
		:rtype: dict
		"""
		product_id = str(product)
		product_qty = int(quantity)

		# Get cart
		ourcart = self.cart
		# add Dictionary/cart
		ourcart[product_id] = product_qty

		self.session.modified = True


		# Deal with logged in user
		if self.request.user.is_authenticated:
			current_user = Profile.objects.filter(user__id=self.request.user.id)
			carty = str(self.cart)
			carty = carty.replace("\'", "\"")
			current_user.update(old_cart=str(carty))


		thing = self.cart
		return thing

	def delete(self, product):
		"""
		Deletes a product from the cart.

		:param product: The product to be deleted.
		:type product: Any
		""" 
		product_id = str(product)

		if product_id in self.cart:
			del self.cart[product_id]

		self.session.modified = True

		# logged in user
		if self.request.user.is_authenticated:
			current_user = Profile.objects.filter(user__id=self.request.user.id)
			carty = str(self.cart)
			carty = carty.replace("\'", "\"")
			current_user.update(old_cart=str(carty))
