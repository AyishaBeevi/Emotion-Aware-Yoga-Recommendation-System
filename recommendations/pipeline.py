from .predictor import predict_emotion
from .preprocessing import extract_symptoms
from .safety import recommend_safe_pose
from .explain import generate_explanation


def analyze_journal(text):
    """
    Complete AI pipeline.
    """

    # Step 1: Mental health prediction
    emotion, confidence = predict_emotion(text)

    # Step 2: Symptom extraction
    symptoms = extract_symptoms(text)

    # Step 3: Safe yoga recommendation
    pose = recommend_safe_pose(
        emotion,
        symptoms
    )

    # Step 4: Explanation
    explanation = generate_explanation(
        emotion,
        confidence,
        symptoms,
        pose
    )

    return {
        "emotion": emotion,
        "confidence": confidence,
        "symptoms": symptoms,
        "pose": pose,
        "explanation": explanation,
    }