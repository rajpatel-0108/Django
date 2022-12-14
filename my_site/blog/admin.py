from django.contrib import admin
from .models import Tag, Author, Post, Comment

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter= ("author", "tags", "date",)
    list_display= ("title","date","author",)

class CommentAdmin(admin.ModelAdmin):
    list_display = ("user_name", "post","text")

admin.site.register(Post,PostAdmin)
admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(Comment, CommentAdmin)