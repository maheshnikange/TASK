

from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('task', views.index,name='index'),
    path('task/<int:id>', views.index,name='task')


]
