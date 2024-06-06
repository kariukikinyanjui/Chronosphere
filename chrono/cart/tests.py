from django.test import TestCase, Client
from django.urls import reverse
from store.models import Product, Profile, User
from .cart import Cart
import json

class CartViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')

        # Check if a profile already exists for the user
        if not Profile.objects.filter(user=self.user).exists():
            self.profile = Profile.objects.create(user=self.user)
        else:
            self.profile = Profile.objects.get(user=self.user)

        self.product = Product.objects.create(name='Test Product', price=20.00, is_sale=False, sale_price=15.00)
        self.cart = Cart(self.client)


    def test_cart_summary_view(self):
        response = self.client.get(reverse('cart_summary'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart_summary.html')

    def test_cart_add_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('cart_add'), {
            'product_id': self.product.id,
            'product_qty': 2
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content)['qty'], 1)
        self.assertEqual(self.client.session['cart'][str(self.product.id)], 2)

    def test_cart_update_view(self):
        self.client.login(username='testuser', password='12345')
        self.client.post(reverse('cart_add'), {
            'product_id': self.product.id,
            'product_qty': 2
        })
        response = self.client.post(reverse('cart_update'), {
            'product_id': self.product.id,
            'product_qty': 5
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content)['qty'], 5)
        self.assertEqual(self.client.session['cart'][str(self.product.id)], 5)

    def test_cart_delete_view(self):
        self.client.login(username='testuser', password='12345')
        self.client.post(reverse('cart_add'), {
            'product_id': self.product.id,
            'product_qty': 2
        })
        response = self.client.post(reverse('cart_delete'), {
            'product_id': self.product.id
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content)['product'], self.product.id)
        self.assertNotIn(str(self.product.id), self.client.session['cart'])


class CartClassTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')

        # Check if a profile already exists for the user
        if not Profile.objects.filter(user=self.user).exists():
            self.profile = Profile.objects.create(user=self.user)
        else:
            self.profile = Profile.objects.get(user=self.user)

        self.product = Product.objects.create(name='Test Product', price=20.00, is_sale=False, sale_price=15.00)
        self.cart = Cart(self.client)

    def test_add_to_cart(self):
        self.cart.add(product=self.product, quantity=1)
        self.assertIn(str(self.product.id), self.client.session['cart'])
        self.assertEqual(self.client.session['cart'][str(self.product.id)], 1)

    def test_cart_total(self):
        self.cart.add(product=self.product, quantity=2)
        self.assertEqual(self.cart.cart_total(), 40.00)

    def test_cart_length(self):
        self.cart.add(product=self.product, quantity=1)
        self.assertEqual(len(self.cart), 1)

    def test_get_prods(self):
        self.cart.add(product=self.product, quantity=1)
        products = self.cart.get_prods()
        self.assertIn(self.product, products)

    def test_get_quants(self):
        self.cart.add(product=self.product, quantity=3)
        quantities = self.cart.get_quants()
        self.assertEqual(quantities[str(self.product.id)], 3)

    def test_update_cart(self):
        self.cart.add(product=self.product, quantity=1)
        self.cart.update(product=self.product.id, quantity=5)
        self.assertEqual(self.cart.cart[str(self.product.id)], 5)

    def test_delete_from_cart(self):
        self.cart.add(product=self.product, quantity=1)
        self.cart.delete(product=self.product.id)
        self.assertNotIn(str(self.product.id), self.cart.cart)
