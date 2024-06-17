from django.db import models

class Course(models.Model):
    code=models.PositiveSmallIntegerField()
    learning_course_hours=models.PositiveSmallIntegerField()
    name=models.CharField(max_length=20)
    learning_method=models.CharField(max_length=20)
    course_what_about=models.CharField(max_length=20)
    course_level=models.PositiveSmallIntegerField()
    course_trainer=models.PositiveSmallIntegerField()
    learning_material=models.PositiveSmallIntegerField()
    course_assignment=models.PositiveSmallIntegerField()
    course_student=models.PositiveSmallIntegerField()



    def __str__(self):
        return f"{self.code} {self.name}"

# Create your models here.
