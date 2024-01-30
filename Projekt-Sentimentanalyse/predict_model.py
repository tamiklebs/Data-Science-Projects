import joblib
import streamlit as st

# Funktion zum Laden des Modells und des Vektorisierers
@st.cache_resource
def load_model_and_vectorizer():
    tfidf_vectorizer = joblib.load('tfidf_vectorizer.pkl')
    model = joblib.load('sentimentanalyse_model.pkl')
    return model, tfidf_vectorizer

# Funktion zur Vorhersage des Sentiments eines Textes
def predict_sentiment(text):
    model, tfidf_vectorizer = load_model_and_vectorizer()
    processed_text = tfidf_vectorizer.transform([text])
     
    prediction = model.predict(processed_text)
   
    return prediction[0]



# Beispielaufruf der Funktion
# prediction = predict_sentiment("A new wonderful day.")
# print("Vorhersage: ", prediction)