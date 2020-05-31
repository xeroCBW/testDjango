from django.db import models

# Create your models here.


class Grade(models.Model):
    name = models.CharField(max_length=32,default='1')

class Student(models.Model):
    name = models.CharField(max_length=32,default='cbw')
    age = models.IntegerField(default=0)
    grade = models.CharField(max_length=32,default='1')
class Major(models.Model):
    name = models.CharField(max_length=32,default='1')