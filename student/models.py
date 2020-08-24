from django.db import models

# Create your models here.
class Student(models.Model):
    student_reg_number = models.TextField(unique=True)
    student_name = models.TextField()
    student_email = models.TextField()
    student_mobile = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now=True)