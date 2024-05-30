from django.shortcuts import render

def cart_summary(request):
    """
    Renders the 'cart_summary' template and returns the rendered HTML as a response.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML response.
    """
    return render(request, 'cart_summary.html', {})



def cart_update(request):
    """
    Renders the 'cart_update' template and returns the rendered HTML as a response.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML response.
    """
    pass


def cart_delete(request):
    """
    Renders the 'cart_delete' template and returns the rendered HTML as a response.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML response.
    """
    pass

def cart_add(request):
    """
    Renders the 'cart_add' template and returns the rendered HTML as a response.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML response.
    """
    pass