from django.db import models
import datetime

class Category(models.Model):
    """ Represents a category with a name field. """
    name = models.CharField(max_length=200)

    class Meta:
        """ Meta class for the Category model. """
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        """
        Returns a string representation of the Category object.
        """
        return self.name

    class Meta:
        """Metadata for the Category model."""
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
class Customer(models.Model):
    """ Represents a customer with a first name, last name, phone number, password, and email. """
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self):
        """
        Returns a string representation of the Customer object.
        """
        return f'{self.first_name} {self.last_name}'
    
class Product(models.Model):
    """ Represents a product with a name, price, and category. """
    name = models.CharField(max_length=200)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=400, null=True, blank=True, default='')
    image = models.ImageField(upload_to='uploadsproducts/', null=True, blank=True)

    def __str__(self):
        """
        Returns a string representation of the Product object.
        """
        return self.name
    
class Order(models.Model):
    """ Represents an order with a product, customer, quantity, address, phone, date, and status. """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=200, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        """
        Returns a string representation of the Order object.
        """
        return self.product
