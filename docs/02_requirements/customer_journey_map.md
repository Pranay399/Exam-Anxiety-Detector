# Customer Journey Map

## Project: AI-Based Exam Anxiety Detector
## User: University Student Experiencing Exam Anxiety

---

## Phase 1: AWARENESS
**Touchpoint:** Student hears about the tool from a classmate or notice board

| Element | Detail |
|---|---|
| **Action** | Hears about Exam Anxiety Detector from a friend |
| **Thought** | "I wonder if this can actually help me understand what I'm feeling" |
| **Emotion** | 😐 Curious but skeptical |
| **Pain Point** | Worried it might not be private or might feel too clinical |
| **Opportunity** | Market via peer recommendation; emphasize privacy |

---

## Phase 2: CONSIDERATION
**Touchpoint:** Student opens the browser and navigates to the Streamlit UI

| Element | Detail |
|---|---|
| **Action** | Opens `http://localhost:8501` in browser |
| **Thought** | "This looks clean and simple. I just need to type?" |
| **Emotion** | 😊 Relieved at simplicity |
| **Pain Point** | Might still be unsure what to type |
| **Opportunity** | Add placeholder text or example prompt in the input box |

---

## Phase 3: USAGE (Core Experience)
**Touchpoint:** Student types thoughts and submits

| Element | Detail |
|---|---|
| **Action** | Types pre-exam thoughts: "I feel like I don't know anything and I'm going to fail tomorrow" |
| **Thought** | "Will this actually understand what I mean?" |
| **Emotion** | 😟 Anxious, hopeful |
| **Pain Point** | Uncertainty about accuracy |
| **Opportunity** | Show model confidence score to build trust |

---

## Phase 4: RESULT RECEIVED
**Touchpoint:** Result displayed with color indicator and tips

| Element | Detail |
|---|---|
| **Action** | Reads result: 🔴 **High Anxiety** with breathing tips |
| **Thought** | "Oh wow this actually understood me. Now I know what I'm feeling is real." |
| **Emotion** | 😮 Validated, slightly less anxious |
| **Pain Point** | May want more detailed or personalized recommendations |
| **Opportunity** | Link to campus counseling resources; add more tips |

---

## Phase 5: POST-EXPERIENCE
**Touchpoint:** Student closes the browser / uses the tips

| Element | Detail |
|---|---|
| **Action** | Follows breathing exercise tip, shares tool with a friend |
| **Thought** | "I should use this before every exam" |
| **Emotion** | 😌 Calmer, empowered |
| **Pain Point** | No way to track progress over time |
| **Opportunity** | Add history dashboard (future feature) |

---

## Emotional Journey Chart

```
Emotion Level (High = Positive)
   
5 ──────────────────────────────────────── 😌 Calm (Post-experience)
4 ─────────────────────── 😊 Relieved ────
3 ──── 😐 Curious ──────────────────────── 😮 Validated
2 ────────────────── 😟 Anxious
1 ──────────────────────────────────────────────────────

     Phase 1      Phase 2     Phase 3     Phase 4     Phase 5
    Awareness  Consideration   Usage    Result Rx   Post-Use
```

---

## Summary of Opportunities

| Phase | Improvement Opportunity |
|---|---|
| Awareness | Email/notice board campaign targeting exam periods |
| Consideration | Add example prompts to guide new users |
| Usage | Show a loading animation to set expectations |
| Result | Add more granular coping tips; show confidence score |
| Post-use | Add mood history / tracking feature |
