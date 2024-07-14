from rest_framework import serializers
from Class_Period.models import Class_Period


class Class_PeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model=Class_Period
        field="__all__"
