# Project Milestones & Tasks

## Project: AI-Based Exam Anxiety Detector
## Sprint Plan — 4 Weeks

---

## Project Timeline

| Phase | Duration | Dates |
|---|---|---|
| Sprint 1: Setup & Planning | Week 1 | March 1–7, 2026 |
| Sprint 2: Data & Model | Week 2 | March 8–14, 2026 |
| Sprint 3: Integration & UI | Week 3 | March 15–21, 2026 |
| Sprint 4: Testing & Deploy | Week 4 | March 22–31, 2026 |

---

## Milestone 1: Environment Setup & System Design
**Sprint:** Week 1  
**Status:** ✅ Complete

| Task | Owner | Status |
|---|---|---|
| Define project scope and problem statement | Team | ✅ |
| Select technology stack | Team | ✅ |
| Set up Python virtual environment (`venv`) | Dev | ✅ |
| Create project folder structure | Dev | ✅ |
| Create `requirements.txt` for all components | Dev | ✅ |
| Initialize Git repository | Dev | ✅ |

---

## Milestone 2: Data Collection & Preprocessing
**Sprint:** Week 1–2  
**Status:** ✅ Complete

| Task | Owner | Status |
|---|---|---|
| Identify Kaggle dataset (Combined Data.csv) | Data | ✅ |
| Write `03_preprocessing.py` | Dev | ✅ |
| Clean and filter text data | Dev | ✅ |
| Map labels: Normal→Low, Stress→Moderate, Anxiety→High | Dev | ✅ |
| Balance dataset (3000 per class = 9000 total) | Dev | ✅ |
| Generate train/val/test splits (70/15/15) | Dev | ✅ |

---

## Milestone 3: Model Training & Evaluation
**Sprint:** Week 2  
**Status:** ✅ Complete

| Task | Owner | Status |
|---|---|---|
| Create `04_bert_model_training.ipynb` for Colab | Dev | ✅ |
| Fine-tune BERT on training data | ML | ✅ |
| Evaluate on validation and test sets | ML | ✅ |
| Save best model weights by validation accuracy | ML | ✅ |
| Export and download `saved_model.zip` | ML | ✅ |
| Place model weights in `models/saved_model/` | Dev | ✅ |

---

## Milestone 4: Backend API Development
**Sprint:** Week 2–3  
**Status:** ✅ Complete

| Task | Owner | Status |
|---|---|---|
| Create `backend/app.py` with FastAPI | Dev | ✅ |
| Create `backend/model.py` (AnxietyModel class) | Dev | ✅ |
| Fix `encode_plus` deprecated API call | Dev | ✅ |
| Add CORS middleware | Dev | ✅ |
| Test `/predict` endpoint manually | Dev | ✅ |
| Test `/health` endpoint | Dev | ✅ |

---

## Milestone 5: Frontend Development
**Sprint:** Week 3  
**Status:** ✅ Complete

| Task | Owner | Status |
|---|---|---|
| Create `frontend/ui.py` with Streamlit | Dev | ✅ |
| Add text input and submit button | Dev | ✅ |
| Connect to FastAPI backend | Dev | ✅ |
| Add color-coded anxiety indicators | Dev | ✅ |
| Add emoji and coping tips | Dev | ✅ |
| Test end-to-end UI → API → Model flow | Dev | ✅ |

---

## Milestone 6: Testing & Deployment
**Sprint:** Week 4  
**Status:** ✅ Complete

| Task | Owner | Status |
|---|---|---|
| Functional testing (all endpoints) | QA | ✅ |
| Edge case testing (empty input, long text) | QA | ✅ |
| UI/UX review | Team | ✅ |
| Create `.gitignore` | Dev | ✅ |
| Push to GitHub | Dev | ✅ |
| Write project documentation | Dev | ✅ |

---

## Sprint Delivery Plan

```
Week 1   [████████] Setup + Data Preprocessing
Week 2   [████████] Model Training + Backend API  
Week 3   [████████] Frontend + Integration
Week 4   [████████] Testing + Docs + GitHub Deploy
```
