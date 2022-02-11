import re
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from .forms import UserRegForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def categories(request):
    return {
        "categories": Category.objects.all()
    }


def index(request):
    context = {"products": Product.objects.all()}
    return render(request, "index.html", context)


def register_user(request):
    fm = UserRegForm()
    if request.method == "POST":
        fm = UserRegForm(request.POST)
        if fm.is_valid():
            username = fm.cleaned_data['username']
            email = fm.cleaned_data['email']
            password1 = fm.cleaned_data['password1']
            password2 = fm.cleaned_data['password2']
            if User.objects.filter(username=username).exists():
                messages.error(request, "username is taken")
                return redirect("register_user")
            if User.objects.filter(email=email).exists():
                messages.error(request, "email is taken")
                return redirect("register_user")
            else:
                fm.save()
                form = UserRegForm()
                messages.success(request, "user registered successfully")
                return render(request, "register_user.html", {"u_reg_msg": "user registered successfully", "form": form})
        else:
            messages.error(request, "user is exist")
            return redirect("register_user")
    else:
        fm = UserRegForm()
        return render(request, "register_user.html", {"form": fm})


# by using ajax we are adding user
# def register_user(request):
#     if request.method == "POST":
#         fm = UserRegForm(request.POST)
#         if fm.is_valid():
#             uname = request.POST['username']
#             email = request.POST['email']
#             password1 = request.POST['password1']
#             password2 = request.POST['password2']
#             print(uname, email, password1, password2)
#             fm.save()
#             return JsonResponse({"status": "save"})
#         else:
#             return JsonResponse({"status": 0})
#     else:
#         fm = UserRegForm()
#         return render(request, "register_user.html", {"form": fm})


def login_user(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        upass = request.POST.get('password')
        user = authenticate(username=uname, password=upass)
        if user is not None:
            login(request, user)
            user_obj = User.objects.get(username=uname)
            request.session['user_id'] = user_obj.id
            context = {"username": uname}
            messages.success(request, "valid user")
            return render(request, "user_profile.html", context)
        else:
            messages.error(request, "invalid user")
            return redirect("login_user")
    else:
        return render(request, "login_user.html")


def logout_user(request):
    logout(request)
    return redirect('login_user')


def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, "category_list.html", {"category": category, "products": products})


def product_details(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, "product_details.html", {"product": product})
