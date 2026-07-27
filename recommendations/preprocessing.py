import re

# Dictionary of symptoms and their keywords
SYMPTOM_KEYWORDS = {
    "Back Pain": [
        "back pain",
        "back hurts",
        "backache",
        "lower back pain",
        "pain in my back",
        "aching back",
        "sore back"
    ],

    "Back Tightness": [
        "tight back",
        "back feels tight",
        "back stiffness",
        "stiff back",
        "tight lower back",
        "back is stiff"
    ],

    "Back Stiffness": [
        "back stiffness",
        "stiff back",
        "back feels stiff",
        "cannot bend my back",
        "hard to move my back"
    ],

    "Neck Stiffness": [
        "stiff neck",
        "neck is stiff",
        "neck feels tight",
        "cannot move my neck",
        "tight neck"
    ],

    "Fatigue": [
        "fatigue",
        "tired",
        "very tired",
        "exhausted",
        "weak",
        "low energy",
        "drained",
        "burned out",
        "no energy",
        "sleepy"
    ],

    "Headache": [
        "headache",
        "head hurts",
        "migraine",
        "pain in my head",
        "throbbing head"
    ],

    "Insomnia": [
        "cant sleep",
        "can't sleep",
        "cannot sleep",
        "insomnia",
        "sleepless",
        "awake all night",
        "not sleeping",
        "difficulty sleeping",
        "trouble sleeping"
    ],

    "Tension": [
        "tension",
        "tense",
        "body tension",
        "muscle tension",
        "feeling tense",
        "stressed muscles"
    ],

    "Poor Posture": [
        "poor posture",
        "bad posture",
        "slouching",
        "slouch",
        "rounded shoulders",
        "hunched back"
    ],

    "Poor Balance": [
        "poor balance",
        "bad balance",
        "lose balance",
        "unsteady",
        "wobbly",
        "difficulty balancing",
        "balance problem"
    ],

    "Swollen Legs": [
        "swollen legs",
        "leg swelling",
        "legs are swollen",
        "puffy legs",
        "leg edema",
        "swollen feet"
    ],

    "Mental Restlessness": [
        "restless",
        "can't relax",
        "mind won't stop",
        "overthinking",
        "racing thoughts",
        "mind racing",
        "mental restlessness",
        "can't focus",
        "mind is busy"
    ],

    "Tight Hamstrings": [
        "tight hamstrings",
        "hamstrings are tight",
        "back of my legs are tight",
        "hamstring pain",
        "tight back of legs"
    ],

    "Hip Tightness": [
        "tight hips",
        "hip tightness",
        "hips feel tight",
        "stiff hips",
        "hip stiffness"
    ],

    "Weak Legs": [
        "weak legs",
        "legs feel weak",
        "leg weakness",
        "my legs are weak",
        "can't stand long"
    ],

    "Shoulder Tightness": [
        "tight shoulders",
        "shoulder tightness",
        "stiff shoulders",
        "shoulders feel tight",
        "shoulder stiffness"
    ],

    "Weak Core": [
        "weak core",
        "core weakness",
        "weak abs",
        "poor core strength",
        "my core is weak",
        "weak stomach muscles"
    ],

    # Included because it's present in your data
    "Anxiety": [
        "anxious",
        "anxiety",
        "nervous",
        "worried",
        "panic",
        "uneasy",
        "restless",
        "fearful"
    ]
}

def clean_text(text):

    text = text.lower()

    # Remove apostrophes completely
    text = text.replace("'", "")

    # Remove remaining punctuation
    text = re.sub(r"[^a-zA-Z\s]", " ", text)

    # Remove extra spaces
    text = " ".join(text.split())

    return text

def extract_symptoms(text):
    """
    Extract physical and emotional symptoms
    from the user's journal.
    """

    cleaned = clean_text(text)

    detected = []

    for symptom, keywords in SYMPTOM_KEYWORDS.items():

        for keyword in keywords:

            if keyword.lower() in cleaned:

                detected.append(symptom)

                break

    return detected