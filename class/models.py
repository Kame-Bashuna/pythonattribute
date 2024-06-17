from django.db import models

class Class(models.Model):
    material=models.CharField(max_length=20)
    table=models.PositiveSmallIntegerField()
    method_of_teaching=models.CharField(max_length=20)
    information_of_student=models.CharField(max_length=20)
    class_name=models.CharField(max_length=20)
    capacity=models.PositiveSmallIntegerField()
    chairs=models.PositiveSmallIntegerField()
    capacity=models.PositiveSmallIntegerField()
    class_assignment=models.PositiveSmallIntegerField()
    learning_hours=models.PositiveSmallIntegerField()



    def __str__(self):
        return f"{self.class_name} {self.learning_hours}"

# Create your models here.
