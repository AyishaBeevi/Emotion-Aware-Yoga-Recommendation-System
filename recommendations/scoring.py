def calculate_score(
    pose,
    emotion,
    symptoms
):

    score = 0

    emotions = [
        item.strip().lower()
        for item in pose.target_emotions.split(",")
    ]

    if emotion.lower() in emotions:
        score += 5

    pose_symptoms = [
        item.strip().lower()
        for item in pose.target_symptoms.split(",")
    ]

    for symptom in symptoms:

        if symptom.lower() in pose_symptoms:
            score += 3

    return score

def find_best_pose(
        poses,
        emotion,
        symptoms
):

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