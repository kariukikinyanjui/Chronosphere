from django.db import models
from django.contrib.auth.models import User

class ShippingAddress(models.Model): 
	"""
    A model representing a user's shipping address for order fulfillment.

    This model stores information about a user's shipping address, including their full name, 
    email address, city, state (optional), zip code (optional), address lines, and country.

    Attributes:
        user (ForeignKey): A foreign key relation to the User model, indicating the user 
            this address belongs to (nullable and blank).
        full_name (CharField): The full name of the recipient.
        email (CharField): The email address of the recipient.
        city (CharField): The city where the address is located.
        state (CharField): The state of the address (nullable and blank).
        zipcode (CharField): The zip code of the address (nullable and blank).
        address1 (CharField): The first line of the street address.
        address2 (CharField): The second line of the street address (nullable and blank).
        country (CharField): The country where the address is located.
    """
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	shipping_full_name = models.CharField(max_length=200)
	shipping_email = models.CharField(max_length=245)
	shipping_city = models.CharField(max_length=250)
	shipping_state = models.CharField(max_length=200, null=True, blank=True)
	shipping_zipcode = models.CharField(max_length=245, null=True, blank=True)
	shipping_address1 = models.CharField(max_length=275)
	shipping_address2 = models.CharField(max_length=254, null=True, blank=True)
	shipping_country = models.CharField(max_length=250)



	class Meta:
		verbose_name_plural = "Shipping Address"

	def __str__(self):
		return f'Shipping Address - {str(self.id)}'