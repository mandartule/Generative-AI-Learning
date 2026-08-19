from dotenv import load_dotenv 
import streamlit as st
from langchain_openai import ChatOpenAI

# Load environment variables from .env
load_dotenv()

# Streamlit page setup
st.set_page_config(
    page_title="Chatbot",
    page_icon="🦁",
    layout="centered",
)
st.title("💬 Generative AI Chatbot")

st.sidebar.markdown("👨‍💻 **Made by Mandar**")

# Initiate chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Show chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# LLM initiate
llm = ChatOpenAI(
    base_url="https://openai.generative.engine.capgemini.com/v1",
    model="openai.gpt-4o",  # or "anthropic.claude-haiku-4-5-20251001-v1:0"
    temperature=1
)

# Input box
user_prompt = st.chat_input("Ask Chatbot...")

if user_prompt:
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role": "user", "content": user_prompt})

    ## this system prompt is not shown to the user its only added to the list so that the model can understand the context
    ## done by unpacking the history and creating a new list by adding the first message
    response = llm.invoke(
        input = [{"role": "system", "content": "You are a helpful assistant"}, *st.session_state.chat_history]
    )
    assistant_response = response.content
    st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})

    with st.chat_message("assistant"):
        st.markdown(assistant_response)
