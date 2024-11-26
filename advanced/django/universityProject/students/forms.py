from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewCourseForm(forms.Form):
    name = forms.CharField(label='Course name', max_length=200)
    teacher = forms.CharField(label='Teacher name', max_length=200)


class NewStudentForm(forms.Form):
    firstName = forms.CharField(label='Course name', max_length=200)
    lastName = forms.CharField(label='Teacher name', max_length=200)
    identifier = forms.CharField(label='Identifier (student card number)', max_length=20)
    