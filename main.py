from openai import OpenAI
import streamlit as st
from configs import OAI_MODEL
from utils import export_current_conversation, num_tokens_from_messages

st.title("Chat with GPT-4 using Streamlit")

# Create a button
export_button = st.button("Export")

if export_button:
    export_current_conversation(st.session_state.messages)

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = OAI_MODEL

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        for response in client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        ):
            full_response += (response.choices[0].delta.content or "")
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})

# Use st.markdown with inline HTML styling to change text color
st.markdown(f"<span style='color:red'>Total tokens used (input+output): {num_tokens_from_messages(st.session_state.messages, OAI_MODEL)}</span>", unsafe_allow_html=True)
