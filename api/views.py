

from rest_framework.views import APIView
from class_period.models import Class_Period
from student.models import Student
from .serializers import StudentSerializer
from teachers.models import Teachers
from .serializers import TeachersSerializer
from course.models import Course
from .serializers import CourseSerializer
from classroom.models import Classes
from .serializers import ClassesSerializer



from rest_framework import status
from rest_framework.response import Response


       
class StudentListView(APIView):
    def get (self,request):
        student=Student.objects.all()
        serializer=StudentSerializer(student, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=StudentListView(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors,status=status.HTTP_BADREQUEST)    
            
class StudentDetailView(APIView):
    def get (self,request):
        student=Student.objects.all(id=id)
        first_name=request.query_params.get("first_name")
        country=request.query_params.get("country")
        if first_name:
            student=students.objects.filter(firstname=first_name)

        if country:
            student=students.objects.filter(country=country)    
        serializer=StudentSerializer(students,many=True)
        return Response(serializer.data)  

    def put(self,request):
        student=Student.objects.get(id=id)
        serializer=StudentSerializer(student,data=request.data)

        if serializer.is_values():
           serializer.save()
           return Response (serializer.data,status=status.HTTP_201_CREATED) 
           
        else:
            return Response (serializer.data,status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,id):
        student=Student.objects.get(id=id)
        student.delete()
        return Response(status=status.HTTP_202_ACCEPTED)    


    def enroll_student(self,student,code):
        code=Code.objects.get(id=code)
        studentcourses.add(code)


    def post(self,request,id):
        student=Student.objects.get(id=id)
        action=request.data.get("action")
        if action=="email":
            code=request.data.get("code")  
            self.enroll_student(student,code)
            return Response(status=status.HTTP_202_ACCEPTED)    




class Class_PeriodListView(APIView):
    def get (self,request):
        class_period=Class_Period.objects.all()
        serializer=Class_PeriodSerializer(class_period, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=ClassPeriodListView(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors,status=status.HTTP_BADREQUEST)  


            

class Class_PeriodDetailView(APIView):
    def get (self,request):
        class_period=Class_Period.objects.all(id=id)
        serializer=Class_PeriodSerializer("class_period")
        return Response(serializer.data)  

    def put(self,request):
        class_period=Class_Period.objects.get(id=id)
        serializer=StudentSerializer(class_period,data=request.data)

        if serializer.is_values():
           serializer.Save()
           return Response (serializer.data,status=status.HTTP_201_CREATED) 
           
        else:
            return Response (serializer.data,status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,id):
        class_period=Class_Period.objects.get(id=id)
        student.delete()
        return Response(status=status.HTTP_202_ACCEPTED)              




class ClassesDetailView(APIView):
    def get (self,request):
        classes=Classes.objects.filter(id=id)
        serializer=ClassesSerializer("class")
        return Response(serializer.data)  

    def put(self,request):
        classes=Classes.objects.get(id=id)
        serializer=ClassesSerializer(classes,data=request.data)

        if serializer.is_values():
           serializer.Save()
           return Response (serializer.data,status=status.HTTP_201_CREATED) 
           
        else:
            return Response (serializer.data,status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,id):
        classes=Classes.objects.get(id=id)
        classes.delete()
        return Response(status=status.HTTP_202_ACCEPTED)  


class ClassesListView(APIView):
    def get (self,request):
        classes=Classes.objects.all()
        serializer=ClassesSerializer(classes, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=ClassesListView(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors,status=status.HTTP_BADREQUEST)         

        
             
           


class TeacherListView(APIView):
    def get (self,request):
        teacher=Teacher.objects.all()
        serializer=TeacherSerializer(teachers, many=True)
        return Response(serializer.data) 

    def post(self,request):
        serializer=TeacherListView(data=request.data)
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
        serializer=TeacherSerializer(teacher,data=request.data)

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
        serializer=CourseSerializer(course,data=request.data)

        if serializer.is_values():
           serializer.Save()
           return Response (serializer.data,status=status.HTTP_201_CREATED) 
           
        else:
            return Response (serializer.data,status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,id):
        course=Course.objects.get(id=id)
        teacher.delete()
        return Response(status=status.HTTP_202_ACCEPTED)  





