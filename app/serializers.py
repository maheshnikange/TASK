from .models import Task
from rest_framework.serializers import Serializer
from rest_framework import serializers

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields='__all__'