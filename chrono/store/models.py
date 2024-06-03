from django.db import models
import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save



class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        """
        Returns a string representation of the object.

        :return: A string representing the name of the object.
        :rtype: str
        """
        return self.name
    
class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=255)

    def __str__(self):
        """
        Returns a string representation of the object.

        :return: A string representing the name of the object.
        :rtype: str
        """
        return f'{self.first_name} {self.last_name}'
    
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=255, default='', null=True, blank=True)
    image = models.ImageField(upload_to='uploads/product/')

    #sales
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        """
        Returns a string representation of the object.

        :return: A string representing the name of the object.
        :rtype: str
        """
        return self.name
    
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    address = models.CharField(max_length=200, default='', null=True, blank=True)
    phone = models.CharField(max_length=200, default='', null=True, blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        """
        Returns a string representation of the object.

        :return: A string representing the name of the object.
        :rtype: str
        """
        return self.product

class Profile(models.Model):
    """
    Model representing additional information about a user.

    Attributes:
        user (User): One-to-one relationship with the User model.
        address1 (str): First line of the address.
        address2 (str): Second line of the address.
        city (str): City name.
        state (str): State or province name.
        zipcode (str): Postal code.
        country (str): Country name.
        old_cart (str): Previous cart data.
        phone (str): Phone number.

    Methods:
        __str__: Returns the username of the associated user.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address1 = models.CharField(max_length=200, blank=True)
    address2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    state = models.CharField(max_length=200, blank=True)
    zipcode = models.CharField(max_length=200, blank=True)
    country = models.CharField(max_length=200, blank=True)
    old_cart = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        """Return the username of the associated user."""
        return self.user.username
    
# Creates user Profile when user signs up as default
def create_profile(sender, instance, created, **kwargs):
	if created:
		user_profile = Profile(user=instance)
		user_profile.save()
# Automation
post_save.connect(create_profile, sender=User)