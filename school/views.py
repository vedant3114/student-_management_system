from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Notification
from student.models import Student, Parent
from django.utils.text import slugify
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
    return render(request, "Home/index.html")

@login_required
def dashboard(request):
    try:
        unread_notification = Notification.objects.filter(user=request.user, is_read=False)
        unread_notification_count = unread_notification.count()
    except:
        unread_notification = []
        unread_notification_count = 0
    return render(request, "Home/index.html", {
        'unread_notification': unread_notification,
        'unread_notification_count': unread_notification_count
    })

@login_required
def admin_dashboard(request):
    try:
        unread_notification = Notification.objects.filter(user=request.user, is_read=False)
        unread_notification_count = unread_notification.count()
    except:
        unread_notification = []
        unread_notification_count = 0
    return render(request, "Home/index.html", {
        'unread_notification': unread_notification,
        'unread_notification_count': unread_notification_count
    })

@login_required
def teacher_dashboard(request):
    try:
        unread_notification = Notification.objects.filter(user=request.user, is_read=False)
        unread_notification_count = unread_notification.count()
    except:
        unread_notification = []
        unread_notification_count = 0
    return render(request, "Home/index.html", {
        'unread_notification': unread_notification,
        'unread_notification_count': unread_notification_count
    })

@login_required
def student_dashboard(request):
    try:
        unread_notification = Notification.objects.filter(user=request.user, is_read=False)
        unread_notification_count = unread_notification.count()
    except:
        unread_notification = []
        unread_notification_count = 0
    return render(request, "Home/index.html", {
        'unread_notification': unread_notification,
        'unread_notification_count': unread_notification_count
    })

@login_required
def student_list(request):
    students = Student.objects.all().order_by('-joining_date')
    return render(request, 'student/student_list.html', {'students': students})

@login_required
def add_student(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        student_id = request.POST.get('student_id')
        gender = request.POST.get('gender')
        date_of_birth = request.POST.get('date_of_birth')
        religion = request.POST.get('religion')
        joining_date = request.POST.get('joining_date')
        phone_number = request.POST.get('mobile_number')
        admission_number = request.POST.get('admission_number')
        section = request.POST.get('section')
        student_image = request.FILES.get('student_image')
        email = request.POST.get('email')
        address = request.POST.get('address')

        #retrieve parent details from the form
        father_name = request.POST.get('father_name')
        father_occupation = request.POST.get('father_occupation')
        father_mobile = request.POST.get('father_mobile')
        father_email = request.POST.get('father_email')
        mother_name = request.POST.get('mother_name')
        mother_occupation = request.POST.get('mother_occupation')
        mother_mobile = request.POST.get('mother_mobile')
        mother_email = request.POST.get('mother_email')
        present_address = request.POST.get('present_address')
        permanent_address = request.POST.get('permanent_address')

        try:
            #save parent information to the database
            parent = Parent.objects.create(
                father_name=father_name,
                father_occupation=father_occupation,
                father_mobile=father_mobile,
                father_email=father_email,
                mother_name=mother_name,
                mother_occupation=mother_occupation,
                mother_mobile=mother_mobile,
                mother_email=mother_email,
                present_address=present_address,
                permanent_address=permanent_address
            )
            
            #save student information to the database
            student = Student.objects.create(
                first_name=first_name,
                last_name=last_name,
                Student_ID=student_id,
                gender=gender,
                date_of_birth=date_of_birth,
                religion=religion,
                joining_date=joining_date,
                phone_number=phone_number,
                admission_number=admission_number,
                section=section,
                student_image=student_image,
                parent=parent,
                email=email,
                address=address
            )
            messages.success(request, 'Student added successfully!')        
            return redirect('student_list')
        except Exception as e:
            messages.error(request, f'Error adding student: {str(e)}')
            return render(request, 'student/add_student.html')
        
    return render(request, 'student/add_student.html')

@login_required
def view_student(request, slug):
    student = get_object_or_404(Student, slug=slug)
    return render(request, 'student/student-details.html', {'student': student})

@login_required
def edit_student(request, slug):
    student = get_object_or_404(Student, slug=slug)
    if request.method == 'POST':
        # Update student information
        student.first_name = request.POST.get('first_name')
        student.last_name = request.POST.get('last_name')
        student.Student_ID = request.POST.get('student_id')
        student.gender = request.POST.get('gender')
        student.date_of_birth = request.POST.get('date_of_birth')
        student.religion = request.POST.get('religion')
        student.joining_date = request.POST.get('joining_date')
        student.phone_number = request.POST.get('mobile_number')
        student.admission_number = request.POST.get('admission_number')
        student.section = request.POST.get('section')
        student.email = request.POST.get('email')
        student.address = request.POST.get('address')
        
        if 'student_image' in request.FILES:
            student.student_image = request.FILES['student_image']

        # Update parent information
        parent = student.parent
        parent.father_name = request.POST.get('father_name')
        parent.father_occupation = request.POST.get('father_occupation')
        parent.father_mobile = request.POST.get('father_mobile')
        parent.father_email = request.POST.get('father_email')
        parent.mother_name = request.POST.get('mother_name')
        parent.mother_occupation = request.POST.get('mother_occupation')
        parent.mother_mobile = request.POST.get('mother_mobile')
        parent.mother_email = request.POST.get('mother_email')
        parent.present_address = request.POST.get('present_address')
        parent.permanent_address = request.POST.get('permanent_address')

        try:
            parent.save()
            student.save()
            messages.success(request, 'Student information updated successfully!')
            return redirect('student_list')
        except Exception as e:
            messages.error(request, f'Error updating student: {str(e)}')
    
    return render(request, 'students/edit-student.html', {'student': student})

@login_required
def delete_student(request, slug):
    if request.method == 'POST':
        student = get_object_or_404(Student, slug=slug)
        try:
            # Delete the parent record first (due to OneToOneField)
            if student.parent:
                student.parent.delete()
            student.delete()
            messages.success(request, 'Student deleted successfully!')
        except Exception as e:
            messages.error(request, f'Error deleting student: {str(e)}')
    return redirect('student_list')

def mark_notification_as_read(request):
    if request.method == 'POST':
        try:
            notification = Notification.objects.filter(user=request.user, is_read=False)
            notification.update(is_read=True)
            return JsonResponse({'status': 'success'})
        except:
            return JsonResponse({'status': 'error', 'message': 'No notifications found'})
    return HttpResponseForbidden()

def clear_all_notification(request):
    if request.method == "POST":
        try:
            notification = Notification.objects.filter(user=request.user)
            notification.delete()
            return JsonResponse({'status': 'success'})
        except:
            return JsonResponse({'status': 'error', 'message': 'No notifications found'})
    return HttpResponseForbidden()

def clear_all_notifications(request):
    return HttpResponse('All notifications cleared (placeholder).')