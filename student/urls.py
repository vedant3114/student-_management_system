from . import views
from django.urls import path,include
from django.contrib import admin
# student app urls
urlpatterns = [
    path('add_student/', views.add_student, name='add_student'),
    path('student_list/', views.student_list, name='student_list'),
]
