from django.shortcuts import render,redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task
# Create your views here.

@api_view(['GET','POST','DELETE','PUT'])
def index(request,id=None):
    if request.method=='GET':
        id=id
        if id is not None:
            drinks = Task.objects.get(id=id)
            serializer = TaskSerializer(drinks)
            return Response(serializer.data)
        task_data=Task.objects.all()
        task_serializer=TaskSerializer(task_data,many=True)
        return Response(task_serializer.data)

    elif(request.method == 'POST'):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'PUT':
        id=id
        emp=Task.objects.get(id=id)
        serializer = TaskSerializer(emp,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
