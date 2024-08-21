

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


    def post(self, request, id):
        action = request.data.get('action')
        if action == 'add_to_class':
            return self.add_student_to_class(request, id)
        elif action == 'assign_teachers_course':
            return self.assign_teacher_course(request)
        elif action == 'assign_teachers_class':
            return self.assign_teacher_class(request)
        elif action == 'create_class_period':
            return self.create_class_period(request)
        elif action == 'get_weekly_timetable':
            return self.get_weekly_timetable(request)
        else:
            return Response({"error": "Invalid action"}, status=status.HTTP_400_BAD_REQUEST) 


    
    def add_student_to_class(self, request, student_id):
        class_id = request.data.get('class_id')
        try:
            student = Student.objects.get(id=student_id)
            class_obj = Classes.objects.get(id=class_id)
            class_obj.students.add(student)
            return Response({"message": "Student added to class successfully"}, status=status.HTTP_200_OK)
        except (Student.DoesNotExist, Classes.DoesNotExist):
            return Response({"error": "Student or Class not found"}, status=status.HTTP_404_NOT_FOUND)     


    def assign_teacher_course(self, request):
        teacher_id = request.data.get('teacher_id')
        course_id = request.data.get('course_id')
        try:
            teacher = Teacher.objects.get(id=teacher_id)
            course = Course.objects.get(id=course_id)
            teacher.courses.add(course)
            return Response({"message": "Teacher assigned to course successfully"}, status=status.HTTP_200_OK)
        except (Teacher.DoesNotExist, Course.DoesNotExist):
            return Response({"error": "Teacher or Course not found"}, status=status.HTTP_404_NOT_FOUND)


    def assign_teacher_class(self, request):
        teacher_id = request.data.get('teacher_id')
        class_id = request.data.get('class_id')
        try:
            teacher = Teacher.objects.get(id=teacher_id)
            class_obj = Classes.objects.get(id=class_id)
            class_obj.teacher = teacher
            class_obj.save()
            return Response({"message": "Teacher assigned to class successfully"}, status=status.HTTP_200_OK)
        except (Teacher.DoesNotExist, Classes.DoesNotExist):
            return Response({"error": "Teacher or Class not found"}, status=status.HTTP_404_NOT_FOUND)



    def create_class_period(self, request):
        teacher_id = request.data.get('teacher_id')
        course_id = request.data.get('course_id')
        class_id = request.data.get('class_id')
        start_time = request.data.get('start_time')
        end_time = request.data.get('end_time')
        day_of_week = request.data.get('day_of_week')
        try:
            teacher = Teacher.objects.get(id=teacher_id)
            course = Course.objects.get(id=course_id)
            class_obj = Classes.objects.get(id=class_id)
            class_period = ClassPeriod.objects.create(
                teacher=teacher,
                course=course,
                class_obj=class_obj,
                start_time=start_time,
                end_time=end_time,
                day_of_week=day_of_week
            )
            serializer = ClassPeriodSerializer(class_period)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except (Teacher.DoesNotExist, Course.DoesNotExist, Classes.DoesNotExist):
            return Response({"error": "Teacher, Course, or Class not found"}, status=status.HTTP_404_NOT_FOUND)


    def get_weekly_timetable(self, request):
        class_id = request.data.get('class_id')
        try:
            class_obj = Classes.objects.get(id=class_id)
            class_periods = ClassPeriod.objects.filter(class_obj=class_obj).order_by('day_of_week', 'start_time')
            timetable = {}
            for period in class_periods:
                day = period.get_day_of_week_display()
                if day not in timetable:
                    timetable[day] = []
                timetable[day].append({
                    'course': period.course.name,
                    'teacher': period.teacher.name,
                    'start_time': period.start_time.strftime('%H:%M'),
                    'end_time': period.end_time.strftime('%H:%M')
                })
            return Response(timetable, status=status.HTTP_200_OK)
        except Classes.DoesNotExist:
            return Response({"error": "Class not found"}, status=status.HTTP_404_NOT_FOUND)                             


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










class TeacherListView(APIView):
   def get (self,request):
       teacher = Teacher.objects.all()
       serializer = TeacherSerializer(teacher,many=True)
       return Response(serializer.data)
   def post(self, request):
       serializer = TeacherSerializer(data= request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data , status=status.HTTP_201_CREATED)
       else:
           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    def put(self,request):
        student=Student.objects.get(id=id)
        serializer=StudentSerializer(student,data=request.data)

        if serializer.is_values():
           serializer.save()
           return Response (serializer.data,status=status.HTTP_201_CREATED) 
           
        else:
            return Response (serializer.data,status=status.HTTP_400_BAD_REQUEST)


    def post(self, request, id):
        action = request.data.get('action')
        if action == 'add_to_class':
            return self.add_student_to_class(request, id)
        elif action == 'assign_teachers_course':
            return self.assign_teacher_course(request)
        elif action == 'assign_teachers_class':
            return self.assign_teacher_class(request)
        elif action == 'create_class_period':
            return self.create_class_period(request)
        elif action == 'get_weekly_timetable':
            return self.get_weekly_timetable(request)
        else:
            return Response({"error": "Invalid action"}, status=status.HTTP_400_BAD_REQUEST) 


    
    def add_student_to_class(self, request, student_id):
        class_id = request.data.get('class_id')
        try:
            student = Student.objects.get(id=student_id)
            class_obj = Classes.objects.get(id=class_id)
            class_obj.students.add(student)
            return Response({"message": "Student added to class successfully"}, status=status.HTTP_200_OK)
        except (Student.DoesNotExist, Classes.DoesNotExist):
            return Response({"error": "Student or Class not found"}, status=status.HTTP_404_NOT_FOUND)     


    def assign_teacher_course(self, request):
        teacher_id = request.data.get('teacher_id')
        course_id = request.data.get('course_id')
        try:
            teacher = Teacher.objects.get(id=teacher_id)
            course = Course.objects.get(id=course_id)
            teacher.courses.add(course)
            return Response({"message": "Teacher assigned to course successfully"}, status=status.HTTP_200_OK)
        except (Teacher.DoesNotExist, Course.DoesNotExist):
            return Response({"error": "Teacher or Course not found"}, status=status.HTTP_404_NOT_FOUND)


    def assign_teacher_class(self, request):
        teacher_id = request.data.get('teacher_id')
        class_id = request.data.get('class_id')
        try:
            teacher = Teacher.objects.get(id=teacher_id)
            class_obj = Classes.objects.get(id=class_id)
            class_obj.teacher = teacher
            class_obj.save()
            return Response({"message": "Teacher assigned to class successfully"}, status=status.HTTP_200_OK)
        except (Teacher.DoesNotExist, Classes.DoesNotExist):
            return Response({"error": "Teacher or Class not found"}, status=status.HTTP_404_NOT_FOUND)



    def create_class_period(self, request):
        teacher_id = request.data.get('teacher_id')
        course_id = request.data.get('course_id')
        class_id = request.data.get('class_id')
        start_time = request.data.get('start_time')
        end_time = request.data.get('end_time')
        day_of_week = request.data.get('day_of_week')
        try:
            teacher = Teacher.objects.get(id=teacher_id)
            course = Course.objects.get(id=course_id)
            class_obj = Classes.objects.get(id=class_id)
            class_period = ClassPeriod.objects.create(
                teacher=teacher,
                course=course,
                class_obj=class_obj,
                start_time=start_time,
                end_time=end_time,
                day_of_week=day_of_week
            )
            serializer = ClassPeriodSerializer(class_period)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except (Teacher.DoesNotExist, Course.DoesNotExist, Classes.DoesNotExist):
            return Response({"error": "Teacher, Course, or Class not found"}, status=status.HTTP_404_NOT_FOUND)


    def get_weekly_timetable(self, request):
        class_id = request.data.get('class_id')
        try:
            class_obj = Classes.objects.get(id=class_id)
            class_periods = ClassPeriod.objects.filter(class_obj=class_obj).order_by('day_of_week', 'start_time')
            timetable = {}
            for period in class_periods:
                day = period.get_day_of_week_display()
                if day not in timetable:
                    timetable[day] = []
                timetable[day].append({
                    'course': period.course.name,
                    'teacher': period.teacher.name,
                    'start_time': period.start_time.strftime('%H:%M'),
                    'end_time': period.end_time.strftime('%H:%M')
                })
            return Response(timetable, status=status.HTTP_200_OK)
        except Classes.DoesNotExist:
            return Response({"error": "Class not found"}, status=status.HTTP_404_NOT_FOUND)                             


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












