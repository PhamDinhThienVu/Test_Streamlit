import os
import streamlit as st
from streamlit_chat import message
import google.generativeai as genai

#Manage page link - nav bar to move on another pages

with st.sidebar:

  st.header('Outline', divider='rainbow')

  st.page_link(page = "pages/Problems.py", 
             label="Problems")

  st.page_link(page = "pages/AboutData.py", 
             label="About Data")

  st.page_link(page = "pages/AnalysData.py", 
             label="Data Analysis")
  
  st.page_link(page = "pages/TestYourHealth.py", 
             label="Test Your Health")
  

  
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




with st.container():
  st.title("Hỏi đáp về bệnh viêm gan C với chatbot AI")
    
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