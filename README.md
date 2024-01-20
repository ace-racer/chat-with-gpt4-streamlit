# chat-with-gpt4-streamlit
Chat with your GPT-4 model using OpenAI API via Streamlit web app using latest OAI and streamlit packages

# Main reference for codes:
- https://docs.streamlit.io/knowledge-base/tutorials/build-conversational-apps

## Starting the app

1. Set up OpenAI API key as a streamlit secret
Create .streamlit/secrets.toml file in our project directory and add the following lines to it:

#### .streamlit/secrets.toml
`OPENAI_API_KEY = "YOUR_API_KEY"`

2. Set up virtual environment using venv in Unix/macOS:
- `python -m venv .venv`
- `source .venv/bin/activate`
- `pip install -r requirements.txt`

3. Start the app:

1. Activate the virtual environment: `source .venv/bin/activate` (if not already activated)
2. `streamlit run main.py`
3. Navigate to `http://localhost:8501` where streamlit runs by default
4. Sample run of the app: ![App image](./docs/gpt4-streamlit-localhost.png)