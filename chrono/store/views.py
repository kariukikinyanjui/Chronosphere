from django.shortcuts import render, redirect
from .models import Product, Category, Profile
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm, UpdateUserForm, ChangePasswordForm, UserInfoForm
from django.db.models import Q
from cart.cart import Cart
import json



def index(request):
    """
    Renders the 'index.html' template and returns the rendered HTML as a response.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML response.
    """
    products = Product.objects.all()
    return render(request, 'index.html',{'products': products})

def about(request):
    """
    Renders the 'about.html' template and returns the rendered HTML as a response.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML response.
    """
    return render(request, 'about.html', {})

def login_user(request):
    """
    Renders the 'login.html' template and returns the rendered HTML as a response.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML response.
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            #shopping cart
            current_user = Profile.objects.get(user__id=request.user.id)

            #Get cart from database
            saved_cart = current_user.old_cart

            #convert string to python dictionary
            if saved_cart:
                    converted_cart = json.loads(saved_cart)
                    cart = Cart(request)
                    for key,value in converted_cart.items():
                         cart.db_add(product=key, quantity=value)

            messages.success(request, 'You have been logged in!')
            return redirect('index')
            
        else:
            messages.success(request, 'Error logging in. Please try again.')
            return redirect('login')
    else:
        return render(request, 'login.html', {})

def logout_user(request):
    """ 
    Logs out the user and redirects to the index page.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML response.
    """
    logout(request)
    messages.success(request, 'You have been logged out!')
    return redirect('index')

def register_user(request):
    """
    Renders the 'register.html' template and returns the rendered HTML as a response.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML response.
    """
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Successful, please fill out user info!')
            return redirect('update_info')
        else:
            messages.error(request, 'Unable to register your account at this time. Please try again later.')
            return redirect('register')
    else:
        return render(request, 'register.html', {'form': form})
    

def product(request, pk):
    """
    Retrieves a specific product from the database based on the given primary key and renders the 'product.html' template with the product as a context variable.

    Parameters:
        request (HttpRequest): The HTTP request object.
        pk (int): The primary key of the product to retrieve.

    Returns:
        HttpResponse: The rendered HTML response containing the 'product.html' template with the product as a context variable.
    """
    product = Product.objects.get(id=pk)
    return render(request, 'product.html',{'product': product})

def category(request, abc):
    """
    Retrieves products from the database based on the given category and renders the 'category.html' template with the products as a context variable.

    Parameters:
        request (HttpRequest): The HTTP request object.
        abc (str): The category to filter products by.

    Returns:
        HttpResponse: The rendered HTML response containing the 'category.html' template with the products as a context variable.
    """
    abc = abc.replace('-', ' ')
    try:
        category = Category.objects.get(name=abc)
        products = Product.objects.filter(category=category)
        return render(request, 'category.html', {'products': products, 'category': category, 'products': products})
    except:
        messages.success(request, 'Category does not exist')
        return redirect('index')
    
def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        user_form   = UpdateUserForm(request.POST or None, instance=current_user)

        if user_form.is_valid():
            user_form.save()

            login(request, current_user)
            messages.success(request, 'Your account has been updated!')
            return redirect('index')
        
        return render(request, 'update_user.html', {'user_form': user_form})
    else:
        messages.success(request, 'Please login first')
        return redirect('index')
    
    
def update_password(request):
    """
    Handles password update functionality for authenticated users.

    If the user is authenticated, this view will:
    - Render a password change form on a GET request.
    - Process the submitted form data on a POST request.
    - Save the new password if the form is valid.
    - Log the user in with the new password.
    - Display appropriate success or error messages.

    If the user is not authenticated, it will:
    - Display a message indicating that login is required.
    - Redirect the user to the home page.

    Parameters:
    request (HttpRequest): The HTTP request object containing user and request data.

    Returns:
    HttpResponse: Redirects to different views based on the flow:
    - Redirects to 'update_user' upon successful password update.
    - Redirects to 'update_password' with error messages if the form is invalid.
    - Redirects to 'home' if the user is not authenticated.
    - Renders 'update_password.html' with the password change form on a GET request.
    """
    
    if request.user.is_authenticated:
        current_user = request.user
        
        if request.method == 'POST':
            form = ChangePasswordForm(current_user, request.POST)
            
            if form.is_valid():
                form.save()
                
                messages.success(request, "Password Has Been Updated")
                
                login(request, current_user)
                
                return redirect('update_user')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)
                
                return redirect('update_password')
        else:
            form = ChangePasswordForm(current_user)
            
            return render(request, "update_password.html", {'form': form})
    else:
        messages.success(request, "To View That Page You Must Be Logged In")
        
        return redirect('home')


def update_info(request):
	if request.user.is_authenticated:
		current_user = Profile.objects.get(user__id=request.user.id)
		
		form = UserInfoForm(request.POST or None, instance=current_user)
        
		if form.is_valid():
			form.save()
			messages.success(request, "Info Updated!!")
			return redirect('index')
		return render(request, "update_info.html", {'form':form})
	else:
		messages.success(request, "You Must Be Logged In To Access Page!!")
		return redirect('index')


def search(request):
    """
    This view function handles the search functionality.
    
    Args:
        request: HttpRequest object
    
    Returns:
        Renders the search.html page with search results if any, or a message if no matching products are found.
    """
    if request.method == "POST":
        searched = request.POST.get('searched', '')
        searched = Product.objects.filter(Q(name__icontains=searched) | Q(description__icontains=searched))
        if not searched:
            messages.success(request, "Product Does Not Exist...Please try Again.")
            return render(request, "search.html", {})
        else:
            return render(request, "search.html", {'searched': searched})
    else:
        return render(request, "search.html", {})	
