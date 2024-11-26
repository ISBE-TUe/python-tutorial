from django.db import models


class Course(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200)
    teacher = models.CharField(max_length=200)


class Student(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    identifier = models.IntegerField(blank=True, default=0, null=True)    
    course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True)