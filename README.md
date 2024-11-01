# Google_Gemini_Demo

Trying LLM demo

1) Invoice_Extractor - 
   This model takes image of invoice and extracts answers to our queries related to that invoice from the image.
   
2) Text_to_SQL - 
   This model connects to SQL database and performs queries on the database as per our instructions. It converts our instructions into SQL queries and extracts the information.
   
   This is a very small database of just 5 entries with columns NAME, SECTION, CLASS AND MARKS. This was done just as a demo the process of running the model, creating streamlit app and deploying it on hugginface.

   HuggingFace: https://huggingface.co/wram1708

   Sample Query: tell me class category and provide class as if marks greater than 90 'first class', marks less than equal to 90 and greater than 80 'second class' else 'third class', only provide name and class,      order according to marks.
