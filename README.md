📧 Email Spam Detection using Machine Learning

This project is a simple Email Spam Detection app built with Python, scikit-learn, and Streamlit.
It uses a Naive Bayes classifier to predict whether an email message is Spam or Not Spam based on its text content.

🚀 Features:
1- Detects if an email is Spam or Not Spam
2- Built using Natural Language Processing (NLP) techniques
3- Interactive Web App using Streamlit

🧠 How It Works:

A- Dataset Loading:
1- The dataset (spam.csv) is loaded using pandas.
2- Duplicate rows are removed to ensure data quality.
3- Categories are renamed:
  ham → Not Spam
  spam → Spam

B- Data Preparation: 
1- The dataset is split into training and testing sets (80% train, 20% test).
2- CountVectorizer converts email text into numerical features using word frequency.

C- Model Training:
A Multinomial Naive Bayes (MultinomialNB) model is trained on the vectorized training data.

D- Prediction:
The predict() function takes user input, transforms it into a vector, and predicts if it’s Spam or Not Spam.

E- Streamlit Interface:
1- Users can enter any email text into a text box.
2- Clicking "Check" runs the prediction.
3- Results appear in color:
  🔴 Red (Spam) — if the email is detected as spam.
  🟢 Green (Not Spam) — if the email is safe.
  🟡 Yellow (YELLOW) — if the input box is left empty.

Example Output:
| Input Message               | Result Shown    |
| --------------------------- | --------------- |
| "You won $500!"             | 🔴 **Spam**     |
| "Meeting at 10 AM tomorrow" | 🟢 **Not Spam** |
| *(blank input)*             | 🟡 **YELLOW**   |

