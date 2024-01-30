import streamlit as st

# Text auf Startseite
def show_start_page():
    st.markdown("<h1 class='title-text'>Hello Sentiment Analyzer 😀☹️</h1>", unsafe_allow_html=True)
    st.markdown("---")  
    st.write("""
             Herzlich willkommen beim Sentiment Analyzer! 
             \nMit dieser Anwendung kannst du die Stimmung (Sentiment) von Beiträgen analysieren. Dafür bietet dieses Tool dir zwei spannende Funktionen:
             \n1. **Analyse eigener Daten**: Hier kannst du deine eigenen Textdateien hochladen und analysieren lassen. Finde heraus, welche Stimmungen in deinen Texten vorherrschen, ob sie nun aus Social Media, Feedbacks oder anderen Quellen stammen.
             \n2. **Reddit-Recherche & Analyse**: Entdecke, was die Reddit-Community über verschiedene Themen denkt. Du kannst nach Beiträgen zu einem bestimmten Thema suchen oder die Beiträge eines bestimmten Users oder Unternehmens analysieren lassen.
             \nDie Anwendung basiert auf einem Machine Learning-Modell, das mit dem Sentiment140 Twitter-Datensatz trainiert wurde. Auf Basis dessen hat das Modell eine Analysegenauigkeit von 76,37%. 
             \nOb du nun Trends erkunden, Meinungen analysieren oder einfach nur neugierig bist – hier kannst du die Welt der Sentimentanalyse erkunden.
             \nViel Spaß beim Entdecken der Stimmungen! :)
             """)
    st.markdown("---")
    
    
