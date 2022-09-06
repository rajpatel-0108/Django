from functools import partial
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
# Create your views here.

@api_view(['GET', 'POST', 'PUT', 'PATCH','DELETE'])
def student_api(request,pk=None):
    if request.method == "GET":
        id = pk
        # id = request.data.get('id') #it is same as pk 
        if id is not None:
            stu = Student.objects.get(id=id) #we can use pk directly here instead of id
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many = True)
        return Response(serializer.data)
    
    if request.method == "POST":
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'msg': 'Data Inserted' })
        return Response(serializer.errors)

    if request.method == "PUT":
        id = pk
        # id  = request.data.get('id') #it is same as p
        stu = Student.objects.get(pk=id)  #we can use pk directly here instead of id
        serializer = StudentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'msg': 'Data Updated' })
        return Response(serializer.errors)
    
    if request.method == "PATCH":
        id = pk
        # id  = request.data.get('id') #it is same as p
        stu = Student.objects.get(pk=id)   
        serializer = StudentSerializer(stu,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'msg': 'Data Updated' })
        return Response(serializer.errors)

    if request.method == "DELETE":
        id = pk
        # id  = request.data.get('id') #it is same as pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg': 'Data Deleted!!'})
    


















# @api_view()
# def hello_world(request):
#     return Response({'msg':'Hi there!!'})

# @api_view(['GET','POST'])
# def hello_world(request):
#     if request.method == 'GET':
#         return Response({'msg':'This one is Get request'})
#     if request.method == 'POST':
#         print(request.data)
#         return Response({'msg':'Hi there!!', 'data':request.data})