from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from product_app.models import Product,Category,Images
from Ecommerce_app.models import Footer,Header

from django.contrib.auth import logout,authenticate,login,update_session_auth_hash
from django.contrib.auth.models import User,auth
from django.contrib import messages
from user_app.models import User_Profile

from user_app.forms import SignUpForm,UserUpdateForm,ProfileUserUpdate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm


# Create your views here.


def Log_in_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.warning(request,'Your password or username do not match.')

    # Return an 'invalid login' error message.
    # category = Category.objects.all()
    # header_query = get_object_or_404(Header)

    data = {
        # "category": category,
        # "header_query": header_query,

    }
    return render(request,'login-user.html',data)


def Register(request):
    # if request.method == 'POST':
    #     form = SignUpForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         username = form.cleaned_data.get('username')
    #         password_raw = form.cleaned_data.get('password1')
    #         user = authenticate(username=username,password=password_raw)
    #         login(request,user)
    #         current_user = request.user
    #         data = UserProfile()
    #         data.user_id = current_user.id
    #         data.image = "user_img/avatar.jpg"
    #         data.save()
    #
    #         return redirect('home')
    #     else:
    #         messages.warning(request,"Your new and reset password is not matching")
    # else:
    #     form = SignUpForm()
    # category = Category.objects.all()
    # header_query = get_object_or_404(Header)
    #
    # data = {
    #     "category": category,
    #     "header_query": header_query,
    #     "form":form
    # }
    # return render(request,'Register_user.html',data)

    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken ')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'taken email')
                return redirect('register')
            else:
                x = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,
                                             password=password1)
                x.save()
                username = username
                password_raw = password1
                user = authenticate(username=username,password=password_raw)
                login(request,user)
                current_user = request.user
                data = User_Profile()
                data.user_id = current_user.id
                data.image = "user_img/avatar.jpg"
                data.save()
        else:
            messages.info(request,'password not matching ')
            return redirect('register')
        return redirect('home')

    # category = Category.objects.all()
    # header_query = get_object_or_404(Header)

    data = {
        # "category": category,
        # "header_query": header_query,
    }
    return render(request,'Register_user.html',data)


def logout_user(request):
    logout(request)
    return redirect('home')


def UserProfilePage(request):
    # category = Category.objects.all()
    # header_query = get_object_or_404(Header)
    current_user = request.user
    profile = User_Profile.objects.get(user_id=current_user.id)
    # get ke  filter korechi ami porbem

    data = {
        # "category": category,
        # "header_query": header_query,
        "profile": profile,

    }

    return render(request,'userprofile.html',data)


@login_required(login_url='/user_app/login/')
def user_profile_update(request):
    if request.method == 'POST':
        current_user = request.user
        post = User_Profile.objects.get(user_id=current_user.id)
        user_form = UserUpdateForm(request.POST,instance=request.user)
        profile_form = ProfileUserUpdate(request.POST or None,request.FILES or None,instance=post)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('userprofile')

    user_form = UserUpdateForm(instance=request.user)
    profile_form = ProfileUserUpdate(instance=request.user)

    data = {
        "user_form": user_form,
        "profile_form": profile_form

    }
    return render(request,'userprofile_update.html',data)


@login_required(login_url='/user_app/login/')
def change_password(request):
    if request.method == 'POST':
        current_user = request.user
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,user)  # Important!
            messages.success(request,'Your password was successfully updated!')
            return redirect('userprofile')
        else:
            messages.error(request,'Please correct the error below.')
            return redirect('change_password')
    else:
        form = PasswordChangeForm(request.user)
    
        data = {
            "form": form,

        }

    return render(request,'user_password_update.html',data)
