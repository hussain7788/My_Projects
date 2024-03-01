
from django.urls import path, include
from .views import *

urlpatterns = [
    path('add/customer/', CustomerAdd.as_view(), name='signup'),
    path('login/', AdminLogin.as_view(), name='login'),
    path('logout/', AdminLogout.as_view(), name='logout'),
]
