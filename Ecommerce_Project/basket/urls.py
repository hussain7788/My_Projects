from django.urls import path, include
from basket import views

urlpatterns = [
    path("basket_summary/", views.basket_summary, name="basket_summary"),
    path("basket_add/", views.basket_add, name="basket_add"),
    path("basket_delete/", views.basket_delete, name="basket_delete"),
    path("basket_update/", views.basket_update, name="basket_update")
]
