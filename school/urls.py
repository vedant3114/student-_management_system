from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='authentication/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('teacher-dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('student-dashboard/', views.student_dashboard, name='student_dashboard'),
    
    path('notifications/mark-read/', views.mark_notification_as_read, name='mark_notification_as_read'),
    path('notifications/clear-all/', views.clear_all_notifications, name='clear_all_notifications'),
    
    # Student URLs
    path('students/', views.student_list, name='student_list'),
    path('students/add/', views.add_student, name='add_student'),
    path('students/view/<slug:slug>/', views.view_student, name='view_student'),
    path('students/edit/<slug:slug>/', views.edit_student, name='edit_student'),
    path('students/delete/<slug:slug>/', views.delete_student, name='delete_student'),

    # Department URLs
    path('departments/add/', views.add_department, name='add_department'),
    path('departments/list/', views.department_list, name='department_list'),
    path('departments/edit/<slug:slug>/', views.edit_department, name='edit_department'),
    path('departments/delete/<slug:slug>/', views.delete_department, name='delete_department'),

    # Teacher URLs
    path('teachers/add/', views.add_teacher, name='add_teacher'),
    path('teachers/list/', views.teacher_list, name='teacher_list'),
    path('teachers/edit/<slug:slug>/', views.edit_teacher, name='edit_teacher'),
    path('teachers/delete/<slug:slug>/', views.delete_teacher, name='delete_teacher'),
]