from django.db import models

class Classes(models.Model):
    class_name=models.CharField(max_length=20)
    material=models.CharField(max_length=20)
    method_of_teaching=models.CharField(max_length=20)
    class_prefect=models.CharField(max_length=20)
    trainer = models.CharField(max_length=100, null=False, default='default_trainer')
    table= models.PositiveSmallIntegerField()
    chairs=models.PositiveSmallIntegerField()
    class_numberof_student=models.PositiveSmallIntegerField()
    class_assignment=models.PositiveSmallIntegerField()
    learning_hours=models.PositiveSmallIntegerField()
    


def __str__(self):
     return f"{self.class_name} {self.learning_hours}"

# Create your models here.
