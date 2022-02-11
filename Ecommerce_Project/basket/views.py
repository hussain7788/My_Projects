from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from app1.models import Product
from .basket import Basket
# Create your views here.


def basket_summary(request):
    basket = Basket(request)
    return render(request, "basket/basket_summary.html", {"basket": basket})



def basket_add(request):
    basket = Basket(request)
    if request.method == "POST":
        id = int(request.POST.get("product_id"))
        qty = int(request.POST.get("product_qty"))
        product = get_object_or_404(Product, id=id)
        basket.add(product=product, qty=qty)
        pr_qty = basket.__len__()
        return JsonResponse({"product_id": id, "qty": pr_qty})
    else:
        return JsonResponse({"method": "Get"})


def basket_delete(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        basket.delete(product=product_id)

        basketqty = basket.__len__()
        baskettotal = basket.get_total_price()
        response = JsonResponse({'qty': basketqty, 'subtotal': baskettotal})
        return response


def basket_update(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        basket.update(product=product_id, qty=product_qty)

        basketqty = basket.__len__()
        baskettotal = basket.get_total_price()
        response = JsonResponse({'qty': basketqty, 'subtotal': baskettotal})
        return response
