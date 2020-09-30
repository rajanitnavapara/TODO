from django.db import models
import datetime

# Create your models here.
class Todo(models.Model):
    date = models.DateTimeField()
    text = models.CharField(max_length = 300)
