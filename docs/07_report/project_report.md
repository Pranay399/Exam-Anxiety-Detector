# Project Report: AI-Based Exam Anxiety Detector

**Version:** 1.0  
**Date:** March 2026  
**GitHub:** https://github.com/Pranay399/Exam-Anxiety-Detector

---

## Project Title
**AI-Based Exam Anxiety Detector**

---

## Project Description

The AI-Based Exam Anxiety Detector is an intelligent mental wellness support system that identifies and categorizes exam-related anxiety from student-generated text using Natural Language Processing (NLP) and a fine-tuned BERT deep learning model.

Students type pre-exam thoughts, reflections, or feelings into a browser-based interface. The system classifies their input into **Low**, **Moderate**, or **High** anxiety levels and returns actionable coping tips — all in real time.

---

## Application Scenarios & Use Cases

| Scenario | Description |
|---|---|
| Pre-exam self-check | Student types their thoughts before an exam to understand their anxiety level |
| Counselor support | Counselors can ask students to use the tool as a first-step wellness check |
| Academic monitoring | Institutions can deploy the tool during exam season to identify trends |
| Research | Researchers can use the model to classify student journal entries |

---

## Technical Architecture Overview

```
[Student] → [Streamlit UI :8501] → HTTP POST → [FastAPI API :8000]
                                                       ↓
                                              [BERT Model Inference]
                                                       ↓
                                              [Anxiety Label + Confidence]
```

Full architecture described in: `docs/03_design/solution_architecture.md`

---

## Prerequisites

- Python 3.10+
- pip (Python package manager)
- Git
- Google Colab account (for model training only)
- Minimum 4GB RAM for model inference
- Internet access (for downloading BERT from HuggingFace on first run)

---

## Prior Knowledge Required

| Domain | Level |
|---|---|
| Python programming | Intermediate |
| Machine Learning concepts | Basic |
| REST APIs | Basic |
| Deep Learning / Transformers | Basic |
| Git & GitHub | Basic |

---

## Project Objectives

1. Build a real-time NLP classification system for exam anxiety detection
2. Fine-tune a BERT-based model on a mental health dataset from Kaggle
3. Develop a FastAPI backend for serving model predictions
4. Create an intuitive Streamlit frontend for student interaction
5. Deploy the codebase to GitHub for version control and collaboration

---

## System Workflow

```
Step 1: Student opens browser → http://localhost:8501
Step 2: Student types pre-exam thoughts in text box
Step 3: Student clicks "Analyse My Anxiety"
Step 4: Streamlit sends POST /predict to FastAPI backend
Step 5: FastAPI tokenizes text using BertTokenizer (128 tokens)
Step 6: BERT model runs forward pass → 3 logits
Step 7: Softmax → probabilities → argmax → predicted class
Step 8: Response JSON returned to frontend
         {prediction_label: "High", confidence: 82.5}
Step 9: Streamlit displays:
         - Color indicator (🔴 Red for High)
         - Anxiety level label
         - Confidence score
         - Coping tips for High Anxiety
```

---

## Milestone Summary

### Milestone 1: Requirement Analysis & System Design
- Defined problem statement: lack of real-time exam anxiety detection for students
- Selected BERT + FastAPI + Streamlit architecture
- Created empathy maps, user stories, and data flow diagrams

### Milestone 2: Environment Setup & Initial Configuration
- Created Python virtual environment
- Installed PyTorch, HuggingFace Transformers, FastAPI, Streamlit
- Set up project folder structure and GitHub repository

### Milestone 3: Core System Development
- Acquired and preprocessed Kaggle "Combined Data.csv" dataset
- Label mapping: Normal→Low, Stress→Moderate, Anxiety→High
- Sampled and balanced 9,000 training records
- Fine-tuned `bert-base-uncased` on Google Colab T4 GPU

### Milestone 4: Integration & Optimization
- Built FastAPI backend with `/predict` and `/health` endpoints
- Integrated `AnxietyModel` singleton with warm model loading
- Fixed deprecated `encode_plus` API for newer transformer versions
- Connected Streamlit frontend to backend API
- Implemented color-coded result display and anxiety-level coping tips

### Milestone 5: Testing & Validation
- Ran functional tests across 8 test cases
- Conducted User Acceptance Testing with 5 students
- 90% UAT success rate
- Weighted F1-score: ~0.77 on held-out test set

---

## Deployment

### Local Deployment

**Backend (Terminal 1):**
```bash
cd backend
..\venv\Scripts\uvicorn app:app --port 8000 --reload
```

**Frontend (Terminal 2):**
```bash
cd frontend
..\venv\Scripts\streamlit run ui.py --server.port 8501
```

**Access UI:** http://localhost:8501  
**Access API docs:** http://localhost:8000/docs

---

## Project Structure

```
Gen AI Anxiety/
├── backend/
│   ├── app.py              # FastAPI application
│   ├── model.py            # BERT model loader & inference
│   └── requirements.txt
├── frontend/
│   ├── ui.py               # Streamlit UI
│   └── requirements.txt
├── notebooks/
│   ├── 03_preprocessing.py # Data preprocessing
│   └── 04_bert_model_training.ipynb
├── data/
│   ├── train.csv
│   ├── val.csv
│   └── test.csv
├── models/
│   └── saved_model/        # Fine-tuned BERT weights
├── docs/                   # All project documentation
├── .gitignore
└── README.md
```

---

## Results

| Metric | Value |
|---|---|
| Training Dataset Size | 6,068 samples (balanced) |
| Validation Accuracy | ~77% |
| Test F1-Score (Weighted Avg) | ~0.77 |
| API Inference Time | < 2.5 seconds (CPU) |
| UAT Approval Rate | 90% |

---

## Advantages & Limitations

### Advantages
- Real-time, instant classification (no waiting for counselor)
- Private — no login, no data storage
- Accessible via any web browser
- Extensible architecture (API-first design)
- BERT captures contextual language nuances

### Limitations
- English language only (v1)
- Model accuracy depends on dataset quality
- Not a substitute for professional psychological evaluation
- CPU inference is 2–3x slower than GPU
- No persistent user history in v1

---

## Future Enhancements

| Feature | Priority |
|---|---|
| User history dashboard (SQLite/PostgreSQL) | High |
| Mobile-responsive UI redesign | Medium |
| Multi-language support | Medium |
| Counselor analytics dashboard | High |
| Cloud deployment (AWS / GCP / Azure) | High |
| Voice-to-text input | Low |
| Integration with LMS (Moodle/Canvas) | Medium |

---

## Conclusion

The AI-Based Exam Anxiety Detector successfully demonstrates an end-to-end AI system for real-time mental wellness support tailored to students. By combining a fine-tuned BERT model, a production-ready FastAPI backend, and an accessible Streamlit frontend, the system provides instant, private, and actionable insights into student anxiety levels.

The tool represents a significant step toward proactive, AI-driven mental health support in educational institutions — shifting the paradigm from reactive counseling to preventive, data-informed wellness monitoring.
