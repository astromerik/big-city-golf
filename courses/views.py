from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Course, District, TeeTime
# Create your views here.


def courses(request):
    """ A view to render all courses available and search/filter """

    courses = Course.objects.all()
    query = None
    districts = None
    direction = None
    sort = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            courses = courses.order_by(sortkey)

        if 'district' in request.GET:
            district = request.GET['district']
            courses = courses.filter(district__name=district)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "No search criteria used")
                return redirect(reverse('courses'))

            queries = Q(course_name__icontains=query)
            courses = courses.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'courses': courses,
        'search_term': query,
        'current_districts': districts,
        'current sorting': current_sorting,
    }

    return render(request, 'courses/courses.html', context)


def course_detail(request, course_id):
    """ A view to show information about a specific golf course """

    course = get_object_or_404(Course, pk=course_id)

    context = {
        'course': course,
    }

    return render(request, 'courses/course_detail.html', context)


def book_tee_time(request, course_id):
    """ A view to book a tee time """

    if request.POST:
        tee_time_form = TeeTime(request.POST)
        if tee_time_form.is_valid():
            tee_time_form.save()
        return render(request, 'golfprofile/golfprofile.html')
