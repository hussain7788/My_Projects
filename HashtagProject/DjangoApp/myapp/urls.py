
from django.urls import path, include
from .views import get_top_hashtags

urlpatterns = [
    path('hashtags/', get_top_hashtags)
]
