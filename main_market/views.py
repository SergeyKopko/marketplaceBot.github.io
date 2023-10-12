from django.http import HttpResponse
from django.shortcuts import render

from .models import Product


def main(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'main.html', context=context)
