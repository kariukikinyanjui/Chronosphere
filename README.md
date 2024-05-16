# Chronosphere
Chronosphere is an e-commerce platform specializing in the sale of high-quality watches. Our mission is to bring the world of luxury watches to your doorstep, providing a seamless and enjoyable shopping experience.

## Features
* **Product Catalog**: Browse and search for products with detailed descriptions, images, and pricing information.
* **Shopping Cart**: Add products to the cart, update quantities, and proceed to checkout.
* **Checkout Process**: Enter shipping and billing information, and complete the order with a secure payment gateway integration.
* **Order Management**: View order history, status updates, and order details for customers and administrators.
* **User Authentication**: Register new accounts, log in, and manage personal information.
* **Admin Dashboard**: Comprehensive administration interface for managing products, categories, orders, users, and site configuration.
* **Search and Filtering**: Search for products by name, category, or other attributes, and apply filters for easy browsing.
* **Reviews and Ratings**: Customers can leave reviews and ratings for products they've purchased.
* **Email and Notifications**: Receive email notifications for order confirmations, shipping updates, and other important events.
* **Responsive Design**: The website is fully responsive and optimized for various devices and screen sizes.

## Technologies Used
* Python 3.x
* Django 3.x
* Django REST Framework
* PostgreSQL
* HTML, CSS, JavaScript
* Bootstrap
* Payment gateway integration (e.g., Stripe, Paypal)
* Email service integration (e.g., Mailgun, SendGrid)

## Installation
1. Clone the repo:
`git clone git@github.com:kariukikinyanjui/Chronosphere.git`

2. Install the required dependencies:
`pip install -r requirements.txt`

3. Set up the database:
* Create a new PostgreSQL database
* Update the database settings in `settings.py` with your database credentials.
* Run the migrations:
`python3 manage.py migrate`

4. Create a superuser account for the admin dashboard:
`python3 manage.py createsuperuser`

5. Configure payment gateway and email service:
* Sign up for a payment gateway service and update the settings in `settings.py`
* Sign up for an email service provider and update the settings

6. Start the development server:
`python3 manage.py runserver`

7. Access the website at `http://localhost:8000/` and the admin dashboard at `http://localhost:8000/admin`

## Contributing

### Contributioins are welcome! Please follow these steps:
1. Fork the repo
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with descriptive messages.
4. Push your changes to your forked repo.
5. Submit a pull request with a detailed description of your changes.
