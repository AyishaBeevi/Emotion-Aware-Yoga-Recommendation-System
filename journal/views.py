from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import JournalEntry

from .models import JournalEntry
from recommendations.predictor import predict_emotion
from recommendations.preprocessing import extract_symptoms

@login_required
def journal(request):

    if request.method == "POST":

        text = request.POST.get("journal")

        emotion, confidence = predict_emotion(text)

        symptoms = extract_symptoms(text)

        JournalEntry.objects.create(
            user=request.user,
            text=text,
            predicted_emotion=emotion,
            confidence=confidence,
            physical_symptoms=",".join(symptoms)
        )

        return redirect("analysis")

    journals = JournalEntry.objects.filter(
        user=request.user
    ).order_by("-created_at")

    return render(
        request,
        "journal.html",
        {
            "journals": journals
        }
    )