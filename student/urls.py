from . import views
from django.urls import path,include
from django.contrib import admin
# student app urls
urlpatterns = [
    path('add/', views.add_student, name='add_student'),
    path('list/', views.student_list, name='student_list'),
    path('view/<slug:slug>/', views.view_student, name='view_student'),
    path('edit/<slug:slug>/', views.edit_student, name='edit_student'),
    path('delete/<slug:slug>/', views.delete_student, name='delete_student'),
]
