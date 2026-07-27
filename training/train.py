import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import torch
import evaluate
from transformers import DistilBertTokenizer

from torch.utils.data import Dataset

from transformers import DistilBertForSequenceClassification

from transformers import TrainingArguments

# Load dataset
df = pd.read_csv("dataset.csv")

# Keep only required columns
df = df[["statement", "status"]]

# Remove rows with missing values
df = df.dropna()

# Remove duplicate statements
df = df.drop_duplicates()

# Reset index
df = df.reset_index(drop=True)

print("Dataset Shape:", df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nLabel Counts:")
print(df["status"].value_counts())

print("\nFirst 5 Rows:")
print(df.head())



label_encoder = LabelEncoder()

df["label"] = label_encoder.fit_transform(df["status"])

print("\nLabel Mapping:")

for label, number in zip(label_encoder.classes_,
                         label_encoder.transform(label_encoder.classes_)):
    print(f"{label} -> {number}")
    
    
joblib.dump(label_encoder, "label_encoder.pkl")

train_texts, test_texts, train_labels, test_labels = train_test_split(
    df["statement"].tolist(),
    df["label"].tolist(),
    test_size=0.2,
    random_state=42,
    stratify=df["label"]
)

print("\nTraining Samples:", len(train_texts))
print("Testing Samples:", len(test_texts))


# Load tokenizer
tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-uncased")

# Tokenize training data
train_encodings = tokenizer(
    train_texts,
    truncation=True,
    padding=True,
    max_length=128
)

# Tokenize testing data
test_encodings = tokenizer(
    test_texts,
    truncation=True,
    padding=True,
    max_length=128
)

print("\nTokenization Complete!")

print("Training Samples:", len(train_encodings["input_ids"]))
print("Testing Samples:", len(test_encodings["input_ids"]))

print("\nLength of first tokenized sample:")
print(len(train_encodings["input_ids"][0]))


class MentalHealthDataset(Dataset):

    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, idx):
        item = {
            key: torch.tensor(val[idx])
            for key, val in self.encodings.items()
        }

        item["labels"] = torch.tensor(self.labels[idx])

        return item

# Create datasets
train_dataset = MentalHealthDataset(
    train_encodings,
    train_labels
)

test_dataset = MentalHealthDataset(
    test_encodings,
    test_labels
)

print("\nPyTorch Dataset Created!")
print("Training Dataset Size:", len(train_dataset))
print("Testing Dataset Size:", len(test_dataset))


# Load model
model = DistilBertForSequenceClassification.from_pretrained(
    "distilbert-base-uncased",
    num_labels=7
)


# Check whether GPU is available
device = torch.device(
    "cuda" if torch.cuda.is_available()
    else "cpu"
)

print("\nUsing device:", device)

if torch.cuda.is_available():
    print(f"GPU Name: {torch.cuda.get_device_name(0)}")
    print(f"GPU Count: {torch.cuda.device_count()}")


# Move model to GPU/CPU
model.to(device)

print("\nModel Loaded Successfully!")


# Training configuration
training_args = TrainingArguments(
    output_dir="./results",

    eval_strategy="epoch",

    save_strategy="epoch",
    
    save_total_limit=1,

    learning_rate=2e-5,

    per_device_train_batch_size=16,

    per_device_eval_batch_size=16,

    num_train_epochs=3,

    weight_decay=0.01,

    logging_dir="./logs",

    logging_steps=100,

    load_best_model_at_end=True,

    metric_for_best_model="accuracy",
    
    fp16=True,

    report_to="none"
)


accuracy = evaluate.load("accuracy")

def compute_metrics(eval_pred):
    predictions, labels = eval_pred

    predictions = predictions.argmax(axis=1)

    return accuracy.compute(
        predictions=predictions,
        references=labels
    )
    
from transformers import Trainer

trainer = Trainer(
    model=model,

    args=training_args,

    train_dataset=train_dataset,

    eval_dataset=test_dataset,

    compute_metrics=compute_metrics,
)


print("\nStarting Training...\n")

trainer.train()


model.save_pretrained("emotion_model")

tokenizer.save_pretrained("emotion_model")

print("\nModel Saved Successfully!")

