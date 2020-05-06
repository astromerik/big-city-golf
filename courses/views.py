from django.shortcuts import render
from .models import Course
# Create your views here.


def courses(request):
    """ A view to render all courses available """

    courses = Course.objects.all()

    context = {
        'courses': courses,
    }

    return render(request, 'courses/courses.html', context)
