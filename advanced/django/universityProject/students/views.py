from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Course, Student
from .forms import NewCourseForm, NewStudentForm


def index(request):
    return HttpResponse("Hello, world. You're at the students index.")

def getCourses(request):    
        courses = Course.objects.all()
        context={       
            'courses': courses,
        } 
        return render(request, 'courses.html', context)

def getStudents(request):    
        students = Student.objects.all()
        context={       
            'students': students,
        } 
        return render(request, 'students.html', context)

def createNewCourse(request):    
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NewCourseForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():            

            course = Course()
            course.name = form.cleaned_data['name']
            course.teacher = form.cleaned_data['teacher']  
            course.save()

            return redirect('courses')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NewCourseForm()

    return render(request, 'newcourse.html', {'form': form})

def createNewStudent(request):      
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NewStudentForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():            

            student = Student()
            student.firstName = form.cleaned_data['firstName']
            student.lastName = form.cleaned_data['lastName']  
            student.identifier = form.cleaned_data['identifier']  
            student.save()

            return redirect('students')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NewStudentForm()

    return render(request, 'newstudent.html', {'form': form})
