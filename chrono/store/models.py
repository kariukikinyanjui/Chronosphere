from django.db import models
import datetime


class Category(models.Model):
    name = models.CharField(max_length=55)

    def __str__(self):
        """
        Returns a string representation of the object.

        :return: A string representing the name of the object.
        :rtype: str
        """
        return self.name

class Customer(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    email = models.EmailField()
    phone = models.CharField(max_length=55)
    password = models.CharField(max_length=255)
    
    def __str__(self):
        """
        Returns a string representation of the object.

        :return: A string representing the name of the object.
        :rtype: str
        """
        return f'{self.last_name}, {self.first_name}'


class Product(models.Model):
    name = models.CharField(max_length=55)
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=500, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/product/')

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
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=500, default='', blank=True)
    phone = models.CharField(max_length=55, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        """
        Returns a string representation of the object.

        :return: A string representing the name of the object.
        :rtype: str
        """
        return self.product