from django.shortcuts import render

from products.models import *

def homepage(request):
    products = Product.objects.all()[0:8]
    return render(request, 'home/homepage.html', {'products': products})


def shop(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    active_category = request.GET.get('category', '')

    print("============================", active_category)

    context = {
        'categories': categories,
        'products': products,
        'active_category': active_category,
    }

    return render(request, 'home/shop.html', context)
