from django.shortcuts import render

from django.db.models import Q

from products.models import *

def homepage(request):
    products = Product.objects.all()[0:8]
    return render(request, 'home/homepage.html', {'products': products})


def shop(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    active_category = request.GET.get('category', '')

    print("============================", active_category)

    if active_category:
        products = products.filter(category__slug=active_category)

    query = request.GET.get('query', '')
    if query:
        products = products.filter(Q(name__icontains=query)| Q(description__icontains=query))

    context = {
        'categories': categories,
        'products': products,
        'active_category': active_category,
    }

    return render(request, 'home/shop.html', context)
