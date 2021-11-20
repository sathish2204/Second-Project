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


class team1_batting(models.Model):
    name = models.CharField(max_length=50)
    balls = models.IntegerField()
    runs = models.IntegerField()
    wicket = models.CharField(max_length=50,null=True)
    bowler = models.CharField(max_length=50,null=True)
class team2_batting(models.Model):
    name = models.CharField(max_length=50)
    balls = models.IntegerField()
    runs = models.IntegerField()
    wicket = models.CharField(max_length=50,null=True)
    bowler = models.CharField(max_length=50,null=True)

class team1_bowling(models.Model):
    name = models.CharField(max_length=50)
    overs = models.FloatField()
    runs = models.IntegerField()
    wickets = models.IntegerField()

class team2_bowling(models.Model):
    name = models.CharField(max_length=50)
    overs = models.FloatField()
    runs = models.IntegerField()
    wickets = models.IntegerField()
    



    
    
    

