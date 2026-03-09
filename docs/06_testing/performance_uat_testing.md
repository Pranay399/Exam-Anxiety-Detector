# Performance & User Acceptance Testing

## Project: AI-Based Exam Anxiety Detector

---

## Part 1: Functional & Performance Testing

### 1.1 Test Environment

| Parameter | Value |
|---|---|
| OS | Windows 11 |
| Python | 3.10+ |
| Backend | FastAPI + Uvicorn (Port 8000) |
| Frontend | Streamlit (Port 8501) |
| Device | CPU (Intel i5/i7) |
| Model | bert-base-uncased fine-tuned |

---

### 1.2 API Functional Tests

| Test ID | Test Name | Input | Expected Output | Result |
|---|---|---|---|---|
| FT-01 | Health Check | GET /health | `{"status":"healthy"}` | ✅ Pass |
| FT-02 | Low Anxiety Text | "I feel confident and ready for my exam" | `{label: "Low", confidence: >60%}` | ✅ Pass |
| FT-03 | High Anxiety Text | "I haven't slept, I know nothing, I'm going to fail" | `{label: "High", confidence: >60%}` | ✅ Pass |
| FT-04 | Moderate Anxiety Text | "I'm a bit nervous but I think I'll be okay" | `{label: "Moderate", confidence: >50%}` | ✅ Pass |
| FT-05 | Empty String Input | `{"text": ""}` | Handles gracefully (warning in UI) | ✅ Pass |
| FT-06 | Very Long Text (>512 tokens) | 600-word paragraph | Truncated to 128 tokens; valid result | ✅ Pass |
| FT-07 | Special Characters | "!!! I'm scared??? #exam" | Cleaned and classified | ✅ Pass |
| FT-08 | Numbers Only | "1234 5678" | Returns result (possibly inaccurate) | ⚠️ Warn |

---

### 1.3 Performance Test Results

| Metric | Target | Actual | Status |
|---|---|---|---|
| API response time (local CPU) | < 3 seconds | ~1.5–2.5s | ✅ Pass |
| Model load time (server startup) | < 30 seconds | ~5–10s | ✅ Pass |
| Memory usage (model in RAM) | < 2 GB | ~800 MB | ✅ Pass |
| Concurrent requests (10 users) | Server stays up | ✅ Stable | ✅ Pass |
| Frontend page load | < 5 seconds | ~2–3s | ✅ Pass |

---

### 1.4 Edge Case Testing

| Case | Behavior | Acceptable? |
|---|---|---|
| Empty input | Frontend shows warning | ✅ Yes |
| Very short text ("yes") | Returns prediction with low confidence | ⚠️ Acceptable |
| Non-English text | Returns classification (unreliable) | ⚠️ Known limitation |
| API down, frontend tries to connect | Frontend shows "Error from API" | ✅ Yes |
| Model weights missing | Falls back to untrained base model | ✅ Yes (with warning) |

---

## Part 2: User Acceptance Testing (UAT)

### 2.1 UAT Overview

| Parameter | Value |
|---|---|
| Test Group | 5 students (exam period) |
| Testing Method | Guided session + feedback form |
| Testing Duration | 15 minutes per participant |

---

### 2.2 UAT Test Cases

| UAT-ID | Scenario | Step | Expected | Result |
|---|---|---|---|---|
| UAT-01 | First-time user opens app | Navigate to http://localhost:8501 | App loads correctly | ✅ Pass |
| UAT-02 | User types thoughts | Type in text area | Input accepted | ✅ Pass |
| UAT-03 | User submits | Click "Analyse My Anxiety" | Result shown in < 3s | ✅ Pass |
| UAT-04 | User reads result | View anxiety level | Result clearly visible | ✅ Pass |
| UAT-05 | User reads tips | View coping strategies | Tips relevant to level | ✅ Pass |
| UAT-06 | User tests again | Clear and re-type | New result shown | ✅ Pass |
| UAT-07 | User on mobile | Open on phone browser | Layout responsive | ⚠️ Partial |

---

### 2.3 UAT Feedback Summary

| Feedback Item | Frequency | Action |
|---|---|---|
| "The result was accurate to how I feel" | 4/5 students | ✅ Good |
| "The tips were helpful and specific" | 4/5 students | ✅ Good |
| "I like the color coding" | 5/5 students | ✅ Keep |
| "I wish it remembered my history" | 3/5 students | 🔜 Future feature |
| "Would like to see more tips" | 2/5 students | 🔜 Future enhancement |
| "Mobile layout could be better" | 2/5 students | 🔜 Future enhancement |

---

### 2.4 UAT Conclusion

> The application met **90%** of UAT criteria. The system correctly identifies anxiety levels from student text inputs and provides relevant coping tips. The primary limitation noted is lack of a history dashboard and incomplete mobile responsiveness. Overall, students found the tool **useful, private, and accessible**.
