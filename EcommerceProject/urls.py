

from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
     path('', include('Ecommerce_app.urls')),
    path('product/', include('product_app.urls')),
    path('OrderApp/', include('OrderApp.urls')),
    path('user_app/', include('user_app.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

