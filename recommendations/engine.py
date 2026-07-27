from .models import YogaPose


def calculate_score(pose, emotion, symptoms):
    """
    Calculates a score for a yoga pose.
    Higher score = better recommendation.
    """

    score = 0

    # ----------------------------
    # Emotion Matching
    # ----------------------------

    target_emotions = [
        item.strip().lower()
        for item in pose.target_emotions.split(",")
        if item.strip()
    ]

    if emotion.lower() in target_emotions:
        score += 50

    # ----------------------------
    # Symptom Matching
    # ----------------------------

    target_symptoms = [
        item.strip().lower()
        for item in pose.target_symptoms.split(",")
        if item.strip()
    ]

    for symptom in symptoms:

        if symptom.lower() in target_symptoms:
            score += 20

    # ----------------------------
    # Difficulty Bonus
    # ----------------------------

    if pose.difficulty == "Beginner":
        score += 10

    # ----------------------------
    # Short Duration Bonus
    # ----------------------------

    if pose.duration <= 10:
        score += 5

    return score


def recommend_pose(emotion, symptoms):
    """
    Returns the best yoga pose.
    """

    poses = YogaPose.objects.filter(is_active=True)

    best_pose = None
    best_score = -1

    for pose in poses:

        score = calculate_score(
            pose,
            emotion,
            symptoms
        )

        if score > best_score:
            best_score = score
            best_pose = pose

    return best_pose