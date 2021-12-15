from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('', home),
    path('course/<slug>/', view_course, name="course"),
    path('become_pro/', become_pro, name="become_pro"),
]