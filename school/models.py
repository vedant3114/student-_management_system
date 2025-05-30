from django.db import models
from django.utils.text import slugify
from django.utils import timezone

# Create your models here.
class Parent(models.Model):
    father_name = models.CharField(max_length=100)
    father_occupation = models.CharField(max_length=100)
    father_mobile = models.CharField(max_length=15, unique=True)
    father_email = models.EmailField(max_length=100, unique=True)
    mother_name = models.CharField(max_length=100)
    mother_occupation = models.CharField(max_length=100)
    mother_mobile = models.CharField(max_length=15, unique=True)
    mother_email = models.EmailField(max_length=100, unique=True)
    pressent_address = models.TextField()
    permanent_address = models.TextField()

    def __str__(self):
        return f"{self.father_name} & {self.mother_name}"
    

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(
        max_length=10,
        choices=[
            ('Male', 'Male'),
            ('Female', 'Female'),
            ('Other', 'Other'),
        ],
        default='Male'
    )

       
    Student_ID = models.CharField(max_length=20,default='Temp123', unique=True)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    religion = models.CharField(max_length=20, null=True, blank=True)
    joining_date = models.DateField(default=timezone.now)
    admission_number = models.CharField(max_length=15, unique=True, null=True, blank=True, default="temp123")
    section = models.CharField(max_length=15, null=True, blank=True)
    student_image = models.ImageField(upload_to='student/', blank=True)

    parent=models.OneToOneField(Parent, on_delete=models.CASCADE, null=True, blank=True)
    slug=models.SlugField(max_length=255, unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = f"{self.first_name}-{self.last_name}-{self.Student_ID}"
        super(Student, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.Student_ID})"

class Course(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20, unique=True)
    description = models.TextField()
    credits = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.code} - {self.name}"

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateField(auto_now_add=True)
    grade = models.CharField(max_length=2, null=True, blank=True)

    class Meta:
        unique_together = ('student', 'course')

    def __str__(self):
        return f"{self.student} - {self.course}"
