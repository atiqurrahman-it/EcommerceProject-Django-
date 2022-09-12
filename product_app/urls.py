from django.urls import path

from . import views

urlpatterns = [
    path("comment_Add/<int:id>/",views.comment_Add,name="comment_Add")

]
