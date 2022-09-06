import imp
from django.contrib import admin
from .models import Student, StudentInsert
# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','roll','city']

@admin.register(StudentInsert)
class StudentInsertAdmin(admin.ModelAdmin):
    list_display = ['id','name','roll','city']

# admin.site.register(Student,StudentAdmin)

