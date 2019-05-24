from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User



#class User(models.Model):
 #   name = models.CharField(max_length=30)
  #  username = models.CharField(max_length=30, default=None, unique=True)
   # email = models.EmailField(max_length=254, unique=True, default='noreply@gmail.com')
    #USERNAME_FIELD = 'username'

    #def __str__(self):
     #   return self.email


class Post(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    created = models.DateField(default=timezone.now)
    title = models.CharField(max_length=50, default=None, blank=True)
    content = models.CharField(max_length=10000, default=None)




