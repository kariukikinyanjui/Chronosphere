from django.urls import path
from . import views

# URL patterns for the shopping cart functionality
urlpatterns = [
    # URL pattern for viewing the cart summary
    path('', views.cart_summary, name="cart_summary"),

    # URL pattern for adding an item to the cart
    path('add/', views.cart_add, name="cart_add"),

    # URL pattern for deleting an item from the cart
    path('delete/', views.cart_delete, name="cart_delete"),

    # URL pattern for updating the quantity of an item in the cart
    path('update/', views.cart_update, name="cart_update"),
]
