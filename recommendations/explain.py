def generate_explanation(emotion, confidence, symptoms, pose):
    """
    Generate a human-friendly AI explanation.
    """

    explanation = []

    explanation.append(
        f"The AI model detected {emotion} with a confidence of {confidence:.2f}%."
    )

    if symptoms:
        explanation.append(
            "The following physical symptoms were identified: "
            + ", ".join(symptoms) + "."
        )
    else:
        explanation.append(
            "No physical symptoms were detected from the journal."
        )

    explanation.append(
        f"{pose.name} was selected because it matches the detected mental state and physical symptoms."
    )

    explanation.append(
        f"It is a {pose.difficulty.lower()} level pose and is recommended for about {pose.duration} minutes."
    )

    benefits = [
        b.strip()
        for b in pose.benefits.split(",")
        if b.strip()
    ]

    if benefits:
        explanation.append(
            "Expected benefits include:"
        )

        for benefit in benefits:
            explanation.append(f"✔ {benefit}")

    explanation.append(
        "This recommendation is AI-assisted and should not replace professional medical advice."
    )

    return explanation