from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer, StudentInsertSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def student_detail(request,pk):
    stu = Student.objects.get(id = pk)  # collecting single model object (Complex Data) 
    serializer = StudentSerializer(stu) # Converting Complex data to Native Python Data type dictionary
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type = 'application/json')
    return JsonResponse(serializer.data)  # Converting Python native data type to Json data

def student_list(request):
    stu = Student.objects.all()
    serializer = StudentSerializer(stu, many=True)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type = 'application/json')
    return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentInsertSerializer(data=pythondata)
        if serializer.is_valid():
            # print(serializer.validated_data)
            serializer.save()
            # res = { 'msg' : 'Data Created' }
            # json_data = JSONRenderer().render(res)
            # return HttpResponse(json_data, content_type = 'application/json')
            # return JsonResponse(res)        
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type = 'application/json')