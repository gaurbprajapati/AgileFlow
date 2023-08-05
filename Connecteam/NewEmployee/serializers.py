# newemployee/serializers.py

from rest_framework import serializers
from .models import NewEmployee


class NewEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewEmployee
        fields = '__all__'
