from django.db import models

# Create your models here.
class Task(models.Model):
    task_definition = models.TextField(max_length=1000)
    task_title =  models.CharField(max_length=100)

