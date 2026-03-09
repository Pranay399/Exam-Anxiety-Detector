# Technology Stack

## Project: AI-Based Exam Anxiety Detector

---

## Overview

The AI-Based Exam Anxiety Detector uses a modern, full-stack AI architecture designed for real-time text classification. Every layer of the stack was selected based on cost-effectiveness (open-source), developer community support, and fitness for purpose.

---

## Technology Stack Summary

| Layer | Technology | Version | Purpose |
|---|---|---|---|
| **Machine Learning** | PyTorch | 2.1+ | Deep learning framework |
| **NLP Model** | BERT (bert-base-uncased) | HuggingFace | Text classification transformer |
| **Tokenizer** | BertTokenizer | HuggingFace Transformers | Text preprocessing |
| **Backend Framework** | FastAPI | 0.109+ | REST API for model inference |
| **Backend Server** | Uvicorn | 0.27+ | ASGI server for FastAPI |
| **Frontend Framework** | Streamlit | 1.31+ | Interactive web UI |
| **Data Processing** | Pandas | 2.x | Data loading and manipulation |
| **ML Utilities** | Scikit-learn | 1.4+ | Train/test split, metrics |
| **Model Training** | Google Colab | - | GPU-accelerated training environment |
| **Version Control** | Git + GitHub | - | Source code management |
| **Language** | Python | 3.10+ | Primary programming language |

---

## Why These Technologies?

### 🤖 BERT (bert-base-uncased)
- Industry-standard pre-trained transformer model
- Excellent at understanding context in text (unlike bag-of-words models)
- Available freely on HuggingFace without authentication
- 110M parameter base model — accurate but fast enough for real-time inference

### ⚡ FastAPI
- Fastest Python web framework for building APIs
- Auto-generates OpenAPI (Swagger) documentation at `/docs`
- Supports async endpoints for non-blocking inference
- Built-in Pydantic validation

### 🖥️ Streamlit
- Zero-HTML frontend development in pure Python
- Ideal for AI/ML demo apps and rapid prototyping
- Built-in support for markdown, charts, and dynamic components

### 🔥 PyTorch
- Most widely used DL framework in research and industry
- Native integration with HuggingFace Transformers
- Strong GPU/CUDA support for fast training

### ☁️ Google Colab
- Free T4 GPU runtime (~15-30 mins to train BERT)
- No local setup required for model training
- Jupyter notebook interface familiar to students

---

## Architecture Layers

```
┌──────────────────────────────────────────┐
│          Streamlit Frontend               │
│    (ui.py — Port 8501)                   │
│    Text Input → API Call → Display       │
└──────────────┬───────────────────────────┘
               │ HTTP POST /predict
               ▼
┌──────────────────────────────────────────┐
│          FastAPI Backend                 │
│    (app.py + model.py — Port 8000)       │
│    Receive Text → Tokenize → Infer       │
└──────────────┬───────────────────────────┘
               │
               ▼
┌──────────────────────────────────────────┐
│       Fine-tuned BERT Model              │
│    (models/saved_model/)                 │
│    pytorch_model.bin / model.safetensors │
└──────────────────────────────────────────┘
```

---

## Development Environment

| Tool | Version/Details |
|---|---|
| OS | Windows 11 |
| Python | 3.10+ (via `venv`) |
| IDE | Visual Studio Code |
| Package Management | pip + requirements.txt |
| GPU Training | Google Colab (T4 GPU) |
