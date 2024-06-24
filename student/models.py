from django.db import models

class Student(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    age=models.PositiveSmallIntegerField()
    email=models.EmailField()
    country=models.CharField(max_length=100)
    student_year=models.PositiveSmallIntegerField()
    date_of_birth=models.PositiveSmallIntegerField()
    hobby=models.CharField(max_length=20)
    student_bio=models.PositiveSmallIntegerField()
    enrollment_year=models.PositiveSmallIntegerField()


    def __str__(self):
        return f"{self.first_name} {self.last_name}"




# Create your models here.
