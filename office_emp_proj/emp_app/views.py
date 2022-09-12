from django.shortcuts import render, HttpResponse
from .models import Department, Employee, Role
from datetime import datetime
from django.db.models import Q


# Create your views here.
def index(request):
    return render(request, 'index.html')


def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    print(context)
    return render(request, 'view_all_emp.html', context)


def add_emp(request):
    dept = Department.objects.all()
    role = Role.objects.all()
    context = {
        'dept': dept,
        'role': role
    }
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        rolename = request.POST['role']
        deptname = request.POST['dept']
        deptid = Department.objects.filter(name= deptname).values_list("id", flat=True)
        dept_nid = deptid[0]
        print(deptid)
        roleid = Role.objects.filter(name=rolename).values_list("id",flat=True)
        role_nid=roleid[0]
        new_emp = Employee(first_name= first_name, last_name=last_name, salary=salary, bonus=bonus, phone=phone, dept_id = dept_nid, role_id = role_nid, hire_date = datetime.now())
        print(new_emp)
        new_emp.save()
        return HttpResponse('Employee added Successfully')
    elif request.method=='GET':
        return render(request, 'add_emp.html',context)
    else:
        return HttpResponse("An Exception Occured! Employee Has Not Been Added")


def remove_emp(request, emp_id = 0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee Removed Successfully")
        except:
            return HttpResponse("Please Enter A Valid EMP ID")
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    return render(request, 'remove_emp.html',context)


def filter_emp(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if dept:
            emps = emps.filter(dept__name__icontains = dept)
        if role:
            emps = emps.filter(role__name__icontains = role)

        context = {
            'emps': emps
        }
        return render(request, 'view_all_emp.html', context)

    elif request.method == 'GET':
        return render(request, 'filter_emp.html')
    else:
        return HttpResponse('An Exception Occurred')

def add_dep(request):
    if request.method == 'POST':
        dep_name = request.POST['dep_name']
        dep_location = request.POST['dep_location']
        new_dep = Department(name= dep_name, location=dep_location)
        new_dep.save()
        return HttpResponse('Department added Successfully')
    elif request.method=='GET':
        return render(request, 'add_dept.html')
    else:
        return HttpResponse("An Exception Occured! Department Has Not Been Added")

