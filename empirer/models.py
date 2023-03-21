from email.message import Message
from django.db import models
from django.contrib.auth.models import User


class Program(models.Model):
    title = models.CharField(max_length=100)
    # program = models.ImageField()
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='img/Programs/Weekly')
    url = models.URLField(blank=True)
    image_url = models.URLField(blank=True, null=True)



class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.CharField(max_length=250)
    date = models.DateField(auto_created=True, blank=False)



class Weekly(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField(null=True, blank=True, max_length=1000)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-updated", "-created"]



class Live(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField(null=True, blank=True, max_length=1000)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-updated", "-created"]

