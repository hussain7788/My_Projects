from django.contrib import admin
from django.urls import path, include
from todo_app1 import views

urlpatterns = [
    path('todo/', views.TodoApiVIew.as_view()),
    path('todo/<int:pk>', views.TodoApiVIew.as_view())
]