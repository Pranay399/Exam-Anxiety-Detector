# Data Flow Diagrams & User Stories

## Project: AI-Based Exam Anxiety Detector

---

## User Stories

### Epic: Anxiety Detection for Students

| ID | User Story | Priority | Status |
|---|---|---|---|
| US-01 | As a **student**, I want to type how I feel before an exam so that the AI can tell me my anxiety level. | High | ✅ Done |
| US-02 | As a **student**, I want to see a color-coded result (Green/Yellow/Red) so I instantly understand my anxiety level. | High | ✅ Done |
| US-03 | As a **student**, I want to receive personalized coping tips so I know what to do next. | High | ✅ Done |
| US-04 | As a **student**, I want the system to understand my anxiety without me having to fill in a form. | High | ✅ Done |
| US-05 | As a **counselor**, I want to see aggregated anxiety trends across the student body. | Low | 🔜 Future |
| US-06 | As a **student**, I want to track my anxiety levels over time. | Low | 🔜 Future |
| US-07 | As a **developer**, I want a health check endpoint so I can verify the API server is running. | Medium | ✅ Done |

---

## Acceptance Criteria for US-01

```
GIVEN I am a student on the Exam Anxiety Detector page
WHEN I type my thoughts into the text box
AND I click the "Analyse My Anxiety" button
THEN the system SHOULD display a prediction within 3 seconds
AND the prediction SHOULD be one of: Low Anxiety, Moderate Anxiety, High Anxiety
AND the prediction SHOULD include a colour indicator (Green/Yellow/Red)
```

---

## Level 0 Data Flow Diagram (Context Diagram)

```
               ┌─────────────────┐
               │    STUDENT      │
               │   (User)        │
               └────────┬────────┘
                        │ Text Input
                        ▼
              ┌─────────────────────┐
              │                     │
              │   EXAM ANXIETY      │
              │   DETECTION SYSTEM  │
              │                     │
              └─────────────────────┘
                        │
                        ▼
               ┌─────────────────┐
               │  ANXIETY RESULT │
               │  + COPING TIPS  │
               └─────────────────┘
```

---

## Level 1 Data Flow Diagram

```
STUDENT
   │
   │ 1. Enters text
   ▼
┌────────────────────────────┐
│     Streamlit Frontend     │
│     (ui.py : 8501)         │
│  - Text input field        │
│  - Result display          │
└────────────┬───────────────┘
             │ 2. HTTP POST /predict
             │    {"text": "..."}
             ▼
┌────────────────────────────┐
│     FastAPI Backend        │
│     (app.py : 8000)        │
│  - CORS handling           │
│  - Input validation        │
│  - Route to model          │
└────────────┬───────────────┘
             │ 3. Calls model.predict()
             ▼
┌────────────────────────────┐
│     BERT Model             │
│     (model.py)             │
│  - Tokenize text           │
│  - Run inference           │
│  - Return label + score    │
└────────────┬───────────────┘
             │ 4. Returns JSON
             │    {label, id, confidence}
             ▼
┌────────────────────────────┐
│     FastAPI Response       │
│  - Maps label to display   │
│  - Returns to frontend     │
└────────────┬───────────────┘
             │ 5. Displays result
             ▼
STUDENT sees: Anxiety Level + Tips
```

---

## Level 2: Data Flow for Model Inference

```
Raw Text Input
     │
     ▼
Clean Text (lowercase, remove special chars)
     │
     ▼
BERT Tokenizer → Token IDs + Attention Mask
     │
     ▼
BERT Encoder (12 Transformer Layers)
     │
     ▼
Classification Head (768 → 3 logits)
     │
     ▼
Softmax → Probability Distribution [P_low, P_mod, P_high]
     │
     ▼
ArgMax → Predicted Label (0=Low, 1=Moderate, 2=High)
     │
     ▼
Return {prediction_label, prediction_id, confidence}
```
