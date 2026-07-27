import os
import django

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "config.settings"
)

django.setup()

from recommendations.pipeline import analyze_journal

journal = """
I feel stressed because of exams.
My back hurts and I am very tired.
"""

result = analyze_journal(journal)

print("\nDetected Emotion")
print(result["emotion"])

print("\nConfidence")
print(result["confidence"])

print("\nSymptoms")
print(result["symptoms"])

print("\nRecommended Pose")
print(result["pose"].name)

print("\nExplanation")
for line in result["explanation"]:
    print(line)