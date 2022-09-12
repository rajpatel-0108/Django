import imp
from django.contrib import admin
from .models import Students, Post

# Register your models here.
@admin.register(Students)
class StudentAdmin(admin.ModelAdmin):
    list_display=("id","name","lastname","roll","city")
# admin.site.register(Students)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title")