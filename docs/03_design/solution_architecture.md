# Solution Architecture

## Project: AI-Based Exam Anxiety Detector

---

## High-Level Architecture

```
┌─────────────────────────────────────────────────────┐
│                    USER (Browser)                   │
│          http://localhost:8501                      │
└─────────────────────┬───────────────────────────────┘
                      │ HTTPS
                      ▼
┌─────────────────────────────────────────────────────┐
│            STREAMLIT FRONTEND (Port 8501)           │
│  frontend/ui.py                                     │
│  ┌───────────────┐  ┌───────────────────────────┐  │
│  │  Text Input   │  │  Results Display Panel    │  │
│  │  (st.text_   │  │  - Color Indicator        │  │
│  │   area)       │  │  - Anxiety Level Label    │  │
│  └───────────────┘  │  - Confidence Score       │  │
│                     │  - Coping Tips            │  │
│                     └───────────────────────────┘  │
└─────────────────────┬───────────────────────────────┘
                      │ HTTP POST /predict
                      │ {"text": "..."}
                      ▼
┌─────────────────────────────────────────────────────┐
│             FASTAPI BACKEND (Port 8000)             │
│  backend/app.py                                     │
│  ┌───────────────┐  ┌───────────────────────────┐  │
│  │  POST /predict│  │  GET /health              │  │
│  │  - Validate   │  │  - Server health check    │  │
│  │  - Call model │  └───────────────────────────┘  │
│  │  - Return JSON│                                  │
│  └───────────────┘                                  │
│  backend/model.py                                   │
│  ┌─────────────────────────────────────────────┐   │
│  │  AnxietyModel (Singleton)                   │   │
│  │  - load_model() → loads from saved_model/   │   │
│  │  - predict(text) → returns label + score    │   │
│  └─────────────────────────────────────────────┘   │
└─────────────────────┬───────────────────────────────┘
                      │ Model Weights (in-memory)
                      ▼
┌─────────────────────────────────────────────────────┐
│        BERT MODEL (models/saved_model/)             │
│  Architecture: BertForSequenceClassification        │
│  Base: bert-base-uncased (110M parameters)          │
│  Fine-tuned on: 6,068 mental health statements      │
│  Labels: 0=Low, 1=Moderate, 2=High                 │
│  Files:                                             │
│  ├── model.safetensors (418 MB)                    │
│  ├── config.json                                    │
│  ├── tokenizer.json                                 │
│  └── tokenizer_config.json                          │
└─────────────────────────────────────────────────────┘
```

---

## Component Descriptions

### 1. Frontend (`frontend/ui.py`)
- **Framework:** Streamlit
- **Responsibilities:** Renders the UI, collects text input, sends API requests, displays results
- **Key features:** Color-coded anxiety display, emoji indicators, coping tips rendering

### 2. Backend API (`backend/app.py`)
- **Framework:** FastAPI + Uvicorn
- **Responsibilities:** Receives HTTP requests, validates input, routes to model, returns JSON
- **Endpoints:**
  - `POST /predict` → runs inference and returns label/confidence
  - `GET /health` → returns server status

### 3. Model Service (`backend/model.py`)
- **Class:** `AnxietyModel` (singleton pattern)
- **Responsibilities:** Loads model on startup, tokenizes input, runs BERT inference, maps output to labels

### 4. ML Model (`models/saved_model/`)
- **Architecture:** `BertForSequenceClassification`
- **Training:** Google Colab T4 GPU, 3-5 epochs, `AdamW` optimizer, lr=1e-5
- **Inference:** CPU-based for local deployment

---

## Data Flow

```
Student Text
     ↓
Streamlit UI (POST to FastAPI)
     ↓
FastAPI (validates request)
     ↓
AnxietyModel.predict(text)
     ↓
BertTokenizer (tokenizes text → 128 tokens)
     ↓
BertForSequenceClassification (forward pass)
     ↓
Softmax → Probabilities [P_low, P_mod, P_high]
     ↓
ArgMax → Predicted class + confidence
     ↓
JSON Response → Streamlit → Display to User
```

---

## Deployment Architecture (Local)

| Component | Port | Command |
|---|---|---|
| Streamlit Frontend | 8501 | `uvicorn app:app` inside `frontend/` |
| FastAPI Backend | 8000 | `streamlit run ui.py` inside `backend/` |
