from django.shortcuts import render

def index(request):
    """
    This function renders the 'index.html' template when the 'home' view is accessed.
    """
    return render(request, 'index.html', {})