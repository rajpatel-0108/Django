from dataclasses import fields
from django import forms
from .models import Students
# class Student(forms.Form):
#     name = forms.CharField(label = "First Name" ,max_length=100, required=False)
#     lastname = forms.CharField(label = "Last Name", max_length=100, required=False)
#     roll = forms.IntegerField(required=False)
#     city = forms.CharField(max_length=100, required=False)
    
class Student(forms.ModelForm):

    class Meta:
        model = Students
        fields = '__all__'