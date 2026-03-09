import streamlit as st
import requests

API_URL = "http://localhost:8000/predict"

st.set_page_config(page_title="Exam Anxiety Detector", page_icon="🧠", layout="centered")

# Custom CSS for visuals
st.markdown("""
<style>
    .low { background-color: #d4edda; color: #155724; padding: 10px; border-radius: 5px; }
    .moderate { background-color: #fff3cd; color: #856404; padding: 10px; border-radius: 5px; }
    .high { background-color: #f8d7da; color: #721c24; padding: 10px; border-radius: 5px; }
</style>
""", unsafe_allow_html=True)

st.title("🧠 AI-Based Exam Anxiety Detector")
st.write("Welcome to the Mental Wellness Support System. Share your thoughts or feelings about your upcoming exams, and let AI help you understand your anxiety levels.")

st.markdown("---")

user_input = st.text_area("How are you feeling about your exams?", 
                          placeholder="e.g., I'm really worried about my physics final, I feel like I'll forget everything...",
                          height=150)

if st.button("Analyze My Feelings"):
    if user_input.strip() == "":
        st.warning("Please enter some text before analyzing.")
    else:
        with st.spinner("Analyzing your text..."):
            try:
                response = requests.post(API_URL, json={"text": user_input})
                if response.status_code == 200:
                    data = response.json()
                    label = data["prediction_label"]
                    confidence = data["confidence"]

                    st.markdown("### Analysis Result:")
                    
                    if label == "Low":
                        st.markdown(f'<div class="low"><b>{label} Anxiety Detected</b> (Confidence: {confidence}%) 😌</div>', unsafe_allow_html=True)
                        st.success("You seem to be managing your exam stress well! Keep up the good work.")
                        st.markdown("**Tips:**\n- Maintain your current study routine.\n- Keep getting good sleep.\n- Stay hydrated and take light breaks.")

                    elif label == "Moderate":
                        st.markdown(f'<div class="moderate"><b>{label} Anxiety Detected</b> (Confidence: {confidence}%) 😟</div>', unsafe_allow_html=True)
                        st.warning("You are experiencing a moderate level of anxiety. Remember that some stress is normal and can even help keep you focused, but don't let it overwhelm you.")
                        st.markdown("**Tips:**\n- Try the Pomodoro technique for studying to avoid burnout.\n- Practice mindful deep breathing when you feel tense.\n- Review topics you feel least confident about first.")

                    elif label == "High":
                        st.markdown(f'<div class="high"><b>{label} Anxiety Detected</b> (Confidence: {confidence}%) 😰</div>', unsafe_allow_html=True)
                        st.error("You are experiencing high levels of anxiety. Your mental health is extremely important.")
                        st.markdown("**Tips:**\n- **Stop studying for now.** Take a 30-minute break away from your screen and books.\n- Talk to a friend, family member, or school counselor.\n- Try the '4-7-8' breathing exercise (inhale for 4 seconds, hold for 7, exhale for 8).\n- Remember that a single exam does not define your worth.")
                
                else:
                    st.error(f"Error from API: {response.text}")
            except requests.exceptions.ConnectionError:
                st.error("Could not connect to the backend server. Is the FastAPI application running?")
            except Exception as e:
                st.error(f"An unexpected error occurred: {e}")

st.markdown("---")
st.caption("Disclaimer: This system is designed as a supportive and non-diagnostic tool. It should not replace professional psychological or medical advice.")
