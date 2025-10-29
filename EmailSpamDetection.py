import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import streamlit as st

#Cleaning and Preparing Data
data = pd.read_csv("D:\Projects\Email Spam Detection\spam.csv")
data = data.drop_duplicates()
data['Category'] = data['Category'].replace(['ham','spam'],['Not Spam','Spam'])

message = data['Message']
category = data['Category']
(message_train,message_test,category_train,category_test) = train_test_split(message, category, test_size=0.2)

cv = CountVectorizer(stop_words='english')
message_train = cv.fit_transform(message_train)


#Creating Model
model = MultinomialNB()
model.fit(message_train,category_train)

#Model Testing
message_test = cv.transform(message_test)

# Predicting Model

def predict(message):
    input_message = cv.transform([message]).toarray()
    result = model.predict(input_message)
    return result


st.header('Email Spam Detection')
input_mess = st.text_input('Enter Email Here')

if st.button('Check'):
    if input_mess.strip() != "":
        output_mess = predict(input_mess)[0]
        if output_mess == "Spam":
            st.error(f"Prediction: {output_mess}") 
        else:
            st.success(f"Prediction: {output_mess}")
    else:
        st.warning("Please enter a message to check!")

