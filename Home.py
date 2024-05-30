import streamlit as st


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
  
st.title(":blue[Project: Dự đoán bệnh viêm gan C] ")