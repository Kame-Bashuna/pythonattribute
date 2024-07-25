from django.urls import path
from .views import StudentListView
from .views import CourseListView
from .views import Class_PeriodListView
from .views import TeacherListView
from .views import ClassesListView
from .views import StudentDetailView





urlpatterns=[
    path("student/<int:id>/",StudentListView.as_view(),name="student_list_view"),
    path("course/<int:id>/",CourseListView.as_view(),name="course_list_view"),
    path("classroom/<int:id>/",ClassesListView.as_view(),name="class_list_view"),
    path("class_period/<int:id>/",Class_PeriodListView.as_view(),name="class_period_list_view"),
    path("teachers/<int:id>/",TeacherListView.as_view(),name="teachers_list_view"),
    path("student/<int:id>/",StudentDetailView.as_view(),name="student_detail_as_view"),
    
]


