from email.message import Message
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Program(models.Model):
    title = models.CharField(max_length=100)
    # program = models.ImageField()
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='img/Programs/Weekly')
    url = models.URLField(blank=True)



class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.CharField(max_length=250)
    date = models.DateField(auto_created=True, blank=False)