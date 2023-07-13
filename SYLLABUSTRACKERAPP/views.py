from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

def course(request):
    return render(request,'course.html')

def coursesyllabus(request):
    return render(request,'coursesyllabus.html')

def day(request):
    return render(request,'day.html')

def syllabus(request):
    return render(request,'syllabus.html')

