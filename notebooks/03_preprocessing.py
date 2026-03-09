import pandas as pd
from sklearn.model_selection import train_test_split
from transformers import BertTokenizer
import os
import re

print("Loading Kaggle dataset (Combined Data.csv)...")
df_full = pd.read_csv('../data/Combined Data.csv')

# The dataset has columns: unique id, statement, status
# We only want rows with 'Normal', 'Stress', 'Anxiety'
valid_statuses = ['Normal', 'Stress', 'Anxiety']
df = df_full[df_full['status'].isin(valid_statuses)].copy()

print(f"Filtered {len(df)} relevant rows from {len(df_full)} total rows.")

# Map Kaggle status to our 3 anxiety levels for consistency with the app
# Normal -> 0 (Low Anxiety)
# Stress -> 1 (Moderate Anxiety)
# Anxiety -> 2 (High Anxiety)
label_mapping = {"Normal": 0, "Stress": 1, "Anxiety": 2}
df['label'] = df['status'].map(label_mapping)

print("Label distribution in filtered dataset:")
print(df['status'].value_counts())

# Downsample if too large, as original was 450, Colab training might take long if 50,000+ rows
# Let's take a balanced sample of 500 from each to make it 1500 total, which is good for Colab
sampled_df = pd.DataFrame()
for status in valid_statuses:
    subset = df[df['status'] == status]
    # take up to 1000 items per class
    sample_size = min(1000, len(subset))
    sampled_df = pd.concat([sampled_df, subset.sample(sample_size, random_state=42)])

df = sampled_df.sample(frac=1, random_state=42).reset_index(drop=True)
print(f"Final sampled dataset size: {len(df)}")

# 1. Clean Text Data
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

print("Cleaning text...")
df['clean_text'] = df['statement'].apply(clean_text)

# Tokenization using BERT Tokenizer
print("Loading BERT Tokenizer...")
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

sample_tokens = tokenizer(df['clean_text'].iloc[0], padding='max_length', truncation=True, max_length=128)
print("Sample tokens length:", len(sample_tokens['input_ids']))

# Split data
print("Splitting dataset...")
train_df, temp_df = train_test_split(df, test_size=0.3, random_state=42, stratify=df['label'])
val_df, test_df = train_test_split(temp_df, test_size=0.5, random_state=42, stratify=temp_df['label'])

print(f"Train size: {len(train_df)}")
print(f"Validation size: {len(val_df)}")
print(f"Test size: {len(test_df)}")

# Save splits
train_df.to_csv('../data/train.csv', index=False)
val_df.to_csv('../data/val.csv', index=False)
test_df.to_csv('../data/test.csv', index=False)
print("Saved train, val, and test splits to /data directory.")
