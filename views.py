from django.shortcuts import render
from django.http import JsonResponse
from .models import Product  # Make sure your Product model is defined in models.py

# Create your views here.
def product_list(request):
    if request.method == 'GET':  # Check if the request is a GET request
        products = Product.objects.all()  # Fetch all products from the database
        products_list = list(products.values())  # Convert QuerySet to a list of dictionaries
        return JsonResponse(products_list, safe=False)  # Return as JSON response
