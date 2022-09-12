from django.contrib import admin
from .models import Footer,Header,ContactForm,FAQ

# Register your models here.

admin.site.register(Footer)

admin.site.register(Header)


class faqAdmin(admin.ModelAdmin):
    list_display = ['orderNumber','question','status','status','update_at']
    list_filter = ['answer','status']


admin.site.register(FAQ,faqAdmin)

admin.site.register(ContactForm)
