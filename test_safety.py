import os
import django

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "config.settings"
)

django.setup()

from recommendations.safety import recommend_safe_pose

emotion = "Stress"

symptoms = [
    "Back Pain"
]

pose = recommend_safe_pose(
    emotion,
    symptoms
)

if pose:

    print("Recommended Safe Pose")

    print("---------------------")

    print(pose.name)

else:

    print("No safe pose found.")