from django.shortcuts import render

# Create your views here.


def courses(request):
    """ A view to render index.html (Home page)"""
    return render(request, 'courses/courses.html')
