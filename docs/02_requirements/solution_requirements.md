# Solution Requirements

## Project: AI-Based Exam Anxiety Detector

---

## 1. Functional Requirements

### FR-01: Text Input
- The system SHALL accept free-form text input of up to 512 words from users.
- The input SHALL NOT require user login or registration.

### FR-02: Anxiety Classification
- The system SHALL classify input text into one of three categories:
  - **Low Anxiety** (Label: 0 / Normal)
  - **Moderate Anxiety** (Label: 1 / Stress)
  - **High Anxiety** (Label: 2 / Anxiety)
- Classification SHALL be performed using a fine-tuned BERT model.

### FR-03: Confidence Score
- The system SHALL return a confidence score (percentage) alongside the predicted label.

### FR-04: Results Display
- The system SHALL display the prediction with:
  - A color-coded indicator (Green = Low, Yellow = Moderate, Red = High)
  - An emoji representing the anxiety level
  - A brief description of what the level means
  - A set of contextual, actionable coping tips

### FR-05: API Endpoints
- The backend SHALL expose a `POST /predict` endpoint accepting JSON `{"text": "..."}`
- The backend SHALL expose a `GET /health` endpoint returning server status

### FR-06: Response Time
- The system SHALL return a prediction within **3 seconds** under normal load.

---

## 2. Non-Functional Requirements

### NFR-01: Performance
- The model inference SHALL complete in under 1.5 seconds for a 128-token input.
- The FastAPI server SHALL handle at least 10 concurrent requests.

### NFR-02: Accuracy
- The trained classification model SHALL achieve at least **75% accuracy** on the held-out test set.

### NFR-03: Availability
- The system SHALL be available for testing at `http://localhost:8501` when both servers are running.

### NFR-04: Security
- API keys and sensitive configurations SHALL NOT be hard-coded in source files.
- CORS policy SHALL restrict API access to trusted origins only.

### NFR-05: Privacy
- No student text inputs SHALL be stored in a database or logged in v1.
- The system SHALL process input in-memory only.

### NFR-06: Maintainability
- All code SHALL follow PEP-8 Python standards.
- Model weights SHALL be stored separately from application code.
- Dependency versions SHALL be pinned in `requirements.txt`.

### NFR-07: Portability
- The application SHALL run on any machine with Python 3.10+ and the venv activated.
- The system SHALL support Windows, macOS, and Linux environments.

---

## 3. Data Requirements

| Requirement | Details |
|---|---|
| Dataset Source | Kaggle — "Sentiment Analysis for Mental Health" (Combined Data.csv) |
| Dataset Size | ~94,000 records (filtered to ~9,000 balanced samples for training) |
| Labels Used | Normal → Low, Stress → Moderate, Anxiety → High |
| Train/Val/Test Split | 70% / 15% / 15% |
| Text Column | `statement` |
| Label Column | `status` |

---

## 4. Constraints

- The system supports **English language only** in v1.
- The model is NOT a replacement for professional medical or psychological evaluation.
- Model training requires a GPU environment (Google Colab recommended).
- Inference on CPU is supported but may be slower than specified SLA.
