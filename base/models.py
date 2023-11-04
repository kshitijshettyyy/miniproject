from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    image=models.ImageField(upload_to='events/%y',null=True)
    name=models.CharField(max_length=100,null=True)
    email=models.EmailField(unique=True,null=True)
    bio=models.TextField(null=True,blank=True)
    event_paricipant=models.BooleanField(default=True,null=True)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username']
    pass

class Event(models.Model):
    image=models.ImageField(upload_to='profile_pics/%y',null=True)
    name=models.CharField(max_length=100,null=True)
    description=models.TextField(null=True,blank=True)
    participants=models.ManyToManyField(User,blank=True,related_name='events')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    date=models.DateTimeField()

    def __str__(self):
        return self.name
