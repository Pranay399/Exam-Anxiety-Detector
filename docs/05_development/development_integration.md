# Development & Integration Documentation

## Project: AI-Based Exam Anxiety Detector

---

## 1. Data Collection & Preparation

### Data Source
- **Dataset:** "Sentiment Analysis for Mental Health" — Kaggle
- **File:** `data/Combined Data.csv`
- **Size:** ~94,000 records

### Columns Used
| Column | Description |
|---|---|
| `statement` | Free-form text written by users |
| `status` | Label (Normal, Stress, Anxiety, Depression, etc.) |

### Label Mapping
| Original Label | Mapped To | Encoded As |
|---|---|---|
| Normal | Low Anxiety | 0 |
| Stress | Moderate Anxiety | 1 |
| Anxiety | High Anxiety | 2 |

### Data Cleaning (03_preprocessing.py)
- Filter only rows with `status` ∈ {Normal, Stress, Anxiety}
- Lowercase all text
- Remove special characters via regex: `[^a-zA-Z0-9\s]`
- Strip extra whitespace
- Balance classes: 3,000 samples per label = 9,000 total
- Split: 70% Train / 15% Validation / 15% Test

### Data Privacy Considerations
- Data is publicly available on Kaggle (anonymized)
- No Personally Identifiable Information (PII) in the dataset
- Training data is not stored or transmitted in production

---

## 2. Model Selection & Architecture

### Model Chosen: bert-base-uncased
- **Architecture:** BertForSequenceClassification
- **Parameters:** 110M
- **Tokenizer:** BertTokenizer (WordPiece, 30,522 vocab)
- **Max sequence length:** 128 tokens
- **Output:** 3 logits → Softmax → Label

### Why BERT?
- Pre-trained on 3.3B words (BookCorpus + English Wikipedia)
- Bidirectional context understanding (better than RNNs/LSTMs)
- Fine-tuning requires only a classification head on top
- Excellent community support and documentation

### Training Configuration
| Hyperparameter | Value |
|---|---|
| Epochs | 3–5 |
| Batch size | 16–32 |
| Learning rate | 1e-5 |
| Warmup steps | 10% of total |
| Optimizer | AdamW (weight_decay=0.01) |
| Gradient clipping | 1.0 |
| Device | CUDA (Colab T4 GPU) |

---

## 3. Prompt Engineering & System Instructions

*(Not applicable — this system uses fine-tuned BERT classification, not prompt-based LLMs like Gemini or GPT)*

For reference, if the system were extended to use Gemini:
- System role: "You are a mental wellness classifier. Analyze the following student journal entry and classify it as Low, Moderate, or High Anxiety."
- Output format: structured JSON `{label, confidence, rationale}`

---

## 4. Development & Integration

### Frontend (`frontend/ui.py`)
```python
# Core Streamlit UI pattern
import streamlit as st
import requests

text = st.text_area("Describe how you feel...")
if st.button("Analyse"):
    response = requests.post("http://localhost:8000/predict", json={"text": text})
    result = response.json()
    # Display result with color and tips
```

### Backend (`backend/app.py`)
```python
from fastapi import FastAPI
from pydantic import BaseModel
from model import anxiety_model

app = FastAPI()

class TextInput(BaseModel):
    text: str

@app.post("/predict")
def predict(input: TextInput):
    return anxiety_model.predict(input.text)
```

### Model Inference (`backend/model.py`)
```python
# Key inference logic
encoding = self.tokenizer(
    text, max_length=128, padding='max_length',
    truncation=True, return_tensors='pt'
)
with torch.no_grad():
    outputs = self.model(**encoding)
    probs = softmax(outputs.logits, dim=1)
    label_id = probs.argmax().item()
```

### Error Handling
- FastAPI global exception handler for 500 errors
- Model loading fallback to base `bert-base-uncased` if saved model not found
- Frontend shows clean error message if API is unreachable

### API Key Security
- No external API keys used in v1
- CORS policy restricts origin in production deployment

---

## 5. Testing & Evaluation

### Functional Testing Results

| Test | Input | Expected | Actual | Pass? |
|---|---|---|---|---|
| Low anxiety detection | "I feel calm and ready for my exam." | Low | Low | ✅ |
| High anxiety detection | "I'm terrified, I haven't slept and I'm going to fail." | High | High | ✅ |
| Moderate anxiety detection | "A bit nervous but I think I'll manage." | Moderate | Moderate | ✅ |
| Empty input | "" | Error/warning | Warning shown | ✅ |
| Long text (>512 words) | 600 word essay | Truncated + result | Truncated OK | ✅ |
| Health check | GET /health | {"status": "healthy"} | {"status": "healthy"} | ✅ |

### Model Evaluation Metrics (Test Set)

| Class | Precision | Recall | F1-Score |
|---|---|---|---|
| Low Anxiety | 0.78 | 0.80 | 0.79 |
| Moderate Anxiety | 0.72 | 0.69 | 0.70 |
| High Anxiety | 0.81 | 0.83 | 0.82 |
| **Weighted Avg** | **0.77** | **0.77** | **0.77** |

### Performance Testing
| Metric | Result |
|---|---|
| Inference time (CPU) | ~1.2–2.0 seconds |
| Inference time (GPU) | ~0.3 seconds |
| API response time (local) | <3 seconds |
| Concurrent requests supported | 10+ |
