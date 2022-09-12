

from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
     path('', include('Ecommerce_app.urls')),
    path('product/', include('product_app.urls')),
    path('OrderApp/', include('OrderApp.urls')),
    path('user_app/', include('user_app.urls')),
]
