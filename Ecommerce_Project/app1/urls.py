from django.urls import path, include
from app1 import views

# app_name = "app1"
urlpatterns = [
    path('', views.index, name="index"),
    path("register_user/", views.register_user, name="register_user"),
    path("login_user/", views.login_user, name="login_user"),
    path('logout_user/', views.logout_user, name="logout_user"),
    path('search/<slug:category_slug>/',
         views.category_list, name="category_list"),
    path("product/<slug:slug>/", views.product_details, name="product_details"),

]
