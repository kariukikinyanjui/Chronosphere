from django import forms
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from .forms import SignUpForm
from .models import Product


def index(request):
    """
    This function renders the 'index.html' template when the 'home' view is accessed.
    """
    products = Product.objects.all()
    return render(request, "index.html", {"products": products})


def about(request):
    """
    This function renders the 'about.html' template when the 'about' view is accessed.
    """
    return render(request, "about.html")


def login_user(request):
    """A function that logs in the user"""
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
    """A function that logs out the user"""
    logout(request)
    messages.success(request, "You have been logged out!")
    return redirect("index")


def register_user(request):
    """A function that registers the user"""
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
