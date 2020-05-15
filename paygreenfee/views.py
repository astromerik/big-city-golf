from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from courses.models import TeeTime
from golfprofile.models import UserProfile
# Create your views here.


@login_required
def paygreenfee(request):
    """ A view to render the users profile """

    current_user = get_object_or_404(UserProfile, user=request.user)
    tee_times = TeeTime.objects.filter(player=current_user)

    return render(request, "paygreenfee/paygreenfee.html",
                  {'tee_times': tee_times
                   })


@login_required
def delete_tee_time(request, tee_time_id):
    """ Delete the booked tee time """
    tee_time = TeeTime.objects.get(pk=tee_time_id)
    tee_time.delete()

    return redirect('paygreenfee')
