# 💬 Multi-Model Generative AI Chatbot

An interactive multi-model chatbot built with **Streamlit** and **LangChain**, connected through an **OpenAI-Compatible API Gateway**.

This application allows users to dynamically switch between leading LLMs from OpenAI, Anthropic, and Google on the fly while retaining conversation history.

---

## 🌟 Key Features

* **Dynamic Model Switching**: Select between multiple frontier foundation models from a single sidebar dropdown without restarting the app.
* **Unified OpenAI SDK Abstraction**: Uses `langchain-openai` as a single unified interface to communicate with OpenAI, Claude, and Gemini models via an OpenAI-compatible gateway.
* **Persistent Conversation History**: Full multi-turn chat memory managed in `st.session_state` so you can compare how different models respond to the same conversation thread.
* **Clean Streamlit UI**: Chat interface with user/assistant avatars, markdown rendering, and chat input.

---

## 🤖 Supported Models

| Provider | Model Identifier | Description |
| :--- | :--- | :--- |
| **OpenAI** | `openai.gpt-4o` | Flagship multimodal GPT-4o model |
| **OpenAI** | `openai.gpt-3.5-turbo` | Fast, lightweight GPT-3.5 model |
| **Anthropic** | `anthropic.claude-sonnet-5` | High-intelligence Claude Sonnet model |
| **Anthropic** | `anthropic.claude-haiku-4-5-20251001-v1:0` | Ultra-fast, cost-efficient Claude Haiku model |
| **Google** | `gemini-3.5-flash` | High-speed, high-reasoning Gemini model |

---

## 📁 Project Structure

```text
multimodal_chatbox/
├── chatbot.py          # Main Streamlit chatbot application
├── requirements.txt    # Python dependencies
├── .env                # API Key and environment configuration (do not commit)
└── README.md           # Documentation
```

---

## ⚙️ Setup & Installation

### 1. Configure Environment Variables
Create a `.env` file in this directory and add your API key:

```env
OPENAI_API_KEY=YOUR_API_KEY
```

---

### 2. Install Dependencies

Ensure your virtual environment is active, then run:

```bash
pip install -r requirements.txt
```

---

### 3. Run the Application

Start the Streamlit application:

```bash
streamlit run chatbot.py
```

The app will open automatically in your browser at `http://localhost:8501`.

---

## 💡 How It Works

1. **Model Selection**: Choose your desired model from the sidebar.
2. **Context Passing**: When a prompt is submitted, the conversation history is dynamically unpacked along with the system instruction:
   ```python
   input=[{"role": "system", "content": "You are a helpful assistant"}, *st.session_state.chat_history]
   ```
3. **Gateway Routing**: `ChatOpenAI` sends the standardized payload to the OpenAI-compatible gateway endpoint configured in `chatbot.py`, which routes the request to the respective provider model and returns the response.
