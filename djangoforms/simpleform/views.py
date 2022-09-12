from django.shortcuts import render
from .forms import Student
from .models import Students
from django.http import HttpResponseRedirect
from django.core.signals import request_finished
from django.dispatch import receiver
from django.core.paginator import Paginator
from django.contrib import messages



# Create your views here.
def index(request):
    if request.method == "POST":
        form = Student(request.POST) 
        if form.is_valid():
            # print(form.cleaned_data)
            # studentdata = Students(
            #     name = form.cleaned_data['name'],
            #     lastname = form.cleaned_data['lastname'],
            #     roll = form.cleaned_data['roll'],
            #     city = form.cleaned_data['city']
            # )
            # studentdata.save()
            form.save()
            messages.success(request, "Student Added Successfully!")
            return HttpResponseRedirect("/insertdata")   
    else:
        form = Student()
    return render(request, "simpleform/student.html", {
    "form":form
})
    # return HttpResponse("hello world")

def insertdata(request):
    Student = Students.objects.all()

    student_paginator = Paginator(Student,4)

    page_num = request.GET.get('page')
    
    page = student_paginator.get_page(page_num)

    return render(request, "simpleform/index.html",{
        "page" : page

    })


@receiver(request_finished)
def func(sender=insertdata, **kwargs):
    print("Request Finished")