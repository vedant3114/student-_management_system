from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import  Parent,Student

@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = ('father_name', 'mother_name', 'father_mobile', 'mother_mobile')
    search_fields = ('father_name', 'mother_name', 'father_mobile', 'mother_mobile')
    list_filter = ('father_occupation', 'mother_occupation')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'Student_ID', 'email', 'date_of_birth', 'phone_number', 'joining_date', 'admission_number')
    search_fields = ('first_name', 'last_name', 'Student_ID', 'email')
    list_filter = ('gender', 'section', 'joining_date')
    prepopulated_fields = {'slug': ('first_name', 'last_name', 'Student_ID')}
    readonly_fields = ('student_image',)

