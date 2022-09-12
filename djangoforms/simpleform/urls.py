from django.urls import path
from . import views
urlpatterns = [
    path("",views.index),
    path("insertdata",views.insertdata, name='index')
]