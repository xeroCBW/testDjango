from django.urls import path
from . import views


urlpatterns = [

    path('', views.index),
    path('home/', views.home),
    path('list_student/',views.list_student),
    path('modify_student/',views.modify_student),
    path('add_student/', views.add_student),
    path('delete_student/',views.delete_student),


    path('grade_students/',views.grade_students),
    path('grade/',views.grade),
]