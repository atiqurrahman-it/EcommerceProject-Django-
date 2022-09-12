from django.contrib import admin
from .models import ShopCart,Order,OderProduct


# Register your models here.

class Shop_carddAdmin(admin.ModelAdmin):
    list_display = ['product','user','quantity','price','amount']
    list_filter = ['user']


admin.site.register(ShopCart,Shop_carddAdmin)


# ----------------------------------------------

class OrderProductline(admin.TabularInline):
    model = OderProduct  # import
    readonly_fields = ('user','product','price','quantity','amount')
    can_delete = False
    extra = 0


class oderAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name',
                    'phone','total','status','transaction_id']
    list_filter = ['status']
    readonly_fields = ('user','first_name','last_name',
                       'phone','address','city','country','total','ip','transaction_id','image_tag')
    can_delete = False
    inlines = [OrderProductline]  # import


admin.site.register(Order,oderAdmin)


class orderProductAdmin(admin.ModelAdmin):
    list_display = ['user','product','price','quantity','amount']
    list_filter = ['user']


admin.site.register(OderProduct,orderProductAdmin)
