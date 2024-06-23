from django.contrib import admin
from django.urls import path

from home.views import *
from products.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='homepage'),
    path('shop/', shop, name='shop'),
    path('product/', product, name='product'),
]
