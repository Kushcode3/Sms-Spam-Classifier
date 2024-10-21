import streamlit as st
import pickle

#text_transformer = pickle.load(open('text_transformer.pkl','rb'))
#model = pickel.load(open('pipeline_rf_etc_bnb.pkl','rb'))

st.title("Email/SMS Spam Classifier")

#input_sms = st.text_area("Enter the message")

if st.button('Predict'):

    # 1. preprocess
    transformed_sms = text_transformer(input_sms)
    # 2. predict
    result = model.predict(vector_input)[0]
    # 3. Display
    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")







  
