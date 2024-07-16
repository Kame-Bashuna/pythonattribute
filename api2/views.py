from django.shortcuts import render


from rest_framework.views import APIView
from class_period.models import Class_Period
from .serializers import Class_PeriodListView
from student.models import Student
from .serializers import StudentListView
from teacher.models import Teacher
from .serializers import TeacherListView
from course.models import Course
from .serializers import CourseListView
from rest_framework.response import Response


class Class_PeriodListView(APIView):
    def get (self,request):
        class_period=Class_Period.objects.all()
        serializer=Class_PeriodSerializer(class_period, many=True)
        return Response(serializer.data)



class StudentListView(APIView):
    def get (self,request):
        student=Student.objects.all()
        serializer=StudentSerializer(student, many=True)
        return Response(serializer.data)

class TeacherListView(APIView):
    def get (self,request):
        student=Student.objects.all()
        serializer=TeacherSerializer(teacher, many=True)
        return Response(serializer.data) 


class CourseListView(APIView):
    def get (self,request):
        student=Student.objects.all()
        serializer=CourseSerializer(course, many=True)
        return Response(serializer.data)   

                  

# Create your views here.
