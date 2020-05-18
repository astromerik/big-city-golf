from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.db.models import Q
from .models import Course, TeeTime, UserProfile
from .forms import TeeTimeForm
# Create your views here.


def courses(request):
    """ A view to render all courses available and search/filter """

    courses = Course.objects.all()
    query = None
    districts = None
    direction = None
    sort = None
    tee_time_form = TeeTimeForm()

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
        'tee_time_form': tee_time_form,
    }

    return render(request, 'courses/courses.html', context)


def course_detail(request, course_id):
    """ A view to show information about a specific golf course """

    course = get_object_or_404(Course, pk=course_id)

    context = {
        'course': course,
    }

    return render(request, 'courses/course_detail.html', context)

@require_POST
def book_course(request):
    # Get the "bag" of courses that the user wants to book 
    course_bag = request.session.get('course_bag', {})

    # Get the course id/tee time for the current course they are booking
    course_id = request.POST.get('course')
    course = get_object_or_404(Course, pk=course_id)
    booked_time = request.POST.get('tee_time')
    print(booked_time)
    # Check whether the tee time has already been booked for that course
    booking_exist = TeeTime.objects.filter(course=course_id,
                                           tee_time=booked_time[0]).exists()

    # If so, return an error and redirect
    if booking_exist:
        messages.error(request, "Tee time is already booked")
        return redirect(reverse('courses'))

    # Otherwise, just add it to the bag
    if not course_id in list(course_bag.keys()):
        course_bag[course_id] = [booked_time]
    else:
        course_bag[course_id].append(booked_time)   
    request.session['course_bag'] = course_bag
    return redirect(reverse('paygreenfee'))


# @login_required
def book_tee_time(request):
    """ A view to book a tee time """

    course_id = request.POST.get('course')
    course = get_object_or_404(Course, pk=course_id)
    booked_time = request.POST.get('tee_time')
    booking_exist = TeeTime.objects.filter(course=course_id,
                                           tee_time=booked_time).exists()
    course_bag = request.session.get('course_bag', {})

    if booking_exist:
        messages.error(request, "Tee time is already booked")
        return redirect(reverse('courses'))

    tee_time_form = TeeTimeForm(request.POST)

    if tee_time_form.is_valid():
        booked_tee_time = tee_time_form.save(commit=False)
        booked_tee_time.booked = True
        p = get_object_or_404(UserProfile, user=request.user)
        booked_tee_time.player_id = p.id
        booked_tee_time.save()

        return render(request, 'paygreenfee/paygreenfee.html',
                      {'tee_time_form': tee_time_form,
                       'course': course})
