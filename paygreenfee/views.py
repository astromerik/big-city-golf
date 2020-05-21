from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings

# from paygreenfee.contexts import course_bookings
from .forms import PaymentInfoForm
from courses.models import TeeTime, Course
from golfprofile.models import UserProfile
from .models import TeeTimePurchase

import stripe
import json
# Create your views here.


@login_required
def paygreenfee(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    course_bag = request.session.get('course_bag', {})
    bag = {k: [get_object_or_404(TeeTime, pk=_id) for _id in v] for k, v in course_bag.items()}
    payment_form = PaymentInfoForm()

    green_fee_grand_total = 0
    for course, teetimelist in bag.items():
        for teetime in teetimelist:
            green_fee_grand_total += teetime.course.green_fee

    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
                    amount=green_fee_grand_total,
                    currency=settings.STRIPE_CURRENCY,
                    )

    if request.method == 'POST':
        form_data = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
        }

        payment_form = PaymentInfoForm(form_data)
        if payment_form.is_valid():

            payment = payment_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            payment.stripe_pid = pid
            payment.original_teetime = json.dumps(course_bag)
            payment.total_greenfee = green_fee_grand_total
            payment.save()

            for course_id, teetimes in course_bag.items():
                course = get_object_or_404(Course, pk=course_id)
                for teetime_id in teetimes:
                    teetime = get_object_or_404(TeeTime, pk=teetime_id)
                    teetime.booked = True
                    teetime.save()
                    tee_time_purchase = TeeTimePurchase(
                        payment_info=payment,
                        tee_time=teetime,
                        course=course,
                        greenfee=course.green_fee,
                    )
                    tee_time_purchase.save()

            if 'course_bag' in request.session:
                del request.session['course_bag']
                messages.success(request, f'Your tee time '
                                 'is now booked. '
                                 'Good luck on the course!')
                return redirect(reverse('golfprofile'))

        else:
            messages.error(request,
                           "Yor form was not filled in correctly,"
                           " please try again.")
            return redirect(reverse('courses'))

    else:

        course_bag = request.session.get('course_bag', {})
        if not course_bag:
            messages.error(request, ('You have no tee times booked....'))

    template = 'paygreenfee/paygreenfee.html'

    context = {
        'payment_form': payment_form,
        'total': green_fee_grand_total,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
        'bag': bag,
    }

    return render(request, template, context)


def remove_tee_time_from_bag(request, teetime_id):
    print("We are here")
    course_bag = request.session.get('course_bag', {})
    print(course_bag)
    teetime = get_object_or_404(TeeTime, pk=teetime_id)
    print(teetime)
    course_id = str(teetime.course.id)
    print(course_id)

    if course_id in course_bag.keys():
        print("I'm there")
        if teetime.id in course_bag[course_id]:
            course_bag[course_id].remove(teetime.id)
            request.session['course_bag'] = course_bag
    print(course_bag)
    return redirect(reverse('paygreenfee'))
