from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.index, name='index'),
    path('notifications/mark-read/', views.mark_notifications_as_read, name='mark_notifications_as_read'),
    path('notifications/clear-all/', views.clear_all_notifications, name='clear_all_notifications'),
]