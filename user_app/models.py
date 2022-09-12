from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe


# Create your models here.

class User_Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    phone = models.CharField(blank=True,max_length=20)
    address = models.CharField(blank=True,max_length=200)
    city = models.CharField(blank=True,max_length=200)
    country = models.CharField(blank=True,max_length=200)
    image = models.ImageField(blank=True,null=True, upload_to='user_img/')

    def image_tag(self):
        return mark_safe('<img src="%s" width="100px" height="100px" />' % self.image.url)

    image_tag.short_description = 'Image'

    def image_url(self):
        return self.image.url

    def user_name(self):
        return self.user.first_name + '' + self.user.last_name + ' [' + self.user.username + ']'

    def __str__(self):
        return self.user.username
