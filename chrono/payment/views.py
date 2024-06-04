from django.shortcuts import render

def payment_success(request):
	"""
    Renders the payment success template after a successful payment.

    This function is likely called after a successful payment flow in your application. 
    It typically displays a confirmation page to the user indicating their payment 
    was successful.

    Args:
        request: The Django HTTP request object containing information about the user's request.

    Returns:
        A Django HttpResponse object rendering the "payment/payment_success.html" template
    """
	return render(request, "payment/payment_success.html", {})