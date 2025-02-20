import streamlit as st
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Default OpenAI API Key (Can be overridden in UI)
DEFAULT_API_KEY = os.getenv("OPENAI_API_KEY", "")

# Default OpenAI settings
MODEL_OPTIONS = [
    "gpt-4",
    "gpt-4o",
    "gpt-4o-mini",
    "gpt-3.5-turbo",
]
DEFAULT_MODEL = "gpt-4"
DEFAULT_PROMPT = os.getenv("SYSTEM_PROMPT", "You are a helpful assistant.")
DEFAULT_TEMPERATURE = 0.7
DEFAULT_MAX_TOKENS = 500
DEFAULT_TOP_P = 1.0
DEFAULT_FREQUENCY_PENALTY = 0.0
DEFAULT_PRESENCE_PENALTY = 0.0

# Streamlit UI - Page Config
st.set_page_config(page_title="ChatGPT UI", page_icon="🤖", layout="wide")

# Custom CSS for UI Styling
st.markdown(
    """
    <style>
        .stTextInput, .stSlider, .stSelectbox {border-radius: 10px !important;}
        .stTextArea {border-radius: 10px !important;}
        .stButton > button {border-radius: 10px !important; background-color: #4CAF50; color: white; font-size: 18px;}
        .stMarkdown {font-size: 18px;}
    </style>
""",
    unsafe_allow_html=True,
)

# Sidebar - Configuration Inputs
st.sidebar.title("⚙️ ChatGPT Settings")

api_key = st.sidebar.text_input(
    "🔑 OpenAI API Key", type="password", value=DEFAULT_API_KEY
)
model = st.sidebar.selectbox("🧠 Model", MODEL_OPTIONS, index=0)
system_prompt = st.sidebar.text_area("💡 System Prompt", DEFAULT_PROMPT, height=100)
temperature = st.sidebar.slider("🌡️ Temperature", 0.0, 1.0, DEFAULT_TEMPERATURE, 0.1)
max_tokens = st.sidebar.slider("🔢 Max Tokens", 50, 4096, DEFAULT_MAX_TOKENS, 50)
top_p = st.sidebar.slider("🎯 Top P", 0.0, 1.0, DEFAULT_TOP_P, 0.1)
frequency_penalty = st.sidebar.slider(
    "📉 Frequency Penalty", -2.0, 2.0, DEFAULT_FREQUENCY_PENALTY, 0.1
)
presence_penalty = st.sidebar.slider(
    "📈 Presence Penalty", -2.0, 2.0, DEFAULT_PRESENCE_PENALTY, 0.1
)

# Main Chat Interface
st.title("🤖 ChatGPT - Custom UI")
st.markdown("Talk to OpenAI's ChatGPT with a fully configurable UI.")

user_message = st.text_area(
    "🗨️ Your Message", placeholder="Type your question here...", height=100
)

if st.button("🚀 Send"):
    if not api_key:
        st.error("⚠️ Please provide a valid OpenAI API Key!")
    else:
        try:
            client = openai.OpenAI(api_key=api_key)

            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_message},
                ],
                temperature=temperature,
                max_tokens=max_tokens,
                top_p=top_p,
                frequency_penalty=frequency_penalty,
                presence_penalty=presence_penalty,
            )

            st.success("✅ Response:")
            st.write(response.choices[0].message.content)

        except Exception as e:
            st.error(f"⚠️ OpenAI API Error: {str(e)}")
