from django.urls import path, include
from checkout import views

# app_name = "app1"
urlpatterns = [
    path("shipping_address/", views.shipping_address, name="shipping_address"),
    path("payment_selection/", views.payment_selection, name="payment_selection")

]
