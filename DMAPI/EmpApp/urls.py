import re
from django.urls import path ,re_path
# from django.conf.urls import url 
from EmpApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path('department',views.departmentApi),
    re_path(r'^department/([0-9]+)$',views.departmentApi),
    # path('department/<int:id>',views.departmentApi),
    path('employee',views.employeeApi),
    path('employee/<int:pk>',views.employeeApi),
    # path('employee/savefile',views.SaveFile)
# ]+static(settings.MEDIA_path,document_root=settings.MEDIA_ROOT)
]