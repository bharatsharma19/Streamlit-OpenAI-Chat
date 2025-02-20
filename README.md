# Streamlit Chatbot UI

## Overview
This project provides a sleek UI for interacting with OpenAI's GPT models using [Streamlit](https://streamlit.io/). Users can dynamically configure all OpenAI parameters via the frontend for a customizable chatbot experience.

## Features
- Selectable OpenAI model (GPT-4, GPT-3.5-turbo, etc.)
- Adjustable parameters: temperature, max tokens, etc.
- Streamed responses for real-time interaction
- User-friendly and interactive UI powered by Streamlit

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/bharatsharma19/Streamlit-OpenAI-Chat.git
   cd Streamlit-OpenAI-Chat/
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
   
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Setup
1. Create a `.env` file and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key
   ```

## Running the Application
To start the Streamlit app, run:
```bash
streamlit run main.py
```
This will launch the chatbot UI in your browser.

## Usage
- Enter a prompt in the input field.
- Choose the OpenAI model and adjust parameters.
- Click "Submit" to receive a streamed response.

## Deployment
To deploy this Streamlit app using Streamlit Cloud:
1. Push your code to a GitHub repository.
2. Connect your repository to Streamlit Cloud.
3. Deploy and enjoy your chatbot.

## License
This project is licensed under the MIT License.
