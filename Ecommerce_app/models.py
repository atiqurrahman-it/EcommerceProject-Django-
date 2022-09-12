from django.db import models


# Create your models here.

class Header(models.Model):
    title = models.CharField(max_length=200,blank=True)
    h_icon = models.ImageField(upload_to='header_icon/')
    phone = models.IntegerField()

    def __str__(self):
        return self.title


class Footer(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='footer_pic/')
    description = models.CharField(max_length=500)
    F_icon = models.ImageField(upload_to='footer_icon/')
    address = models.CharField(max_length=200)
    phone = models.IntegerField()
    email = models.EmailField()
    facebook = models.CharField(max_length=100,blank=True)
    twitter = models.CharField(max_length=100,blank=True)
    instagram = models.CharField(max_length=100,blank=True)
    google_plus = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.email


class ContactForm(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=450)
    message = models.TextField()

    def __str__(self):
        return self.name


class FAQ(models.Model):
    STATUS = (
        ("True","True"),
        ("False","False")
    )
    orderNumber = models.IntegerField()
    question = models.CharField(max_length=100)
    answer = models.TextField()
    status = models.CharField(choices=STATUS,max_length=200,default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question
