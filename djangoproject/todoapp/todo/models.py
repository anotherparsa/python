from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField()
    password = models.CharField()


class Task(models.Model):
    title = models.CharField()
    task = models.CharField()
    created = models.DateTimeField(auto_now_add=True)