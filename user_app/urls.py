from django.urls import path
from . import views
urlpatterns = [
    path('login/',views.Log_in_user,name="login_user"),
    path('register/',views.Register,name="register"),
    path('logout_user/',views.logout_user,name="logout_user"),
    path('userprofile/',views.UserProfilePage,name="userprofile"),
    path('userprofile_update/',views.user_profile_update,name="userprofile_update"),
    path('change_password/',views.change_password,name="change_password"),
]
