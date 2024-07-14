from django.shortcuts import render


from rest_framework.views import APIView
from class_period.models import Class_Period
from .serializers import Class_PeriodListView
from rest_framework.response import Response


class Class_PeriodListView(APIView):
    def get (self,request):
        class_period=Class_Period.objects.all()
        serializer=Class_PeriodSerializer(student, many=True)
        return Response(serializer.data)

# Create your views here.
