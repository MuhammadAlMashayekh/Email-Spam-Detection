📧 Email Spam Detection using Machine Learning

This project is a simple Email Spam Detection app built with Python, scikit-learn, and Streamlit.
It uses a Naive Bayes classifier to predict whether an email message is Spam or Not Spam based on its text content.

🚀 Features

Detects if an email is Spam or Not Spam

Built using Natural Language Processing (NLP) techniques

Interactive Web App using Streamlit

Real-time prediction from user input

🧠 How It Works

Dataset Loading

The dataset (spam.csv) is loaded using pandas.

Duplicate rows are removed to ensure data quality.

Categories are renamed:

ham → Not Spam

spam → Spam

Data Preparation

The dataset is split into training and testing sets (80% train, 20% test).

CountVectorizer converts email text into numerical features using word frequency.

Model Training

A Multinomial Naive Bayes (MultinomialNB) model is trained on the vectorized training data.

Prediction

The predict() function takes user input, transforms it into a vector, and predicts if it’s Spam or Not Spam.

Streamlit Interface

Users can enter any email text into a text box.

Clicking "Check" runs the prediction.

Results appear in color:

🔴 Red (Spam)

🟢 Green (Not Spam)
