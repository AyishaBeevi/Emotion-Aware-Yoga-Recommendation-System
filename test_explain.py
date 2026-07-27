import os
import django

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "config.settings"
)

django.setup()

from recommendations.models import YogaPose
from recommendations.explain import generate_explanation

pose = YogaPose.objects.first()

result = generate_explanation(
    "Stress",
    ["Back Pain", "Fatigue"],
    pose
)

for line in result:
    print(line)