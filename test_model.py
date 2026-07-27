# from recommendations.predictor import predict_emotion

# tests = [
#     "I feel anxious because of exams.",
#     "Life is beautiful and I am happy.",
#     "I don't want to live anymore.",
#     "I feel stressed because of work.",
#     "Everything feels normal today."
# ]

# for text in tests:
#     emotion, confidence = predict_emotion(text)

#     print("-" * 50)
#     print("Input :", text)
#     print("Prediction :", emotion)
#     print("Confidence :", confidence)


import pandas as pd

df = pd.read_csv("training/dataset.csv")

# Look for exact phrase
print(df[df["statement"].str.contains(
    "don't want to live",
    case=False,
    na=False
)])

print("=" * 80)

print(df[df["statement"].str.contains(
    "suicide",
    case=False,
    na=False
)])

print("=" * 80)

print(df[df["statement"].str.contains(
    "kill myself",
    case=False,
    na=False
)])