import pandas as pd
import numpy as np
import random
import os

# Set seed for reproducibility
random.seed(42)
np.random.seed(42)

# Define templates for different anxiety levels
low_anxiety_templates = [
    "I'm feeling pretty confident about the {subject} exam.",
    "I have studied well and I am ready for this test.",
    "I slept well and went through all my notes. Feeling relaxed.",
    "The {subject} syllabus was straightforward. Not too worried.",
    "Looking forward to getting this exam over with, I know I'll do fine.",
    "I took a few mock tests and scored well. Feeling good.",
    "Honestly, I'm just calm. I know the material.",
    "Prepared as much as I could. Whatever happens, happens, but I feel okay.",
    "Feeling perfectly normal, no stress at all for {subject}.",
    "I have a good grasp of the concepts. Ready to go."
]

moderate_anxiety_templates = [
    "I'm a bit nervous about the {subject} paper, hope it's not too hard.",
    "I studied a lot but I still feel like I might forget some formulas.",
    "Feeling slightly jittery, the syllabus is huge.",
    "Trying to stay calm, but my heart is beating a little fast.",
    "I think I'll pass, but I really want a good grade, which makes me anxious.",
    "Not entirely sure about a few topics in {subject}. Just hoping they don't appear.",
    "A bit stressed because I didn't sleep much last night.",
    "I'm worried about time management during the exam.",
    "Feeling tense in my shoulders, but I can manage.",
    "Slightly overwhelmed, need to review my notes one last time."
]

high_anxiety_templates = [
    "I am absolutely terrified. I feel like I'm going to fail {subject}.",
    "My hands are shaking, I can't concentrate or remember anything.",
    "I'm having a panic attack about this test. The pressure is too much.",
    "I feel completely unprepared. I'm going to ruin my GPA.",
    "I couldn't sleep at all. My heart is racing and I feel sick to my stomach.",
    "I'm crying because I don't understand the {subject} material at all.",
    "This is too overwhelming. I want to give up. I'm so stressed.",
    "I'm terrified of blanking out the moment I see the paper.",
    "My chest is tight and I can't breathe properly thinking about this exam.",
    "Total dread. I feel severely anxious and paralyzed by fear of failure."
]

subjects = ["Math", "Physics", "Chemistry", "Biology", "History", "Literature", "Computer Science", "Economics"]

def generate_sentence(template_list):
    template = random.choice(template_list)
    return template.format(subject=random.choice(subjects))

# Generate dataset
num_samples = 450
data = []

# Balanced dataset: 150 each
for _ in range(150):
    data.append({"text": generate_sentence(low_anxiety_templates), "label_text": "Low", "label": 0})
    data.append({"text": generate_sentence(moderate_anxiety_templates), "label_text": "Moderate", "label": 1})
    data.append({"text": generate_sentence(high_anxiety_templates), "label_text": "High", "label": 2})

# Add some variations and noise
additional_noise = [
    ("This is just another day.", "Low", 0),
    ("Whatever.", "Low", 0),
    ("I need to pass, please.", "Moderate", 1),
    ("My hands are sweaty.", "High", 2),
    ("Help me.", "High", 2)
]

for _ in range(10): # Duplicate noise heavily to add randomness
    for text, label_text, label in additional_noise:
        data.append({"text": text, "label_text": label_text, "label": label})

df = pd.DataFrame(data)

# Shuffle
df = df.sample(frac=1).reset_index(drop=True)

# Save to CSV
output_path = "../data/exam_anxiety_dataset.csv"
os.makedirs("../data", exist_ok=True)
df.to_csv(output_path, index=False)
print(f"Generated synthetic dataset with {len(df)} records at {output_path}")
print(df.head(10))
print("\nLabel Distribution:")
print(df['label_text'].value_counts())
