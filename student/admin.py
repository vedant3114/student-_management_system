from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Parent, Student

@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = ('father_name', 'mother_name', 'father_mobile', 'mother_mobile')
    search_fields = ('father_name', 'mother_name', 'father_mobile', 'mother_mobile')
    list_filter = ('father_name', 'mother_name')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'Student_ID', 'gender', 'date_of_birth', 'joining_date', 'phone_number', 'admission_number', 'section')
    search_fields = ('first_name', 'last_name', 'Student_ID', 'admission_number')
    list_filter = ('gender', 'section')
    readonly_fields = ('student_image',)  # Optional: makes the image field read-only
