from django.db import models


class YogaPose(models.Model):

    LEVEL_CHOICES = [
        ("Beginner", "Beginner"),
        ("Intermediate", "Intermediate"),
        ("Advanced", "Advanced"),
    ]

    name = models.CharField(max_length=100)

    sanskrit_name = models.CharField(max_length=100, blank=True)

    difficulty = models.CharField(
        max_length=20,
        choices=LEVEL_CHOICES
    )

    duration = models.PositiveIntegerField()

    description = models.TextField()

    benefits = models.TextField()

    contraindications = models.TextField(blank=True)

    instructions = models.TextField()

    image = models.ImageField(
        upload_to="yoga/",
        blank=True,
        null=True
    )

    # ---------- AI Fields ----------

    target_emotions = models.CharField(
    max_length=300,
    default="",
    help_text="Comma separated emotions"
)

    target_symptoms = models.CharField(
    max_length=300,
    default="",
    help_text="Comma separated symptoms"
)

    avoid_conditions = models.CharField(
        max_length=300,
        blank=True,
        help_text="Pregnancy,Knee Injury,etc"
    )

    difficulty_score = models.PositiveIntegerField(default=1)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name