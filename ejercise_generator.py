import streamlit as st
import openai
import os

# Configure your OpenAI API key securely through environment variable
openai.KEY_ALPHA = os.getenv("KEY_ALPHA")


# Configure your OpenAI API key
client = OpenAI(api_key= openai.KEY_ALPHA )

# Streamlit UI
st.title("AI-powered ESL Exercise Generator")

# Selectors for the exercise parameters
level = st.selectbox("Choose English Level", ["A1", "A2", "B1", "B2", "C1", "C2"])
topic = st.text_input("Topic", "Travel")
exercise_type = st.selectbox("Exercise Type", ["Vocabulary", "Grammar", "Speaking", "Listening comprehension", "Reading comprehension", "Writing"])

# Button to generate the exercise
if st.button("Generate Exercise"):
    with st.spinner('Generating your exercise...'):
        prompt = (
            f"You are an English teacher assistant AI specialized in generating ESL exercises. "
            f"Create an exercise based on the following criteria:\n"
            f"Level: {level}\n"
            f"Topic: {topic}\n"
            f"Exercise Type: {exercise_type}\n"
            f"Task Instructions: Clearly describe what students need to do.\n\n"
            f"Provide the exercise content first, followed by an answer key or model solution."
        )

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )

        exercise = response.choices[0].message.content

        st.markdown("### Generated Exercise")
        st.write(exercise)
