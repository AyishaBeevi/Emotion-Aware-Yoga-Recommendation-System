from transformers import DistilBertForSequenceClassification, DistilBertTokenizer

checkpoint = "results/checkpoint-7665"

model = DistilBertForSequenceClassification.from_pretrained(checkpoint)
tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-uncased")

model.save_pretrained("emotion_model")
tokenizer.save_pretrained("emotion_model")

print("Model saved successfully!")