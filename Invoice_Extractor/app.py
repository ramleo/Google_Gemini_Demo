## Invoice Extractor

import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
from PIL import Image

##initialize our streamlit app
st.set_page_config(page_title="Gemini Image Demo")

load_dotenv() # Load all environment variables from .env

## Configure api key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


## Function to load gemini-1.5-pro vision model and get response
def get_gemini_response(input, image, prompt):
  # Load gemini model
  model = genai.GenerativeModel("gemini-1.5-pro")

  response = model.generate_content([input, image[0], prompt])

  return response


def input_image_setup(file):
  if file is not None:
    # Read the file into bytes
    bytes_data = file.getvalue()

    image_parts = [
      {
        "mime_type": file.type, # Get mime type of the file
        "data": bytes_data
      }
    ]
    return image_parts

  else:
    raise FileNotFoundError("No file uploaded.")




st.header("Gemini Application")
input=st.text_input("Input Prompt: ",key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)


submit=st.button("Tell me about the image")

input_prompt = """
               You are an expert in understanding invoices.
               You will receive input images as invoices &
               you will have to answer questions based on the input image
               """


## If ask button is clicked
if submit:
    image_data = input_image_setup(uploaded_file)
    response=get_gemini_response(input_prompt,image_data,input)
    extracted_text = response.candidates[0].content.parts[0].text+"\n"
    st.subheader("The Response is")
    st.write(extracted_text)


#===============================================================================================





