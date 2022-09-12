from turtle import pos
from django.db import models
from django.db.models.signals import post_save, pre_save

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=100, null=True)
    lastname = models.CharField(max_length=100,blank=True, null=True)
    roll = models.IntegerField(null=True)
    city = models.CharField(max_length=100,blank=True, null=True)
    


    class Meta:
        verbose_name_plural = "Student"

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)


# def save_post(sender, instance, **kwargs):
#     print("Post save works!!")

# def save_pre(sender, instance, **kwargs):
#     print("Pre save works!!")

# post_save.connect(save_post, sender=Post)
# pre_save.connect(save_pre, sender=Post)