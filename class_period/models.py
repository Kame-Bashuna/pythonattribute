# from django.db import models


# class Class_Period():
#     start_time=models.TimeField()
#     end_time=models.TimeField()
#     course=models.CharField(max_length=100)
#     classroom=models.CharField(max_length=100)
#     day_of_the_week=models.CharField(max_length=100)
    


#     def __str__(self):
#         return f"{self.course} {self.start_time}"

# # Create your models here.


from django.db import models


class Class_Period(models.Model):
    # Define your fields here
      start_time=models.TimeField()
      end_time=models.TimeField()
      course=models.CharField(max_length=100)
      classroom=models.CharField(max_length=100)
      day_of_the_week=models.CharField(max_length=100)

      def __str__(self):
        return self.start_time 
        # Example: Return a field to represent the object

