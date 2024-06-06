from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import ShippingAddress
from .forms import ShippingForm

class ShippingAddressModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.shipping_address = ShippingAddress.objects.create(
            user=self.user,
            shipping_full_name='John Doe',
            shipping_email='john@example.com',
            shipping_address1='123 Main St',
            shipping_address2='Apt 4B',
            shipping_city='Anytown',
            shipping_state='CA',
            shipping_zipcode='12345',
            shipping_country='USA'
        )

    def test_shipping_address_creation(self):
        self.assertTrue(isinstance(self.shipping_address, ShippingAddress))
        self.assertEqual(str(self.shipping_address), f'Shipping Address - {self.shipping_address.id}')


class ShippingFormTest(TestCase):
    def test_valid_shipping_form(self):
        form_data = {
            'shipping_full_name': 'John Doe',
            'shipping_email': 'john@example.com',
            'shipping_address1': '123 Main St',
            'shipping_address2': 'Apt 4B',
            'shipping_city': 'Anytown',
            'shipping_state': 'CA',
            'shipping_zipcode': '12345',
            'shipping_country': 'USA'
        }
        form = ShippingForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_shipping_form(self):
        form_data = {
            'shipping_full_name': '',
            'shipping_email': 'john@example.com',
            'shipping_address1': '',
            'shipping_city': 'Anytown',
            'shipping_country': 'USA'
        }
        form = ShippingForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 2)  # 'shipping_full_name' and 'shipping_address1' are required


class PaymentSuccessViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_payment_success_view(self):
        response = self.client.get(reverse('payment_success'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'payment/payment_success.html')
