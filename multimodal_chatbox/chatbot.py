from dotenv import load_dotenv 
import streamlit as st
from langchain_openai import ChatOpenAI

# Load environment variables from .env
load_dotenv()

# Streamlit page setup
st.set_page_config(
    page_title="Multi-Model Chatbot",
    page_icon="🦁",
    layout="centered",
)
st.title("💬 Multi-Model Generative AI Chatbot")

# Model selection in sidebar
st.sidebar.title("⚙️ Model Settings")
selected_model = st.sidebar.selectbox(
    "Choose LLM Model:",
    options=[
        "openai.gpt-4o",
        "openai.gpt-3.5-turbo",
        "anthropic.claude-sonnet-5",
        "anthropic.claude-haiku-4-5-20251001-v1:0",
        "gemini-3.5-flash"
    ],
    index=0
)
st.sidebar.caption(f"Currently active: `{selected_model}`")

# Initiate chat history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Show previous chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Initiate LLM with selected model
llm = ChatOpenAI(
    base_url="https://openai.generative.engine.capgemini.com/v1",
    model=selected_model,
    temperature=0.7
)

# User input box
user_prompt = st.chat_input("Ask Chatbot...")

if user_prompt:
    # Display user message immediately
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role": "user", "content": user_prompt})

    ## this system prompt is not shown to the user its only added to the list so that the model can understand the context
    ## done by unpacking the history and creating a new list by adding the first message
    response = llm.invoke(
        input = [{"role": "system", "content": "You are a helpful assistant"}, *st.session_state.chat_history]
    )
    assistant_response = response.content

    # Save to history & render assistant message
    st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})
    
    with st.chat_message("assistant"):
        st.markdown(assistant_response)
