import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from recommendations.engine import recommend_pose

emotion = "Stress"

symptoms = [
    "Back Pain",
    "Fatigue"
]

pose = recommend_pose(emotion, symptoms)

if pose:
    print("Recommended Pose")
    print("----------------")
    print("Name:", pose.name)
    print("Difficulty:", pose.difficulty)
    print("Duration:", pose.duration)
else:
    print("No pose found.")
    
