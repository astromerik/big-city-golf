from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
from .models import UserProfile
# Create your views here.


@login_required
def golfprofile(request):
    """ A view to render the users profile """

    return render(request, 'golfprofile/golfprofile.html')


def UserProfileUpdate(request):
    form = UserProfileForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request, "golfprofile/golfprofile.html", context)
