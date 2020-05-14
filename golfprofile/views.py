from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm, UserForm
from .models import UserProfile
from courses.models import TeeTime, Course

# Create your views here.


@login_required
def golfprofile(request):
    """ A view to render the users profile """

#    tee_times = TeeTime.objects.all()
    current_user = get_object_or_404(UserProfile, user = request.user)
    tee_times = TeeTime.objects.filter(player = current_user)

    # course = get_object_or_404(Course,)

    user = request.user
    user_form = UserForm(instance=user)

    profile = get_object_or_404(UserProfile, user=user)
    user_profile_form = UserProfileForm(instance=profile)

    if request.method == "POST":
        user_form = UserForm(request.POST, instance=user)
        user_profile_form = UserProfileForm(request.POST, instance=profile)

        if user_form.is_valid():
            user_form.save()

        if user_profile_form.is_valid():
            user_profile_form.save()

        # flash a message "Your info has been updated!"

    return render(request, "golfprofile/golfprofile.html",
                  {'user_form': user_form,
                   'user_profile_form': user_profile_form,
                   'tee_times': tee_times,
                   })


def delete_tee_time(request, tee_time_id):
    """ Delete the booked tee time """
    tee_time = get_object_or_404(TeeTime, pk=tee_time_id)
    tee_time.delete()

    return redirect(reverse('golfprofile'))

