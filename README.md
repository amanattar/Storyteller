# AI-Driven Storyteller

AI-Driven Storyteller is a Streamlit-based web application that generates creative stories from user-provided titles. Using OpenAI's powerful GPT models, this application creates engaging, vivid, and structured stories tailored to the user's preferences.

## Features
- **Story Title Input**: Users can enter a story title as inspiration for the generated story.
- **Length Options**: Choose between short (500 words), medium (1000 words), or long (1500 words) stories.
- **Creativity Control**: Adjust the AI's creativity level using a temperature slider.
- **Centered Title Display**: The generated story includes a centered title for better aesthetics.
- **Real-Time Story Generation**: Stories are generated dynamically based on the title and settings.

---

## Installation and Setup

### Prerequisites
1. [Python 3.10+](https://www.python.org/downloads/)
2. [OpenAI API Key](https://platform.openai.com/signup/)
3. [Streamlit](https://streamlit.io/)

### Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/ai-driven-storyteller.git
   cd ai-driven-storyteller
   ```

2. **Create a Python Environment**:
   ```bash
   conda create -n storyteller python=3.10 -y
   conda activate storyteller
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up OpenAI API Key**:
   - Open the `storyteller_app.py` file.
   - Replace the placeholder API key with your actual API key:
     ```plaintext
     openai.api_key = "your-api-key-here"
     ```

5. **Run the Application**:
   ```bash
   streamlit run storyteller_app.py
   ```

6. **Access the App**:
   Open your browser and navigate to `http://localhost:8501`.

---

## Usage

### Generate a Story
1. Enter a title for your story (e.g., "The Lost Treasure").
2. Select a story length:
   - Short (800 words)
   - Medium (1700 words)
   - Long (2500 words)
3. Adjust the creativity slider to set the AI's storytelling style.
4. Click **Generate Story**.

### View the Story
- The app will display the title (centered) followed by the generated story.

---

## Example

### Input:
- **Title**: The Lost Treasure
- **Length**: Medium (1700 words)
- **Creativity**: 0.8

### Output:
#### The Lost Treasure

*Once upon a time, in a small coastal village, there was a legend about a hidden treasure buried deep within the forest...*

[Full story continues...]

---

## Project Structure
```
ai-driven-storyteller/
├── storyteller_app.py  # Main application script
├── requirements.txt    # Required Python packages
└── README.md           # Project documentation
```

---

## Customization
- **Modify the Prompt**:
  You can tweak the story generation prompt in `storyteller_app.py` to create specific types of stories (e.g., fantasy, sci-fi).
- **Add New Features**:
  Feel free to enhance the app with additional settings like genre selection or story character customization.

---

## Dependencies
- `openai`
- `streamlit`
---

## License
This project is licensed under the MIT License. See `LICENSE` for more details.
