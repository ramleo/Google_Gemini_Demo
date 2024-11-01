# SQL Coder

import os
import sqlite3
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

##initialize our streamlit app
st.set_page_config(page_title="Retrieve SQL Query")

load_dotenv() # Load all environment variables from .env

## Configure api key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load gemini-1.5-flash-8b model and provide querries as  response
def get_gemini_response(question, prompt):
  # Load gemini model
  model = genai.GenerativeModel("gemini-1.5-flash-8b")

  response = model.generate_content([prompt[0], question])

  return response

## Function to retrieve query from the database
def read_sql_query(sql, db):
  conn = sqlite3.connect(db)
  cur = conn.cursor()
  cur.execute(sql)
  rows = cur.fetchall()

  conn.commit()
  conn.close()

  # for row in rows:
  #   print(row)

  return rows

## Define prompt
prompt = [
  """
  You are an expert in converting English questions to SQL query! The SQL database has the name STUDENT and has the following columns - NAME, CLASS, SECTION, MARKS \n\nFor example,\nExample 1 - How many entries of records are present?, the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ; \nExample 2 - Tell me all the students studying in Data Science class?, the SQL command will be something like this SELECT * FROM STUDENT where CLASS="Data Science"; also the sql code should not have ``` in beginning or end and sql word in output
  """
]

st.header("Gemini App to retrieve sql query")

question = st.text_input("Input: ", key="input")

submit = st.button("Ask the question")

# If submit is clicked
if submit:
  output = get_gemini_response(question, prompt)
  # print(output)
  extracted_text = output.candidates[0].content.parts[0].text
  print(extracted_text)
  response = read_sql_query(extracted_text, "student.db")
  # print(response)
  st.subheader("The Response is")
  for row in response:
    print(row)
    st.header(row)