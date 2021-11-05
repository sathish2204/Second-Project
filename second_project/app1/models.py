from os import name
from django.db import models

class employe(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    salary = models.IntegerField()
    city = models.CharField(max_length=50)
    

