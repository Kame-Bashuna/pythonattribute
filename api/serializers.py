from rest_framework import serializers
from class_period.models import Class_Period
from student.models import Student
from teachers.models import Teachers
from course.models import Course
from classroom.models import Classes

class Classroom_PeriodSerializer(serializers.ModelSerializer):
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
        fields="__all__"

class ClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Classes
        fields="__all__"        





