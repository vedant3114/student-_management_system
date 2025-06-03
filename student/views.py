from django.shortcuts import render

# Create your views here.
def add_student(request):
    return render(request, 'student/add_student.html')


def student_list(request):
    return render(request, 'student/student_list.html')


def edit_student(request):
    return render(request, 'student/edit_student.html')



def view_student(request):
    return render(request, 'student/student-detials.html')