# from django.db import models
# from django.contrib.auth.models import User


# class JournalEntry(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     text = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.user.username} - {self.created_at.strftime('%d/%m/%Y')}"


from django.db import models
from django.contrib.auth.models import User


class JournalEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    text = models.TextField()

    predicted_emotion = models.CharField(
        max_length=50,
        blank=True
    )

    confidence = models.FloatField(
        default=0
    )

    physical_symptoms = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.user.username} - {self.created_at:%d/%m/%Y}"