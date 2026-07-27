from .engine import calculate_score
from recommendations.models import YogaPose


from .models import YogaPose


def is_pose_safe(pose, symptoms):
    """
    Returns:
        (True, "")                     -> Safe
        (False, warning_message)       -> Unsafe
    """

    if not pose:
        return False, "No yoga pose found."

    # Combine both fields
    restrictions = (
        pose.contraindications + "," + pose.avoid_conditions
    )

    restrictions = [
        item.strip().lower()
        for item in restrictions.split(",")
        if item.strip()
    ]

    for symptom in symptoms:

        if symptom.lower() in restrictions:

            return (
                False,
                f"{pose.name} is not recommended because of {symptom}."
            )

    return True, ""

def recommend_safe_pose(emotion, symptoms):
    """
    Returns the highest scoring SAFE yoga pose.
    """

    poses = YogaPose.objects.filter(is_active=True)

    ranked = []

    for pose in poses:

        score = calculate_score(
            pose,
            emotion,
            symptoms
        )

        ranked.append((score, pose))

    ranked.sort(reverse=True, key=lambda x: x[0])

    for score, pose in ranked:

        safe, warning = is_pose_safe(
            pose,
            symptoms
        )

        if safe:
            return pose

    return None