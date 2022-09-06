from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
# Create your views here.

@method_decorator(csrf_exempt, name='dispatch')
class StudentAPI(View):
    def get(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        # print(pythondata)
        id = pythondata.get('id', None)
        # print(id)
        if id is not None:
            stu = Student.objects.get(id=id)
            # print(stu)
            serializer = StudentSerializer(stu)
            # print(serializer)
            # json_data = JSONRenderer().render(serializer.data)
            # return HttpResponse(json_data, content_type = 'application/json')
            return JsonResponse(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        # json_data = JSONRenderer().render(serializer.data)
        # return HttpResponse(json_data, content_type = 'application/json')
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data Inserted'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type = 'application/json')
        # json_data = JSONRenderer().render(serializer.errors)
        # return HttpResponse(json_data, content_type = 'application/json')
        return JsonResponse(serializer.errors)

    def put(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        # print(stream)
        pythondata = JSONParser().parse(stream)
        # print(pythondata)
        id = pythondata.get('id')
        # print(id)
        stu = Student.objects.get(id=id)
        # print(stu)
        serializer = StudentSerializer(stu, data=pythondata, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data Updated!!'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type = 'application/json')
        res = {'msg': 'Error in Updating!!'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type = 'application/json')
        # json_data = JSONRenderer().render(serializer.errors)
        # return HttpResponse(json_data, content_type = 'application/json')

    def delete(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        res = {'msg': 'Data Deleted!!'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type = 'application/json')



# @csrf_exempt
# def Student_api(request):
#     if request.method == 'GET':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         # print(pythondata)
#         id = pythondata.get('id', None)
#         # print(id)
#         if id is not None:
#             stu = Student.objects.get(id=id)
#             # print(stu)
#             serializer = StudentSerializer(stu)
#             # print(serializer)
#             # json_data = JSONRenderer().render(serializer.data)
#             # return HttpResponse(json_data, content_type = 'application/json')
#             return JsonResponse(serializer.data)
#         stu = Student.objects.all()
#         serializer = StudentSerializer(stu, many=True)
#         # json_data = JSONRenderer().render(serializer.data)
#         # return HttpResponse(json_data, content_type = 'application/json')
#         return JsonResponse(serializer.data, safe=False)
   
#     if request.method == 'POST':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         serializer = StudentSerializer(data=pythondata)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg':'Data Inserted'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type = 'application/json')
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data, content_type = 'application/json')
    
#     if request.method == 'PUT':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         # print(stream)
#         pythondata = JSONParser().parse(stream)
#         # print(pythondata)
#         id = pythondata.get('id')
#         # print(id)
#         stu = Student.objects.get(id=id)
#         # print(stu)
#         serializer = StudentSerializer(stu, data=pythondata, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg':'Data Updated!!'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type = 'application/json')
#         res = {'msg': 'Error in Updating!!'}
#         json_data = JSONRenderer().render(res)
#         return HttpResponse(json_data, content_type = 'application/json')
#         # json_data = JSONRenderer().render(serializer.errors)
#         # return HttpResponse(json_data, content_type = 'application/json')
    
#     if request.method == 'DELETE':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         id = pythondata.get('id')
#         stu = Student.objects.get(id=id)
#         stu.delete()
#         res = {'msg': 'Data Deleted!!'}
#         json_data = JSONRenderer().render(res)
#         return HttpResponse(json_data, content_type = 'application/json')

        