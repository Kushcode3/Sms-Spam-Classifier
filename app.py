import streamlit as st
import pickle
import os
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import string
string.punctuation

def transform_text(text):
    text = re.sub('[^a-zA-Z]', ' ', text) # replacing all non-alphabetic characters with a space
    text = text.lower() # converting to lowecase
    text = nltk.word_tokenize(text) # to split a string into individual words (tokens)

    filtered_text = []
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation: # removal of stop words and punctuation
           filtered_text.append(ps.stem(i)) # Stemming

    return " ".join(filtered_text)
    
model = pickle.load(open('pipeline_rf_etc_bnb.pkl','rb'))


st.title("Email/SMS Spam Classifier")

input_sms = st.text_area("Enter the message")

if st.button('Predict'):
    if input_sms.strip():  # Check if the input is not empty or just whitespace
        # 1. Preprocess
        transformed_sms = transform_text(input_sms)
        # 2. Predict
        result = model.predict([transformed_sms])[0]  # Ensure input is in list format
        # 3. Display
        if result == 1:
            st.header("Spam")
        else:
            st.header("Not Spam")
    else:
        st.error("Please enter a message to classify.")




  
