import streamlit as st
import pickle
import numpy as np

# Load trained model
with open('mood_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Page configuration
st.set_page_config(page_title="Mood Score Predictor", page_icon="🧠", layout="centered")

# Title
st.title("🧠 Mood Score Predictor")
st.write("Estimate your mood score based on your digital habits and receive tips to improve your well-being.")

# Sidebar for inputs
st.sidebar.header("Your Digital Habits")
screen_time = st.sidebar.slider("Daily Screen Time (hours)", 1.0, 12.0, 6.0)
platforms_used = st.sidebar.slider("Number of Social Media Platforms Used", 1, 5, 3)
tiktok_hours = st.sidebar.slider("Hours on TikTok (daily)", 0.0, 7.2, 2.0)
sleep_hours = st.sidebar.slider("Sleep Hours per Night", 3.0, 10.0, 7.0)
stress_level = st.sidebar.slider("Stress Level (1 = Low, 10 = High)", 1, 10, 6)

# Predict button
if st.button("Predict Mood Score"):
    features = np.array([[screen_time, platforms_used, tiktok_hours, sleep_hours, stress_level]])
    prediction = model.predict(features)[0]

    # Display numeric score
    st.markdown(f"### Predicted Mood Score: *{prediction:.2f}*")

    # Mood level interpretation
    if prediction <= 4:
        st.markdown("<span style='color:red; font-weight:bold;'>Mood Level: Low 😔</span>", unsafe_allow_html=True)
        explanation = "Your digital habits may be negatively affecting your mood. Consider reducing screen time and social media usage."
    elif 4 < prediction <= 7:
        st.markdown("<span style='color:orange; font-weight:bold;'>Mood Level: Moderate 🙂</span>", unsafe_allow_html=True)
        explanation = "Your mood is okay, but there’s room for improvement. Focus on good sleep and moderate social media use."
    else:
        st.markdown("<span style='color:green; font-weight:bold;'>Mood Level: High 😄</span>", unsafe_allow_html=True)
        explanation = "Great! Your digital habits are supporting a positive mood. Keep maintaining balanced screen time and healthy sleep."
    
    st.info(explanation)

    # Personalized recommendations
    st.subheader("💡 Tips to Improve Your Mood")
    if screen_time > 8:
        st.write("- Reduce your daily screen time to avoid digital fatigue.")
    if tiktok_hours > 2:
        st.write("- Limit time spent on TikTok or social media apps to prevent overstimulation.")
    if sleep_hours < 7:
        st.write("- Aim for 7-9 hours of sleep each night for better mental health.")
    if stress_level > 6:
        st.write("- Practice stress management techniques like meditation, exercise, or short breaks.")
    if 4 < prediction <= 7:
        st.write("- Maintain a balanced lifestyle with moderate screen time and social interaction.")
    if prediction > 7:
        st.write("- Keep up the good habits! Consider sharing your routine tips with others.")