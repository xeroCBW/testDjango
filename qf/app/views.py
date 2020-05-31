import random

from django.shortcuts import render,HttpResponse,redirect
from .models import Student,Grade
# Create your views here.



def index(request):

    list = Student.objects.all()


    return render(request,'index.html',{'list':list})


def home(request):
    return render(request,'home.html')


def add_student(request):

    student = Student()
    student.name = 'cbw%d' % random.randrange(0,100)
    # student.grade = Grade()
    student.save()

    return index(request)


def delete_student(request):






    return index(request)


def list_student(request):



    return index(request)


def modify_student(request):

    student = Student.objects.get(pk=1)
    student.age += 1
    student.save()

    return index(request)


def grade_students(request):


    pass

    # grade = Grade.objects.get(name='1')
    # list =  grade.student_set.all()
    #
    # return render(request,'grade.html',{'list':list})