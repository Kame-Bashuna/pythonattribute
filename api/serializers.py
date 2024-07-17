from rest_framework import serializers
from class_period.models import Class_Period
from student.models import Student
from teacher.models import Teacher
from course.models import Course
from class.models import Class




class Class_PeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model=Class_Period
        field="__all__"


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        field="__all__"

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model=Teacher
        field="__all__"

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        field="__all__"

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model=Class
        field="__all__"        


        

