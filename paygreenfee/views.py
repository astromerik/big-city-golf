from django.shortcuts import render, get_object_or_404, redirect, HttpResponse, reverse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings

# from paygreenfee.contexts import course_bookings
from .forms import PurchaseForm
from courses.models import TeeTime, Course
from golfprofile.models import UserProfile
from .models import PaymentInfo, TeeTimePurchase

import stripe
import json
# Create your views here.


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'course_bag': json.dumps(request.session.get('course_bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, ('Sorry, your payment cannot be '
                                 'processed right now. Please try '
                                 'again later.'))
        return HttpResponse(content=e, status=400)


@login_required
def paygreenfee(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    current_user = get_object_or_404(UserProfile, user=request.user)
    tee_times = TeeTime.objects.filter(player=current_user)
    purchase_form = PurchaseForm()


    if request.method == 'POST':
        course_bag = request.session.get('course_bag', {})

        form_data = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
        }

        purchase_form = PurchaseForm(form_data)
        if purchase_form.is_valid():
            # 1. check whether booking_exists
            # 2. if not, create TeeTime, attached to the course_id
            # 3. create the TeeTimePurchase (linked to the course_id and the TeeTime)
            # 4. Attach the TeeTimePurchase to the PaymentInfo instance
            purchase = purchase_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            purchase.stripe_pid = pid
            purchase.original_teetime = json.dumps(course_bag)
            purchase.save()
            for course_id, course_data in course_bag.items():
                try:
                    course = Course.objects.get(id=course_id)
                    if isinstance(course_data, int):
                        tee_time_purchase = TeeTimePurchase(
                            tee_time=tee_time,
                            course=course,
                            quantity=course_data,
                        )
                        tee_time_purchase.save()
                    else:
                        return redirect(reverse('courses'))
                except Course.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your bag wasn't "
                        "found in our database. "
                        "Please call us for assistance!")
                    )
                    purchase.delete()
                    return redirect(reverse('home'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('golfprofile',
                                    args=[purchase.order_number]))

        else:
            messages.error(request, ('We could not save your purchase correctly, please double check your form'))
    else:
        course_bag = request.session.get('course_bag', {})
        if not course_bag:
            messages.error(request, ('You have no tee times booked....'))

        
        # course_bag = course_contents(request)
        # total = 

    template = 'paygreenfee/paygreenfee.html'

    context = {
        'purchase_form': purchase_form,
        'tee_times': tee_times,
        'stripe_public_key': stripe_public_key,
        'client_secret': 'test client secret',
    }

    return render(request, template, context)


@login_required
def delete_tee_time(request, tee_time_id):
    """ Delete the booked tee time """
    tee_time = TeeTime.objects.get(pk=tee_time_id)
    tee_time.delete()

    return redirect('paygreenfee')
