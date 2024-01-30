import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
import joblib



# Datensatz importieren
df = pd.read_csv('C:\\Users\\tami9\\OneDrive\\Desktop\\Data Scienctist\\Projekt\\Sentimentanalyse\\tweets.csv', encoding='latin-1')
df = df[['target', 'text']]


# Verteilung der Sentimente
# sentiment_counts = df['target'].value_counts()
# print(sentiment_counts)


######---Textvorbereitung---######

# Wandle den gesamten Text in Kleinbuchstaben um
df['text_processed'] = df['text'].str.lower()

# Entferne Zeichen, die keine Buchstaben sind, und Zahlen.
df['text_processed'] = df['text_processed'].str.replace('[^a-zA-Z\s]', '', regex=True)

# Teile den Text in einzelne Wörter (Tokens) auf.
df['text_processed'] = df['text_processed'].apply(lambda x: word_tokenize(x))

# Lade NLTK-Ressourcen herunter
# nltk.download('stopwords')
# nltk.download('wordnet')

# Entferne Stoppwörtern wie "und", "ist", "der"
stop_words = set(stopwords.words('english'))  
df['text_processed'] = df['text_processed'].apply(lambda x: [word for word in x if word not in stop_words])

# Lemmatisierung: Reduziere Wörter auf ihre Grundform, um die Anzahl der eindeutigen Wörter zu reduzieren.
lemmatizer = WordNetLemmatizer()
df['text_processed'] = df['text_processed'].apply(lambda x: [lemmatizer.lemmatize(word) for word in x])

# Füge die Tokens wieder zu Sätze zusammen
df['text_processed'] = df['text_processed'].apply(lambda x: ' '.join(x))



######---Sentimentanalyse mit einem Naive Bayes-Modell---######

# Aufteilen der Daten in Trainings- und Testdaten
train_data, test_data, train_labels, test_labels = train_test_split(df['text_processed'], df['target'], test_size=0.2, random_state=42)

# Vektorisierung der Textdaten: Umwandeln der Textdaten in numerische Vektoren, damit sie vom Modell verarbeitet werden können
tfidf_vectorizer = TfidfVectorizer()
X_train = tfidf_vectorizer.fit_transform(train_data)
X_test = tfidf_vectorizer.transform(test_data)

# Training des Modells
model = MultinomialNB()
model.fit(X_train, train_labels)

# Auswertung der Leistung des Modells
predictions = model.predict(X_test)
accuracy = accuracy_score(test_labels, predictions)
print(f"Genauigkeit des Modells: {accuracy}")
print("Klassifikationsbericht:\n", classification_report(test_labels, predictions))
print("\n\n")


# Test Anwendung Modell / Textvektorisierung 
example_data = tfidf_vectorizer.transform(["A new great tweet.", "Another stupid tweet."])
exd_predictions = model.predict(example_data)
print(exd_predictions)


# Modell & TF-IDF-Vektorisierer speichern
joblib.dump(tfidf_vectorizer, 'tfidf_vectorizer.pkl')
joblib.dump(model, 'sentimentanalyse_model.pkl')



######---Gespeichertes Model laden---######

# import joblib
# from sklearn.feature_extraction.text import TfidfVectorizer

# senti_model = joblib.load('sentimentsanalyse_model.pkl')

# Lade auch den gespeicherten TF-IDF-Vektorisierer
# tfidf_vectorizer = joblib.load('tfidf_vectorizer.pkl')

# Test Anwendung des geladenen Modells
# test_data = tfidf_vectorizer.transform(["A new wonderful day.", "Bad day."])
# exd_predictions = senti_model.predict(test_data)
# print(exd_predictions)
