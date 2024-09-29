import streamlit as st
import os #picking up env vars
from PIL import Image
import google.generativeai as genai


genai.configure(api_key="AIzaSyBU03LKzNI6HwsD5SDe5FFZwOB8MdET264") #config.


#function to load gemini pro vision
model=genai.GenerativeModel('gemini-1.5-flash')
def get_gemini_response(Input,Image,prompt):
    response=model.generate_content((Input,Image[0],prompt))
    return response.text
def input_image_details(uploaded_file):
    if uploaded_file is not None:
        bytes_data=uploaded_file.getvalue()
        image_parts=[
            {
                "mime_type":uploaded_file.type,
                "data":bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("no file uploaded")
    
st.set_page_config(page_title="Parin's Invoice Generator")
st.sidebar.header("RoboBill")
st.sidebar.write("Made by Parin")
st.header("RoboBill")
st.subheader("Made by Parin")
st.subheader("Manage Your Expenses with RoboBill")
input = st.text_input("What do you want to do?",key="input")
uploaded_file = st.file_uploader("Choose an image",type=['jpg','jpeg','png'])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image,caption="Uploaded Image",use_column_width=True)

ssubmit = st.button("Let's Go!")

input_prompt = """
You are an expert in calculus i will upload an image with a calculus question,solve it and give me the steps
At the end, make sure to repeat the name of our app "RoboBill 🦾" and ask the user to use it again.
"""

if ssubmit:
    image_data = input_image_details(uploaded_file)
    response=get_gemini_response(input_prompt,image_data,input)
    st.subheader("Here's what you need to know:")
    st.write(response)
