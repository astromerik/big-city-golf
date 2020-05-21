from django.shortcuts import render

# Create your views here.


def index(request):
    """ A view to render index.html (Home page)"""
    return render(request, 'home/index.html')

def about(request):
    """ A view to render about.html (About page)"""
    return render(request, 'home/about.html')
