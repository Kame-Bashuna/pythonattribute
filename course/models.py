from django.db import models

class Course(models.Model):
    code=models.PositiveSmallIntegerField()
    name=models.CharField(max_length=20)
    learning_method=models.CharField(max_length=20)
    learning_course_hours=models.PositiveSmallIntegerField()
    course_level=models.CharField(max_length=20)
    course_trainer=models.PositiveSmallIntegerField()
    learning_material=models.CharField(max_length=20)
    course_assignment=models.PositiveSmallIntegerField()
    course_student=models.PositiveSmallIntegerField()
    course_about = models.CharField(max_length=100, null=False, default='default_course_about')

    





    

    def __str__(self):
        return f"{self.code} {self.name}"

# Create your models here.
