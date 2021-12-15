from django.shortcuts import render, HttpResponse
from .models import *
import stripe


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


def become_pro(request):
    if request.method == 'POST':
        membership = request.POST.get('membership', 'MONTHLY')
        amount = 1000
        if membership == 'YEARLY':
            amount = 3500
        stripe.api_key = "sk_test_51Jqx0YFIYgM5uAssYim24tC1MHJt9BEKUoapvNuEeImHofsaFdLOzziWfkgUFiruTmZ5lBF4Mp1R1VOMBUJaeca400RA9BNYxm"
        customer = stripe.Customer.create(
            email=request.user.email
        )
        charge = stripe.Charge.create(
            customer=customer,
            amount=amount*100,
            currency='BDT',
            description='membership'
        )
    return render(request, 'become_pro.html')
