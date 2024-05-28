from django.shortcuts import render

def index(request):
    """
    Render the 'store/index.html' template for the given request.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML response.
    """
    return render(request, 'index.html', {})
