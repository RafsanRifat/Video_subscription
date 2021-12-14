from django.shortcuts import render, HttpResponse
from .models import *


# Create your views here.

def home(request):
    course = Course.objects.all()
    context = {'course': course}
    return render(request, 'home.html', context)
