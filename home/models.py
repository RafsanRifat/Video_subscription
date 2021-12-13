from django.db import models
from django.utils.text import slugify

# Create your models here.

class Course(models.Model):
    course_name = models.CharField(max_length=80)
    course_description = models.TextField()
    is_premium = models.BooleanField(default=False)
    course_image = models.ImageField(upload_to='course.png')
    slug = models.SlugField(blank=True)
