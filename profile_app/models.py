from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):

    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    ]

    LEVEL_CHOICES = [
        ("Beginner", "Beginner"),
        ("Intermediate", "Intermediate"),
        ("Advanced", "Advanced"),
    ]

    TIME_CHOICES = [
        ("Morning", "Morning"),
        ("Afternoon", "Afternoon"),
        ("Evening", "Evening"),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    age = models.PositiveIntegerField(null=True, blank=True)

    gender = models.CharField(
        max_length=20,
        choices=GENDER_CHOICES,
        blank=True
    )

    height = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True
    )

    weight = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True
    )

    medical_conditions = models.TextField(blank=True)

    injuries = models.TextField(blank=True)

    is_pregnant = models.BooleanField(default=False)

    yoga_level = models.CharField(
        max_length=20,
        choices=LEVEL_CHOICES,
        default="Beginner"
    )

    preferred_time = models.CharField(
        max_length=20,
        choices=TIME_CHOICES,
        default="Morning"
    )

    stress_relief = models.BooleanField(default=False)

    flexibility = models.BooleanField(default=False)

    better_sleep = models.BooleanField(default=False)

    back_pain_relief = models.BooleanField(default=False)

    weight_loss = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username