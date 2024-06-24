from django.db import models

class Teachers(models.Model):
     first_name=models.CharField(max_length=20)
     last_name=models.CharField(max_length=20)
     age=models.PositiveSmallIntegerField()
     email=models.EmailField()
     country=models.CharField(max_length=20)
     subject=models.CharField(max_length=20)
     years_of_experience=models.PositiveSmallIntegerField()
     office_hours=models.PositiveSmallIntegerField()
     office_room_number=models.PositiveSmallIntegerField()
     id_number=models.PositiveSmallIntegerField()
  

def __str__(self):
        return f"{self.first_name} {self.last_name} {self.years_of_experience}"
# Create your models here.
