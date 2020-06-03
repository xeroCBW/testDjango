from django.db import models
from db.base_model import BaseMode
# Create your models here.


class Grade(BaseMode):
    name = models.CharField(max_length=32,default='1')

class Student(BaseMode):
    name = models.CharField(max_length=32,default='cbw')
    age = models.IntegerField(default=0)
    grade = models.CharField(max_length=32,default='1')
class Major(BaseMode):
    name = models.CharField(max_length=32,default='1')