from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="home"),
    path('single/<int:product_id>/', views.product_Single, name="single_product"),
    path('product/<int:id>/<slug:slug>/', views.category_product, name="category_product"),
    path('search/', views.search, name="search"),
    path('about/', views.About_Me, name="about"),
    path('contact/', views.Contact_page, name="contact"),
    path('faq/', views.faq_details, name="faq_details"),
]
