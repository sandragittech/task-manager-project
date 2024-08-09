from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('url/task/', views.task_view, name='task'),
]