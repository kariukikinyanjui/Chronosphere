from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Category, Customer, Product, Order, Profile
from .forms import SignUpForm, UpdateUserForm, ChangePasswordForm, UserInfoForm

class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Electronics")

    def test_category_creation(self):
        self.assertEqual(self.category.name, "Electronics")
        self.assertEqual(str(self.category), "Electronics")

class CustomerModelTest(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(first_name="John", last_name="Doe", email="john@example.com", password="password")

    def test_customer_creation(self):
        self.assertEqual(str(self.customer), "John Doe")

class ProductModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Electronics")
        self.product = Product.objects.create(name="Laptop", price=1000, category=self.category)

    def test_product_creation(self):
        self.assertEqual(self.product.name, "Laptop")
        self.assertEqual(str(self.product), "Laptop")

class OrderModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Electronics")
        self.product = Product.objects.create(name="Laptop", price=1000, category=self.category)
        self.customer = Customer.objects.create(first_name="John", last_name="Doe", email="john@example.com", password="password")
        self.order = Order.objects.create(product=self.product, customer=self.customer, quantity=1)

    def test_order_creation(self):
        self.assertEqual(str(self.order), self.product.name)

class ProfileModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="john", password="password")
        self.profile = Profile.objects.create(user=self.user, address1="123 Street", phone="1234567890")

    def test_profile_creation(self):
        self.assertEqual(str(self.profile), self.user.username)

class SignUpFormTest(TestCase):
    def test_valid_form(self):
        form_data = {
            'username': 'john',
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john@example.com',
            'password1': 'strongpassword',
            'password2': 'strongpassword',
        }
        form = SignUpForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form_data = {
            'username': '',
            'first_name': '',
            'last_name': '',
            'email': 'john@example.com',
            'password1': 'strongpassword',
            'password2': 'differentpassword',
        }
        form = SignUpForm(data=form_data)
        self.assertFalse(form.is_valid())

class ViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="john", password="password")
        self.category = Category.objects.create(name="Electronics")
        self.product = Product.objects.create(name="Laptop", price=1000, category=self.category)

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_about_view(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')

    def test_login_view(self):
        response = self.client.post(reverse('login'), {'username': 'john', 'password': 'password'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('index'))

    def test_logout_view(self):
        self.client.login(username='john', password='password')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('index'))

    def test_register_view(self):
        response = self.client.post(reverse('register'), {
            'username': 'jane',
            'first_name': 'Jane',
            'last_name': 'Doe',
            'email': 'jane@example.com',
            'password1': 'strongpassword',
            'password2': 'strongpassword',
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('update_info'))

    def test_product_view(self):
        response = self.client.get(reverse('product', args=[self.product.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product.html')

    def test_category_view(self):
        response = self.client.get(reverse('category', args=[self.category.name.replace(' ', '-')]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'category.html')

    def test_search_view(self):
        response = self.client.post(reverse('search'), {'searched': 'Laptop'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'search.html')
        self.assertContains(response, 'Laptop')

    def test_update_user_view(self):
        self.client.login(username='john', password='password')
        response = self.client.post(reverse('update_user'), {
            'username': 'john_updated',
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john_updated@example.com',
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('index'))

    def test_update_password_view(self):
        self.client.login(username='john', password='password')
        response = self.client.post(reverse('update_password'), {
            'new_password1': 'newstrongpassword',
            'new_password2': 'newstrongpassword',
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('update_user'))

    def test_update_info_view(self):
        self.client.login(username='john', password='password')
        response = self.client.post(reverse('update_info'), {
            'phone': '1234567890',
            'address1': '123 Street',
            'address2': 'Apt 4',
            'city': 'City',
            'state': 'State',
            'zipcode': '12345',
            'country': 'Country',
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('index'))
