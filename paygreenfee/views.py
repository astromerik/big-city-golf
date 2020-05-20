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
    payment_form = PaymentInfoForm()
    green_fee_grand_total = sum(
                        [entry[0][1] for entry in list(course_bag.values())])
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

            for course_id, course_data in course_bag.items():
                player = get_object_or_404(UserProfile, user=request.user)
                course = get_object_or_404(Course, pk=course_id)
                for booked_time in course_data:
                    booked_time_string = booked_time[0]
                    booked_time_green_fee = booked_time[1]
                    tee_time = TeeTime.objects.create(
                        tee_time=booked_time_string,
                        price=booked_time_green_fee,
                        course=course,
                        player=player,
                        booked=True
                    )
                    tee_time.save()

                    create_tee_time_purchase = TeeTimePurchase(
                        payment_info=payment,
                        tee_time=tee_time,
                        course=course,
                        player=player,
                        total_greenfee=booked_time_green_fee,
                    )
                    create_tee_time_purchase.save()

            if 'course_bag' in request.session:
                del request.session['course_bag']
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
        'course_bag': course_bag,
    }

    return render(request, template, context)


def remove_tee_time_from_bag(request, course_id):
    course_bag = request.session.get('course_bag', {})
    course_bag.pop(course_id)

    request.session['course_bag'] = course_bag
    return render(reverse('courses'))
