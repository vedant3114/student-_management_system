from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .models import Student

# Create your views here.
def index(request):
    return render(request, 'Home/index.html')

@login_required
def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/students.html', {'student_list': students})

@login_required
def add_student(request):
    if request.method == 'POST':
        # Handle form submission
        pass
    return render(request, 'students/add-student.html')

@require_POST
@login_required
def mark_notifications_as_read(request):
    # Here you would implement the logic to mark notifications as read
    # For now, we'll just return a success response
    return JsonResponse({'status': 'success'})

@require_POST
@login_required
def clear_all_notifications(request):
    # Here you would implement the logic to clear all notifications
    # For now, we'll just return a success response
    return JsonResponse({'status': 'success'})