from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Course
# Create your views here.


def courses(request):
    """ A view to render all courses available and search/filter """

    courses = Course.objects.all()
    query = None 
    
    if request.GET:
        if 'a' in request.GET:
            query = request.GET['a']
            if not query:
                messages.error(request, "No search criteria used")
                return redirect(reverse('courses'))

            queries = Q(course_name__icontains=query)
            courses = courses.filter(queries)
    
    context = {
        'courses': courses,
        'search_term': query
    }

    return render(request, 'courses/courses.html', context)
    

def course_detail(request, course_id):
    """ A view to show information about a specific golf course """

    course = get_object_or_404(Course, pk=course_id)

    context = {
        'course': course,
    }

    return render(request, 'courses/course_detail.html', context)



