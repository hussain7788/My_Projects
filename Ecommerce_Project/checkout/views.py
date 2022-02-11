from django.http import JsonResponse
from django.shortcuts import render
from basket.basket import Basket
# Create your views here.
from .models import Address
from django.contrib import messages
from django.contrib.auth.models import User


def shipping_address(request):
    basket = Basket(request)
    if request.method == "POST":
        user = request.user
        fn = request.POST.get("first_name")
        ln = request.POST.get("last_name")
        em = request.POST.get("email")
        ph = request.POST.get("phone")
        ad1 = request.POST.get("address1")
        ad2 = request.POST.get("address2")
        zip = request.POST.get("zip")
        town = request.POST.get("town")
        user_obj = User.objects.filter(username=user).get()
        address = Address(customer=user_obj, first_name=fn, last_name=ln, phone=ph,
                          Email=em, address_line=ad1, address_line2=ad2, postcode=zip, town_city=town)
        address.save()
        messages.success(request, "address details added successfully")
        return render(request, "checkout/payment_selection.html")
    else:
        return render(request, "checkout/shipping_address.html", {"basket": basket})


def payment_selection(request):
    return render(request, "checkout/payment_selection.html")
