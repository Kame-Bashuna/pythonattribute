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


class MinimalClassPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model=ClassPeriod
        fields=["id","start_time","end_time"]




class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Student
        fields="__all__"

class MinimalStudentSerializer(serializers.ModelSerializer):
    full_name=serializers.SerializerMethodField()
    def get_full_name(self,object):
        return f"{object.first_name} {object.last_name}"
    class Meta:
        model=Student
        fields=["id","full_name","email"]        
        



class TeachersSerializer(serializers.ModelSerializer):
    class Meta:
        model=Teachers
        fields="__all__"



class MinimalTeachersSerializer(serializers.ModelSerializer):
    full_name=serializers.SerializerMethodField()
    def get_full_name(self,object):
        return f"{object.first_name} {object.last_name}"
    class Meta:
        model=Teachers
        fields=["id","full_name","email","years-of-experience"]




class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields="__all__"



class MinimalCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields=["id","title","course_code","number_of_topics","duration"]





class ClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Classes
        fields="__all__"     


class MinimalClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Classes
        fields=["id","class_name"]           








