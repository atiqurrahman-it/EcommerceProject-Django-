from django.shortcuts import render,HttpResponse,HttpResponseRedirect,get_object_or_404,redirect
from OrderApp.models import ShopingCartForm,ShopCart,Order,OderProduct,OderForm
from product_app.models import Product,Category,Images,Comment
from Ecommerce_app.models import Footer,Header,ContactForm
from user_app.models import User_Profile

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.crypto import get_random_string


# Create your views here.

def Add_to_Shoping_cart(request,id):
    url = request.META.get('HTTP_REFERER')
    current_user = request.user
    checking = ShopCart.objects.filter(product_id=id,user_id=current_user.id)
    if checking:
        control = 1
    else:
        control = 0

    if request.method == "POST":
        form = ShopingCartForm(request.POST)
        if form.is_valid():
            if control == 1:
                data = ShopCart.objects.get(product_id=id,user_id=current_user.id)
                data.quantity += form.cleaned_data['quantity']
                data.save()
            else:
                data = ShopCart()
                data.user_id = current_user.id
                data.product_id = id
                data.quantity = form.cleaned_data['quantity']
                data.save()
                messages.success(request,'your product successfully added')
        return HttpResponseRedirect(url)
    else:
        if control == 1:
            data = ShopCart.objects.get(product_id=id,user_id=current_user.id)
            data.quantity += 1
            data.save()

        else:
            data = ShopCart()
            data.user_id = current_user.id
            data.product_id = id
            data.quantity = 1
            data.save()
        return HttpResponseRedirect(url)


def Shoping_cart_details(request):
    # add to card
    current_user = request.user
    shop_card_details = ShopCart.objects.filter(user_id=current_user.id)
    # je login thakbe tar add product dakhabe
    total_amount = 0
    for p in shop_card_details:
        total_amount += p.product.New_price * p.quantity

    data = {
        "shop_card_details": shop_card_details,
        "total_amount": total_amount,
    }
    return render(request,'shop_card_details.html',data)


def cart__product_delete(request,id):
    url = request.META.get('HTTP_REFERER')
    current_user = request.user
    product_delete = ShopCart.objects.filter(id=id,user_id=current_user.id)
    product_delete.delete()
    messages.warning(request,'Your product has been deleted .')
    return HttpResponseRedirect(url)


@login_required(login_url='/user_app/login/')
def Order_card(request):
    current_user = request.user
    Shoping_Card = ShopCart.objects.filter(user_id=current_user.id)
    totalamount = 0
    # shoping card a add product er total amount
    for ta in Shoping_Card:
        totalamount += ta.quantity * ta.product.New_price

    if request.method == "POST":
        form = OderForm(request.POST,request.FILES)
        if form.is_valid():
            # form theke asa sob data order model a add or Submission or save
            data = Order()
            # get product quantity from form
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.address = form.cleaned_data['address']
            data.city = form.cleaned_data['city']
            data.phone = form.cleaned_data['phone']
            data.country = form.cleaned_data['country']
            data.transaction_id = form.cleaned_data['transaction_id']
            data.transaction_image = form.cleaned_data['transaction_image']
            data.user_id = current_user.id
            data.total = totalamount
            data.ip = request.META.get('REMOTE_ADDR')
            order_code = get_random_string(5).upper()  # random cod
            data.code = order_code
            data.save()

            # moving data shortcart to product cart
            # orderProduct model a add hobe
            for rs in Shoping_Card:
                dat = OderProduct()
                dat.order_id = data.id  # data.id  that means oder model primary id
                dat.user_id = current_user.id
                dat.product_id = rs.product_id  # rs.product_id import shopCard
                dat.quantity = rs.quantity  # rs.quantity mane shopCard model er quantity
                dat.price = rs.product.New_price  # price that means (self.product.New_price)
                dat.amount = rs.quantity * rs.product.New_price  # amount that means (self.quantity * self.product.New_price)
                dat.save()

                # koto gula product order kora hobe totogula product product model er amount theke - kora hobe
                product = Product.objects.get(id=rs.product_id)
                product.product_amount -= rs.quantity  # product model product_amount theke - kora hobe orderproduct er sonkha
                product.save()

                # Now remove all oder data from the shoping cart

            ShopCart.objects.filter(user_id=current_user.id).delete()


            data = {
                # 'category':category,
                'order_code': order_code,

            }

            return render(request,'oder_completed.html',data)
        else:
            messages.warning(request,form.errors)
    form = OderForm()
    # problem get korle kal dekhte hobe
    profile = User_Profile.objects.get(user_id=current_user.id)
    # total amount dui ta ache koi
    total_amount = 0
    for p in Shoping_Card:
        total_amount += p.quantity * p.product.New_price
    data = {
        "Shoping_Card": Shoping_Card,
        "totalamount": totalamount,
        "total_amount": total_amount,
        "profile": profile,
        "form": form,
    }
    return render(request,'oder_checkout.html',data)


def orderShow_user(request):
    current_user = request.user
    your_order = Order.objects.filter(user_id=current_user.id)
    data = {
        "your_order": your_order,

    }
    return render(request,'orderShow_user.html',data)  # user panel


# ordershow_user.html je Detail button ache or code
@login_required(login_url='/user_app/login/')
def orderShow_Details_user(request,id):
    current_user = request.user
    order = Order.objects.get(user_id=current_user.id,id=id)
    Products = OderProduct.objects.filter(user_id=id)

    data = {
        "order": order,
        "Products": Products
    }
    return render(request,'orderShow_details_user.html',data)  # user panel


def orderProduct_list_Show(request):
    current_user = request.user
    your_orderProduct_list = OderProduct.objects.filter(user_id=current_user.id)
    data = {
        "your_orderProduct_list": your_orderProduct_list,

    }
    return render(request,'orderProduct_list_show.html',data)  # user panel


@login_required(login_url='/user_app/login/')
def orderProduct_show_Details(request,id,oid):  # oid order id
    current_user = request.user
    order = Order.objects.get(user_id=current_user.id,id=oid)
    Products = OderProduct.objects.filter(user_id=current_user.id,id=id)

    data = {
        "order": order,
        "Products": Products
    }
    return render(request,'orderProduct_details.html',data)  # user panel


def usercommentshow(request):

    current_user = request.user
    commentShow = Comment.objects.filter(user_id=current_user.id)

    data = {
        "commentShow": commentShow,
    }
    return render(request,'userCommentShow.html',data)


def commentDelete(request,id):
    current_user=request.user
    comment = Comment.objects.filter(user_id=current_user.id,id=id)
    comment.delete()
    return redirect("userCommentShow")
