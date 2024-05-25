from django import forms
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.shortcuts import render
from .forms import SignUpForm
from .models import Product, Category


def index(request):
    """This function renders the 'index.html' template when the 'home' view is accessed.

    :param request:

    """
    products = Product.objects.all()
    return render(request, "index.html", {"products": products})


def about(request):
    """This function renders the 'about.html' template when the 'about' view is accessed.

    :param request:
    """
    return render(request, "about.html")


def login_user(request):
    """A function that logs in the user

    :param request:

    """
    if request.method == "POST":
        """Login user"""
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in!")
            return redirect("index")
        else:
            messages.success(request, "Error logging in")
            return redirect("login")
    else:
        return render(request, "login.html", {})


def logout_user(request):
    """A function that logs out the user

    :param request:

    """
    logout(request)
    messages.success(request, "You have been logged out!")
    return redirect("index")


def register_user(request):
    """A function that registers the user

    :param request:

    """
    form = SignUpForm()
    if request.method == "POST":
        """Register user"""
        form = SignUpForm(request.POST)
        if form.is_valid():
            """Save user"""
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have successfully registered")
            return redirect("index")
        else:
            """Show errors if user not saved"""
            messages.success(request, "Error registering user")
            return redirect("register")
    else:
        """Render registration form"""
        return render(request, "register.html", {"form": form})
    return render(request, "about.html")

def product(request, pk):
    """This function renders the 'product.html' template when the 'product' view is accessed.

    :param request:
    :param pk: product id

    """
    product = Product.objects.get(id=pk)
    return render(request, "product.html", {"product": product})

def category(request, abc):
    """This function renders the 'category.html' template when the 'category' view is accessed.

    :param request:
    :param abc: category id

    """
    abc = abc.replace("-", " ")
    try:
        category = Category.objects.get(name=abc)
        products = Product.objects.filter(category=category)
        return render(request, "category.html", {"category": category, "products": products})
    except:
        messages.success(request, "Category does not exist")
        return redirect("index")
