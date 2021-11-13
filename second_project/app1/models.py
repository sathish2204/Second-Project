from os import name
from django.db import models

class employe(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    salary = models.IntegerField()
    city = models.CharField(max_length=50)

class india(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    runs = models.IntegerField()

class australia(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    runs = models.IntegerField()



    
    
    

