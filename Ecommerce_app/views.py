from django.shortcuts import render,get_object_or_404,redirect,HttpResponse

from .models import Footer,Header,ContactForm,FAQ
from product_app.models import Product,Category,Images

from OrderApp.models import ShopCart
from product_app.models import Comment


# Create your views here.

def homepage(request):
    current_user = request.user
    slider = Product.objects.all().order_by('id')[:10]
    latest_product = Product.objects.all().order_by('-id')[:10]
    all_product = Product.objects.all().order_by()
    # add to card
    shop_card_details = ShopCart.objects.filter(user_id=current_user.id)
    # je login thakbe tar add product dakhabe
    total_amount = 0
    total_product_add = 0
    for p in shop_card_details:
        total_amount += p.product.New_price * p.quantity
        total_product_add += 1

    data = {
        "latest_product": latest_product,
        "all_product": all_product,
        "slider": slider,
        # add to card
        "shop_card_details": shop_card_details,
        "total_amount": total_amount,
        "total_product_add": total_product_add

    }
    return render(request,'index.html',data)


def product_Single(request,product_id):
    single_product = get_object_or_404(Product,id=product_id)
    extra_image = Images.objects.filter(product_id=product_id)
    related_product = Product.objects.all().order_by('id')[:7]

    comment_show = Comment.objects.filter(product_id=product_id,
                                          status=True)  # second product_id hoilo request er id first product id comment theke import

    data = {
        "single_product": single_product,
        "extra_image": extra_image,
        "related_product": related_product,
        "comment_show": comment_show,  # comment show kora jonno  import kora hoiche
    }
    return render(request,'single_page.html',data)


def category_product(request,id,slug):
    category_pro = Product.objects.filter(category_id=id)

    category = Category.objects.all()
    footer_query = get_object_or_404(Footer)
    header_query = get_object_or_404(Header)

    data = {
        "category_product": category_pro,
        "category": category,
        "footer_query": footer_query,
        "header_query": header_query,
    }
    return render(request,'category_product.html',data)


def search(request):
    try:
        q = request.POST.get('q')
    except:
        q = None
    if q:
        search_pro = Product.objects.filter(title__icontains=q)

        data = {
            "category_product": search_pro,

        }
        return render(request,'category_product.html',data)

    else:
        data = {
        }
        return render(request,'Eorr_440.html',data)


def About_Me(request):
    data = {
    }
    return render(request,'about.html',data)


def Contact_page(request):
    footer_query = get_object_or_404(Footer)
    if request.method == 'POST':
        name = request.POST.get('customerName')
        email = request.POST.get('customerEmail')
        subjects = request.POST.get('contactSubject')
        details = request.POST.get('contactMessage')
        our_data = ContactForm(name=name,email=email,subject=subjects,message=details)
        our_data.save()
        return redirect('contact')
    data = {
        "footer_query": footer_query,
    }
    return render(request,'contact_page.html',data)


def faq_details(request):
    faqData = FAQ.objects.filter(status=True).order_by('create_at')
    data = {

        "faqData": faqData,
    }
    return render(request,'faqPage.html',data)
