from django.db import models

class Student(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    age=models.PositiveSmallIntegerField()
    email=models.EmailField()
    country=models.CharField(max_length=100)
    student_year = models.IntegerField(default=2024)  
    date_of_birth=models.PositiveSmallIntegerField()
    hobby = models.CharField(max_length=100, null=False, default='default_hobby')
    student_bio = models.TextField(null=False, default='default_student_bio')
    enrollment_year = models.CharField(max_length=100, null=False, default='default_enrollment_year')


    def __str__(self):
        return f"{self.first_name} {self.last_name}"




# Create your models here.
