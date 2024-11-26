from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),    
    path('courses/', views.getCourses, name='courses'),
    path('students/', views.getStudents, name='students'),
    path('newcourse/', views.createNewCourse, name='newcourse'), 
    path('newstudent/', views.createNewStudent, name='newstudent')
]