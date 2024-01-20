# chat-with-gpt4-streamlit
Chat with your GPT-4 model using OpenAI API via Streamlit web app using latest OAI and streamlit packages

# Main reference for Streamlit related code:
- https://docs.streamlit.io/knowledge-base/tutorials/build-conversational-apps

## Starting the app

1. Set up OpenAI API key as a streamlit secret
- Create `.streamlit/secrets.toml` file in the project directory and add the following lines to it:

`OPENAI_API_KEY = "YOUR_API_KEY"`

2. Set up virtual environment using venv in Unix/macOS:
- `python -m venv .venv`
- `source .venv/bin/activate`
- `pip install -r requirements.txt`

3. Start the app by following below steps:

- Activate the virtual environment: `source .venv/bin/activate` (if not already activated)
- `streamlit run main.py`
- Navigate to `http://localhost:8501` where streamlit runs by default
- Sample run of the app: ![App image](./docs/gpt4-streamlit-localhost.png)

4. More features of the chat app:

- Streaming generation of the response - No waiting!
- Export the current conversation to save on API calls - outputs are written in the project directory inside a folder called `exports`
    - A CSV file is created with the time stamp of the local time when the export button was clicked
    - Export button: ![Export button](./docs/export-conversation.png)
    - Exported content as a CSV file: ![Exported content](./docs/exported-conversation.png)


5. Advanced configurations:

- Adjust the name of the OpenAI text generation model used by changing the `OAI_MODEL` parameter in the `configs.py` file
List of all possible models from OpenAI [here](https://platform.openai.com/docs/models/gpt-4-and-gpt-4-turbo) and [here](https://platform.openai.com/docs/models/gpt-3-5)
- Adjust the location where the chat exports are saved by changing the `EXPORT_DIR` parameter in the `configs.py` file