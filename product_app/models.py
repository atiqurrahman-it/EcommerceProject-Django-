from django.db import models

from django.utils.safestring import mark_safe
from django.db import models
from mptt.models import MPTTModel,TreeForeignKey

from django.contrib.auth.models import User
from django.forms import ModelForm
from django.db.models import Avg,Count,Max


# Create your models here.
class Category(MPTTModel):
    status = (
        ('True',True),
        ('False',False),
    )
    parent = TreeForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,related_name='children')
    title = models.CharField(max_length=200)
    keywords = models.CharField(max_length=150)
    image = models.ImageField(blank=True,upload_to='category_image/')
    status = models.CharField(max_length=50,choices=status)
    slug = models.SlugField(null=True,unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self):
        return self.title


class Product(models.Model):
    status = (
        ('True',True),
        ('False',False),
    )

    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    keywords = models.CharField(max_length=150)
    details = models.TextField()
    image = models.ImageField(upload_to='product_pic/')
    status = models.CharField(max_length=50,choices=status)
    New_price = models.DecimalField(max_digits=15,decimal_places=2)
    Old_price = models.DecimalField(max_digits=15,decimal_places=2)
    product_amount = models.IntegerField(default=0)
    min_product_amount = models.IntegerField(default=4)
    slug = models.SlugField(null=True,unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def image_tag(self):
        return mark_safe('<img src="%s" width="100px" height="100px" />' % self.image.url)

    image_tag.short_description = 'Image'

    def image_url(self):
        return self.image.url

    def get_absolute_url(self):
        return reverse('product_element',kwargs={'slug': self.slug})

    # Comment er jonno
    def review_average(self):
        reviews = Comment.objects.filter(
            product=self,status=True).aggregate(average=Avg('rating_review'))
        avg = 0
        if reviews['average'] is not None:
            avg = float(reviews['average'])
            return avg
        else:
            return avg

    # def total_review(self):
    #     reviews = Comment.objects.filter(
    #         product=self,status=True).aggregate(count=Count('id'))
    #
    #     cou = 0
    #     if reviews['count'] is not None:
    #         avg = float(reviews['count'])
    #         return cou
    #     else:
    #         return cou

    def __str__(self):
        return self.title


class Images(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    title = models.CharField(max_length=200,blank=True)
    image = models.ImageField(blank=True,upload_to='product_pic/')

    def __str__(self):
        return self.title


class Comment(models.Model):
    STATUS = (
        ('New','New'),
        ('True','True'),
        ('False','False'),

    )
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    subject = models.CharField(max_length=200,blank=True)
    comment = models.CharField(max_length=500,blank=True)
    rating_review = models.IntegerField(default=1)
    ip = models.CharField(max_length=100,blank=True)
    status = models.CharField(max_length=40,choices=STATUS,default='New')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['subject','comment','rating_review']
