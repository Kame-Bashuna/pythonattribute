from django.urls import path
from .views import StudentListView,CourseListView,ClassListView,ClassPeriodListView,TeacherListView,StudentDetailView



urlpatterns=[
    path("student/",StudentListView.as_view(),name="student_list_view"),
    path("course/",CourseListView.as_view(),name="course_list_view"),
    path("class/",ClassListView.as_view(),name="class_list_view"),
    path("class_period/",ClassPeriodListView.as_view(),name="class_period_list_view"),
    path("teacher/",TeacherListView.as_view(),name="teacher_list_view"),
    path("students/<int:id>/",StudentDetailView.as_view(),name="student_detail_as_view"),
    
]


