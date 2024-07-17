from django.urls import path
from .views import StudentListView

urlpatterns=[
    path("student/",StudentListView.as_view(),name="student_list_view")
]

urlpatterns=[
    path("course/",StudentListView.as_view(),name="course_list_view")
]

urlpatterns=[
    path("class/",StudentListView.as_view(),name="class_list_view")
]

urlpatterns=[
    path("class_period/",StudentListView.as_view(),name="class_period_list_view")
]
