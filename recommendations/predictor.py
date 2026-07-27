import os
import joblib
import torch

from transformers import (
    DistilBertTokenizer,
    DistilBertForSequenceClassification
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "ai", "emotion_model")
ENCODER_PATH = os.path.join(BASE_DIR, "ai", "label_encoder.pkl")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

print(f"Loading AI model on {device}...")

tokenizer = DistilBertTokenizer.from_pretrained(MODEL_PATH)

model = DistilBertForSequenceClassification.from_pretrained(MODEL_PATH)

model.to(device)
model.eval()

label_encoder = joblib.load(ENCODER_PATH)

print("AI model loaded successfully.")


def predict_emotion(text):

    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=128
    )

    inputs = {k: v.to(device) for k, v in inputs.items()}

    with torch.no_grad():
        outputs = model(**inputs)

    probabilities = torch.softmax(outputs.logits, dim=1)

    confidence, prediction = torch.max(probabilities, dim=1)

    emotion = label_encoder.inverse_transform(
        [prediction.item()]
    )[0]

    return emotion, round(confidence.item() * 100, 2)