from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from journal.models import JournalEntry

from .pipeline import analyze_journal

from django.shortcuts import get_object_or_404


from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from journal.models import JournalEntry
from .pipeline import analyze_journal


EMOJI_MAP = {
    "Normal": "😊",
    "Anxiety": "😟",
    "Stress": "😫",
    "Depression": "😔",
    "Bipolar": "😵",
    "Personality disorder": "💭",
    "Suicidal": "🆘",
}


@login_required
def dashboard(request):

    journals = (
        JournalEntry.objects
        .filter(user=request.user)
        .order_by("-created_at")
    )

    latest = journals.first()

    result = None

    emotion = None
    confidence = None
    symptoms = []
    pose = None
    emoji = "🧘"

    if latest:

        result = analyze_journal(latest.text)

        emotion = result["emotion"]

        confidence = result["confidence"]

        symptoms = result["symptoms"]

        pose = result["pose"]

        emoji = EMOJI_MAP.get(emotion, "🧘")

    context = {

        "journals": journals[:5],

        "journal_count": journals.count(),

        "latest": latest,

        "result": result,

        "emotion": emotion,

        "confidence": confidence,

        "symptoms": symptoms,

        "pose": pose,

        "emoji": emoji,

    }

    return render(
        request,
        "dashboard.html",
        context
    )



from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from journal.models import JournalEntry

EMOJI = {
    "Normal": "😊",
    "Stress": "😣",
    "Anxiety": "😟",
    "Depression": "😔",
    "Bipolar": "🎭",
    "Suicidal": "⚠️",
    "Personality disorder": "🧠",
}


@login_required
def analysis(request):

    journal = (
        JournalEntry.objects
        .filter(user=request.user)
        .order_by("-created_at")
        .first()
    )

    emotion = None
    confidence = 0
    symptoms = []
    emoji = "🤖"

    if journal:

        emotion = journal.predicted_emotion
        confidence = journal.confidence

        emoji = EMOJI.get(emotion, "🙂")

        if journal.physical_symptoms:
            symptoms = [
                s.strip()
                for s in journal.physical_symptoms.split(",")
                if s.strip()
            ]

    context = {
        "journal": journal,
        "emotion": emotion,
        "confidence": confidence,
        "symptoms": symptoms,
        "emoji": emoji,
    }

    return render(
        request,
        "analysis.html",
        context,
    )
@login_required
def recommendation(request):

    journal = (
        JournalEntry.objects
        .filter(user=request.user)
        .order_by("-created_at")
        .first()
    )

    if not journal:
        return render(
            request,
            "recommendation.html",
            {
                "error": "No journal entry found."
            }
        )

    result = analyze_journal(journal.text)

    return render(
        request,
        "includes/dashboard/recommendation.html",
        {
            "journal": journal,
            "result": result,
        }
    )
    # Run the AI pipeline
    result = analyze_journal(latest.content)

    context = {
        "journal": latest,
        "result": result
    }

    return render(
        request,
        "recommendation.html",
        context
    )


@login_required
def history(request):

    journals = JournalEntry.objects.filter(
        user=request.user
    ).order_by("-created_at")

    return render(
        request,
        "history.html",
        {
            "journals": journals
        }
    )