import streamlit as st
from openai import OpenAI
import openai  # for exception handling
import os

# Initialize the OpenAI client
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])


# Streamlit UI
st.title("FLYNT ESL Exercise Generator")

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
            f"Provide the exercise content first, followed by an answer key or model solution. the solution has to be separaded quite a bit from the exercise.\n"
            f"Provide the exercise content using clear formatting:\n"
            f"- Use underscores (____) or [   ] for blank spaces\n"
            f"- Use Markdown tables for structured formats like matching or multiple choice\n"
            f"- Separate the answer key clearly at the end\n"
        )

        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            exercise = response.choices[0].message.content
            st.markdown("### Generated Exercise")
            st.write(exercise)
        except openai.OpenAIError as e:
            st.error(f"OpenAI API Error: {str(e)}")
        except Exception as e:
            st.error(f"Unexpected error: {str(e)}")
