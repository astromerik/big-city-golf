from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from courses.models import TeeTime
from golfprofile.models import UserProfile
from paygreenfee.contexts import greenfee_contents
from .forms import PurchaseForm

from .models import PaymentInfo, TeeTimePurchase
import stripe
# Create your views here.


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, ('Sorry, your payment cannot be '
                                 'processed right now. Please try '
                                 'again later.'))
        return HttpResponse(content=e, status=400)

@login_required
def paygreenfee(request):
    """ A view to render the users profile """

    current_user = get_object_or_404(UserProfile, user=request.user)
    tee_times = TeeTime.objects.filter(player=current_user)
    purchase_form = PurchaseForm()
    template = 'paygreenfee/paygreenfee.html'

    context = {
        'purchase_form': purchase_form,
        'tee_times': tee_times,
        'stripe_public_key': 'pk_test_QZvzChOy9KYagi3I7AEOK5qO00bbrZcJ88',
        'client_secret': 'test client secret'
    }

    return render(request, template, context)


@login_required
def delete_tee_time(request, tee_time_id):
    """ Delete the booked tee time """
    tee_time = TeeTime.objects.get(pk=tee_time_id)
    tee_time.delete()

    return redirect('paygreenfee')
