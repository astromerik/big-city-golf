from django.shortcuts import render, get_object_or_404
from .models import Course
# Create your views here.


def courses(request):
    """ A view to render all courses available """

    courses = Course.objects.all()

    context = {
        'courses': courses,
    }

    return render(request, 'courses/courses.html', context)
    

def course_detail(request, course_id):
    """ A view to show information about a specific golf course """

    course = get_object_or_404(Course, pk=course_id)

    context = {
        'course': course,
    }

    return render(request, 'courses/course_detail.html', context)