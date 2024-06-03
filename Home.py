import os
import streamlit as st
from streamlit_chat import message
import google.generativeai as genai

# Google AI API Key configuration
api_key = "AIzaSyCY3PsLzWeM9gUa807ypz5atI4GMO6cjGc"
genai.configure(api_key=api_key)

# Create the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}
safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
]

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    safety_settings=safety_settings,
    generation_config=generation_config,
)

# Sidebar Navigation
with st.sidebar:
    st.header('Outline')

    if st.button('Problems'):
        st.experimental_set_query_params(page='Problems')
    if st.button('About Data'):
        st.experimental_set_query_params(page='AboutData')
    if st.button('Data Analysis'):
        st.experimental_set_query_params(page='AnalysData')
    if st.button('Test Your Health'):
        st.experimental_set_query_params(page='TestYourHealth')
    if st.button('Chatbot'):
        st.experimental_set_query_params(page='Chatbot')

# Determine which page to show
query_params = st.experimental_get_query_params()
page = query_params.get('page', [''])[0]

if page == 'Problems':
    st.title("Problems")
    exec(open("pages/Problems.py").read())
elif page == 'AboutData':
    st.title("About Data")
    exec(open("pages/AboutData.py").read())
elif page == 'AnalysData':
    st.title("Data Analysis")
    exec(open("pages/AnalysData.py").read())
elif page == 'TestYourHealth':
    st.title("Test Your Health")
    exec(open("pages/TestYourHealth.py").read())
elif page == 'Chatbot':
    st.title("Chatbot hỗ trợ")
    
    # Chatbot functionality
    if 'messages' not in st.session_state:
        st.session_state.messages = []

    user_input = st.text_input("Bạn:", key="input")

    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})

        # Get response from Google Generative AI
        chat_session = model.start_chat(history=[])
        response = chat_session.send_message(f"{user_input}")
        
        st.session_state.messages.append({"role": "bot", "content": response.text})

    for msg in st.session_state.messages:
        message(msg['content'], is_user=msg['role'] == 'user')

else:
    st.title(":blue[Project: Dự đoán bệnh viêm gan C]")
