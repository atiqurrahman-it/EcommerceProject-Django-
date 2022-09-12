from django.contrib import admin
from .models import User_Profile


# Register your models here.

class userprofileAdmin(admin.ModelAdmin):
    list_display = ['user','country','image_tag']


admin.site.register(User_Profile,userprofileAdmin)
