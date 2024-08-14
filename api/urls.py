from django.urls import path
from .views import StudentListView
from .views import StudentDetailView

from .views import CourseListView
from .views import CourseDetailView

from .views import Class_PeriodListView
from .views import Class_PeriodDetailView

from .views import TeacherListView
from .views import TeacherDetailView

from .views import ClassesListView
from .views import ClassesDetailView













urlpatterns=[
    path("students/",StudentListView.as_view(),name="student_list_view"),
    path("students/<int:id>/",StudentDetailView.as_view(),name="student_detail_as_view"),

    path("course/",CourseListView.as_view(),name="course_list_view"),
    path("course/<int:id>/",CourseDetailView.as_view(),name="course_detail_as_view"),

    path("classroom/",ClassesListView.as_view(),name="class_list_view"),
    path("classroom/<int:id>/",ClassesDetailView.as_view(),name="class_detail_as_view"),

    path("class_period/",Class_PeriodListView.as_view(),name="class_period_list_view"),
    path("class_period/<int:id>/",Class_PeriodListView.as_view(),name="class_period_detail_as_view"),

    path("teachers/",TeacherListView.as_view(), name="teachers_list_as_view" ),
    path("teachers/<int:id>/",TeacherListView.as_view(),name="teachers_detail_as_view"),
   


    
]


