
from django.contrib import admin
from django.urls import path, include
from app1 import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='base.html')),
    path('user_signup/', views.user_signup, name='user_signup'),
    path('user_login/', views.user_login, name='user_login'),
    path('validate_otp/', views.validate_otp, name='validate_otp'),
    path('auto_suggest/', views.auto_suggest, name='auto_suggest'),
    path('search/', views.search, name='search'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('dashboard/', views.dashboard, name='dashboard'),

    ###################### API ########################
    path('user/signup/', views.user_signup_api),
    path('user/login/', views.user_login_api),
    path('user/logout/', views.user_logout_api),
    path('login/', include('rest_framework.urls'))




]
