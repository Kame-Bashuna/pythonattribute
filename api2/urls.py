from django.urls import path
from .views import Class_PeriodListView

urlpatterns=[
    path("class_period/",Class_PeriodListView.as_view(),name="class_period_list_view")
]