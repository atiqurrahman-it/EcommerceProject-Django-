from django.urls import path
from . import views
urlpatterns = [
    path('Add_to_Shop_card/<int:id>/', views.Add_to_Shoping_cart, name="Add_to_Shop_card"),
    path('Shop_card_details/', views.Shoping_cart_details, name="Shop_card_details"),
    path('Shop_card_delete/<int:id>/', views.cart__product_delete, name="Shop_card_delete"),
    path('Order_card/', views.Order_card, name="Order_card"),
    path('order_list_Show/',views.orderShow_user,name="orderShow_panel"),
    path('order_Details_Show/<int:id>/',views.orderShow_Details_user,name="order_Details_Show"),
    path('orderProduct_list_Show/',views.orderProduct_list_Show,name="orderProduct_list_Show"),
    path('orderProduct_Details/<int:id>/<int:oid>/',views.orderProduct_show_Details,name="orderProduct_Details"),
    path('userCommentShow/',views.usercommentshow,name="userCommentShow"),
    path('commentDelete/<int:id>/',views.commentDelete,name="commentDelete"),

]
