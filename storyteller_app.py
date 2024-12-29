import streamlit as st
import openai

# Set OpenAI API key
openai.api_key = "Open_AI_API_Key"

st.title("AI-Driven Storyteller")
st.subheader("Generate creative stories effortlessly from just a title!")

# User input for story generation
story_title = st.text_input("Enter a story title:", placeholder="The Lost Treasure")

# Story length options
length_option = st.selectbox(
    "Choose story length:",
    options=["Short (800 words)", "Medium (1700 words)", "Long (2500 words)"]
)

# Map length option to max_tokens
length_map = {
    "Short (800 words)": 800,
    "Medium (1700 words)": 1700,
    "Long (2500 words)": 2500
}
max_tokens = length_map[length_option]

# Set creativity level
creativity = st.slider("Set creativity level (temperature):", min_value=0.0, max_value=1.0, value=0.7)

# Generate story button
if st.button("Generate Story"):
    if story_title.strip():
        with st.spinner("Generating your story..."):
            try:
                # Prompt engineering
                prompt = (
                    f"Generate a creative, engaging, and well-structured story based on the following title:\n\n"
                    f"Title: {story_title}\n\n"
                    f"Ensure the story has a clear beginning, middle, and end. Add vivid descriptions, "
                    f"interesting characters, and unexpected twists to make it captivating."
                )

                # Call OpenAI API
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "user", "content": prompt}
                    ],
                    max_tokens=max_tokens,
                    temperature=creativity
                )
                story = response.choices[0].message['content'].strip()
                
                # Display the title in the center
                st.markdown(f"<h2 style='text-align: center;'>{story_title}</h2>", unsafe_allow_html=True)
                st.write(story)
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter a story title.")

st.caption("Created by Aman Attar")
