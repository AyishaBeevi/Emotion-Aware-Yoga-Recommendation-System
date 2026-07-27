from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import UserProfileForm


@login_required
def profile(request):

    profile, created = UserProfile.objects.get_or_create(
        user=request.user
    )

    if request.method == "POST":

        form = UserProfileForm(
            request.POST,
            instance=profile
        )

        if form.is_valid():

            form.save()

            return redirect("profile")

    else:

        form = UserProfileForm(
            instance=profile
        )

    bmi = None
    bmi_category = None

    if profile.height and profile.weight:

        height_m = profile.height / 100

        bmi = round(profile.weight / (height_m ** 2), 1)

        if bmi < 18.5:
            bmi_category = "Underweight"

        elif bmi < 25:
            bmi_category = "Normal"

        elif bmi < 30:
            bmi_category = "Overweight"

        else:
            bmi_category = "Obese"

    return render(
        request,
        "profile.html",
        {
            "form": form,
            "bmi": bmi,
            "bmi_category": bmi_category,
        }
    )