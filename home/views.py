from django.shortcuts import render, HttpResponse
from .models import *


# Create your views here.

def home(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request, 'home.html', context)


def view_course(request, slug):
    course = Course.objects.filter(slug=slug).first()
    course_module = CourseModule.objects.filter(course=course)

    context = {'course': course, 'course_module': course_module}
    return render(request, 'course.html', context)
