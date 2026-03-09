# Problem-Solution Fit

## Project: AI-Based Exam Anxiety Detector

---

## Problem Summary

Students experience exam anxiety that goes undetected until it's too late, largely because:
- No scalable, private, real-time detection tool exists
- Traditional surveys and counselor consultations have high latency
- Students are reluctant to self-report due to social stigma

---

## Solution Summary

An AI-powered text classifier that:
- Accepts free-form student text (thoughts, reflections)
- Instantly classifies anxiety level as Low, Moderate, or High
- Returns actionable coping tips based on the result
- Operates via a browser-based UI with no login required

---

## Problem-Solution Fit Matrix

| Problem | Solution Component | Fit? |
|---|---|---|
| No real-time anxiety detection | BERT model + FastAPI inference (<3s) | ✅ Strong |
| Subjectivity of human assessment | Trained ML model with consistent outputs | ✅ Strong |
| Students reluctant to report | Anonymous, no-login UI | ✅ Strong |
| Generic advice not helpful | 3-tier level system with tailored tips | ✅ Good |
| Delayed intervention | Instant result on every submission | ✅ Strong |
| No data-driven trends for counselors | N/A (future feature) | ⚠️ Partial |

---

## Value Proposition Canvas

### For Students (Customer):
**Jobs to be done:**
- Understand how anxious they are before an exam
- Get specific advice on what to do about their anxiety

**Pains relieved:**
- Removes stigma of speaking to a counselor for "minor" stress
- Provides instant, private feedback
- Validates that their feelings are recognized

**Gains created:**
- Awareness of anxiety level before it spirals
- Actionable steps (breathing, preparation, rest)
- Confidence that they understood

### For Educators (Secondary Customer):
**Jobs to be done:**
- Monitor student wellness without invading privacy
- Identify at-risk students proactively

**Gains created (future):**
- Aggregated dashboard view
- Early intervention triggers

---

## Fit Validation

| Criteria | Result |
|---|---|
| Does the solution solve the core problem? | ✅ Yes — classifies anxiety from text |
| Is the solution accessible to students? | ✅ Yes — browser-based, no login |
| Is the solution fast enough to be useful? | ✅ Yes — sub-3s inference |
| Is the solution accurate enough to be trusted? | ✅ Improving — retrained on 6,000+ samples |
| Is the solution ethical and private? | ✅ Yes — no data stored, no user tracking |

---

## Conclusion

The AI-Based Exam Anxiety Detector demonstrates **a strong problem-solution fit** for the core user segment (students). The solution directly addresses the timeliness, accessibility, and privacy gaps in current mental health support systems available to students.
