from recommendations.preprocessing import extract_symptoms

tests = [
    "My back hurts and I am very tired.",
    "I have a headache and neck pain.",
    "I can't sleep because I am stressed.",
    "Everything feels normal today."
]



print(extract_symptoms("I can't sleep because I am stressed."))

for text in tests:
    print("-" * 50)
    print(text)
    print(extract_symptoms(text))