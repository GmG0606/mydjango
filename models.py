from django.db import models
from django.contrib.auth.models import User 
# Create your models here.
class UserSerializer(models.Model):
  name = models.CharField(max_length=20)
  usernane = models.CharField(max_length=25)
  password = models.IntegerField(max_length=12)