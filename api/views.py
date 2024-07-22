

from rest_framework.views import APIView
from class_period.models import ClassPeriod
from .serializers import ClassPeriodListView
from student.models import Student
from .serializers import StudentListView
from teacher.models import Teacher
from .serializers import TeacherListView
from course.models import Course
from .serializers import CourseListView



from rest_framework import status
from rest_framework.response import Response



        
class StudentListView(APIView):
    def get (self,request):
        student=Student.objects.all()
        serializer=StudentSerializer(student, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=StudentListView(data=requestdata)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors,status=status.HTTP_BADREQUEST)    
            
class StudentDetailView(APIView):
    def get (self,request):
        student=Student.objects.all(id=id)
        serializer=StudentSerializer("student")
        return Response(serializer.data)  

    def put(self,request):
        student=Student.objects.get(id=id)
        serializer=StudentSerializer(student,data=requestdata)

        if serializer.is_values():
           serializer.Save()
           return Response (serializer.data,status=status.HTTP_201_CREATED) 
           
        else:
            return Response (serializer.data,status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,id):
        student=Student.objects.get(id=id)
        student.delete()
        return Response(status=status.HTTP_202_ACCEPTED)        


class Class_PeriodListView(APIView):
    def get (self,request):
        class_period=Class_Period.objects.all()
        serializer=Class_PeriodSerializer(class_period, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=ClassPeriodListView(data=requestdata)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors,status=status.HTTP_BADREQUEST)  


 class ClassDetailView(APIView):
    def get (self,request):
        class=Class.objects.all(id=id)
        serializer=ClassSerializer("class")
        return Response(serializer.data)  

    def put(self,request):
        class=Class.objects.get(id=id)
        serializer=ClassSerializer(class,data=requestdata)

        if serializer.is_values():
           serializer.Save()
           return Response (serializer.data,status=status.HTTP_201_CREATED) 
           
        else:
            return Response (serializer.data,status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,id):
        class=Class.objects.get(id=id)
        class.delete()
        return Response(status=status.HTTP_202_ACCEPTED)        
           



class TeacherListView(APIView):
    def get (self,request):
        teacher=Teacher.objects.all()
        serializer=TeacherSerializer(teachers, many=True)
        return Response(serializer.data) 

    def post(self,request):
        serializer=TeacherListView(data=requestdata)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors,status=status.HTTP_BADREQUEST) 


 class TeacherDetailView(APIView):
    def get (self,request):
        teacher=Teacher.objects.all(id=id)
        serializer=TeacherSerializer("teacher")
        return Response(serializer.data)  

    def put(self,request):
        teacher=Teacher.objects.get(id=id)
        serializer=TeacherSerializer(teacher,data=requestdata)

        if serializer.is_values():
           serializer.Save()
           return Response (serializer.data,status=status.HTTP_201_CREATED) 
           
        else:
            return Response (serializer.data,status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,id):
        teacher=Teacher.objects.get(id=id)
        teacher.delete()
        return Response(status=status.HTTP_202_ACCEPTED)              




class CourseListView(APIView):
    def get (self,request):
        course=Course.objects.all()
        serializer=CourseSerializer(course, many=True)
        return Response(serializer.data)   

    def post(self,request):
        serializer=CourseListView(data=requestdata)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors,status=status.HTTP_BADREQUEST)  



 class CourseDetailView(APIView):
    def get (self,request):
        course=Course.objects.all(id=id)
        serializer=CourseSerializer("course")
        return Response(serializer.data)  

    def put(self,request):
        course=Course.objects.get(id=id)
        serializer=CourseSerializer(course,data=requestdata)

        if serializer.is_values():
           serializer.Save()
           return Response (serializer.data,status=status.HTTP_201_CREATED) 
           
        else:
            return Response (serializer.data,status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,id):
        course=Course.objects.get(id=id)
        teacher.delete()
        return Response(status=status.HTTP_202_ACCEPTED)                   














# Create your views here.
