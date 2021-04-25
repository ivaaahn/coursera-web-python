from django.db.models import *
from django.utils import timezone

# Create your models here.

class User(Model):
    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255)


class Blog(Model):
    title = CharField(max_length=255)
    author = ForeignKey(User, on_delete=CASCADE)
    created = DateTimeField(default=timezone.now)

    subscribers = ManyToManyField(User, related_name='subsriptions')

class Topic(Model):
    title = CharField(max_length=255)
    blog = ForeignKey(Blog, on_delete=CASCADE)
    author = ForeignKey(User, on_delete=CASCADE)
    created = DateTimeField(default=timezone.now)
    
    likes = ManyToManyField(User, related_name='likes')