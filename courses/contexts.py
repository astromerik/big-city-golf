from django.shortcuts import get_object_or_404
from courses.models import Course


def course_bookings(request):

    course_courses = []
    total = 0
    course_count = 0
    course_bag = request.session.get('course_bag', {})

    for course_id, course_data in course_bag.items():
        if isinstance(course_data, int):
            course = get_object_or_404(Course, pk=course_id)
            total += course.green_fee
            course_count += course_data
            course_courses.append({
                'course_id': course_id,
                'course_data': course_data,
                'course': course,
            })

    context = {
        'course_courses': course_courses,
        'total': total,
        'course_count': course_count,
        'course_bag': course_bag,
    }

    return context
