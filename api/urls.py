from django.urls import path
from .views import StudentListView
from .views import CourseListView
from .views import ClassListView
from .views import Class_PeriodListView
from .views import TeacherListView

urlpatterns=[
    path("student/",StudentListView.as_view(),name="student_list_view"),
    path("course/",CourseListView.as_view(),name="course_list_view"),
    path("class/",ClassListView.as_view(),name="class_list_view"),
    path("class_period/",Class_PeriodListView.as_view(),name="class_period_list_view"),
    path("teacher/",TeacherListView.as_view(),name="teacher_list_view"),
]


