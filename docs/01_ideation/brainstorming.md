# Brainstorming Template

## Project: AI-Based Exam Anxiety Detector

---

## Brainstorming Session Overview

**Date:** March 2026  
**Team:** AI Development Group  
**Method:** Mind Mapping + How Might We (HMW) + Crazy 8s  

---

## Central Theme
*"Detecting exam anxiety from student-written text using AI"*

---

## Ideas Generated

### A. Input Methods
- ✅ Free-form text box for student reflections
- Chat-style journaling interface
- Voice-to-text input (future)
- Pre-exam check-in forms
- WhatsApp/Telegram bot integration (future)

### B. AI/ML Approaches
- ✅ Fine-tuned BERT model for classification
- GPT-based sentiment analysis
- Rule-based keyword detection (baseline)
- Ensemble of multiple models
- Real-time streaming inference
- Multi-language support (future)

### C. Output / Feedback Methods
- ✅ Color-coded anxiety level indicator (Green / Yellow / Red)
- ✅ Actionable coping tips per level
- Personalized recommendations based on history
- Mood tracker with historical graph
- Email alerts to counselors for High Anxiety detection

### D. Data Sources Considered
- ✅ Kaggle "Sentiment Analysis for Mental Health" (Combined Data.csv)
- Reddit mental health subreddits (r/anxiety, r/exams)
- Survey-based synthetic data (rejected)
- Clinical psychology datasets

### E. Technology Stack Ideas
- ✅ BERT (HuggingFace Transformers) — NLP model
- ✅ FastAPI — backend inference API
- ✅ Streamlit — frontend
- Flask REST API (alternative)
- React + Node.js frontend (overkill for prototype)
- Google Colab for GPU training

---

## How Might We (HMW) Questions

| # | HMW Question |
|---|---|
| 1 | HMW make it easy for students to share how they feel before an exam? |
| 2 | HMW ensure the AI output is accurate enough to be trusted? |
| 3 | HMW make the anxiety level result feel supportive, not clinical? |
| 4 | HMW enable educators to see trends without violating student privacy? |
| 5 | HMW make the system accessible on any device with a browser? |

---

## Ideas Shortlisted for Development

| Feature | Priority | Status |
|---|---|---|
| Text-based anxiety classification (Low/Moderate/High) | High | ✅ Done |
| Color-coded results UI | High | ✅ Done |
| Coping tips per anxiety level | Medium | ✅ Done |
| FastAPI backend | High | ✅ Done |
| Streamlit frontend | High | ✅ Done |
| Historical mood tracker | Low | 🔜 Future |
| Counselor dashboard | Low | 🔜 Future |
| Mobile app | Low | 🔜 Future |

---

## Ideas NOT Pursued (with reasons)

| Idea | Reason Not Selected |
|---|---|
| Voice input | Adds complexity; text is sufficient for v1 |
| Multi-language | Dataset only in English; scope limitation |
| Chatbot interface | Out of scope; would require LLM integration |
| React frontend | Streamlit faster for prototyping |
