from django.db.models.signals import post_save, pre_save
from .models import Post, Students
from django.dispatch import receiver

def save_post(sender, instance, **kwargs):
    print("Post save works!!")

def save_pre(sender, instance, **kwargs):
    print("Pre save works!!")

post_save.connect(save_post, sender=Post)
pre_save.connect(save_pre, sender=Post)


@receiver(post_save, sender=Students)
def stud(sender, instance,created, **kwargs):
    if created:
        print(instance)
        Post.objects.create(title=instance)