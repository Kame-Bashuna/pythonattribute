from rest_framework import serializers
from .models import Class_Period
from .models import Student
from .models import Teachers
from .models import Course
# from class.models import Class


class Class_PeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model=Class_Period
        fields="__all__"


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Student
        fields="__all__"

class TeachersSerializer(serializers.ModelSerializer):
    class Meta:
        model=Teachers
        fields="__all__"

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        field="__all__"

# class ClassSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Class
#         fields="__all__"        





