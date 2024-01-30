import streamlit as st
import pandas as pd 
import api  
from predict_model import predict_sentiment
import start
from io import StringIO



# Setze Grundkonfiguration der Seite
st.set_page_config(
    page_title="Sentiment Analyzer 😀☹️",
    page_icon="🔍")


custom_css = """
    <style>
        /* Main background color */
        .reportview-container {
            background: #111111;
        }
        /* Text color */
        body {
            color: #ffffff;
        }
        /* Sidebar background color */
        .sidebar .sidebar-content {
            background: #222222;
        }
        /* Title text color */
        h1 {
            color: #f40076;
        }
        /* Sidebar title text color */
        .sidebar h2 {
            color: #f40076;
        }
    </style>
"""

# Erlaube das Einbetten von HTML
st.markdown(custom_css, unsafe_allow_html=True)

# Initialisiere Zustände im session_state, falls noch nicht gesetzt
if 'current_page' not in st.session_state:
    st.session_state.current_page = None
if 'analysis_done' not in st.session_state:
    st.session_state['analysis_done'] = False
if 'details_shown' not in st.session_state:
    st.session_state['details_shown'] = False
if 'sentiments' not in st.session_state:
    st.session_state['sentiments'] = None
if 'text_lines' not in st.session_state:
    st.session_state['text_lines'] = []
if 'show_details_import' not in st.session_state:
    st.session_state['show_details_import'] = False 
if 'current_search_mode' not in st.session_state:
    st.session_state.current_search_mode = None
    
    
# Sidebar für Eingabewidgets
with st.sidebar:
    st.title("Navigationsmenü")
    page = st.radio("Bitte wähle eine Option:", ['Startseite', 'Datenimport & Analyse', 'Reddit-Recherche & Analyse'])
    if page != st.session_state.current_page:
        st.session_state.current_page = page
        st.session_state['start_analysis'] = False
        st.session_state['show_details'] = False
        st.session_state['current_search_mode'] = None
    thema = ""
    username = ""
    # Bedingungen für die Anzeige von Seiten-spezifischen Optionen
    if page == 'Reddit-Recherche & Analyse':
        st.markdown("---")
        # Optionen für die Suche
        suchmodus = st.radio("Suche nach:", ['Thema/Schlüsselwort', 'User/Unternehmen'])
        # Überprüfe, ob sich der Suchmodus geändert hat und setze den Status zurück
        if suchmodus != st.session_state.current_search_mode:
            st.session_state.current_search_mode = suchmodus
            st.session_state['start_analysis'] = False  
            st.session_state['show_details'] = False
        if suchmodus == 'Thema/Schlüsselwort':
            thema = st.text_input("Thema oder Schlüsselwort eingeben:")
            # Optionen für den Suchbereich, wenn nach einem Thema gesucht wird
            suche_in = st.radio("Suche in:", ['Ganz Reddit', 'Bestimmtes Subreddit'])
            # Auswahl aus den meist genutzten Subreddits
            if suche_in == 'Bestimmtes Subreddit':
                subreddit = st.selectbox("Wähle ein Subreddit:", ["news", "gaming", "technology", "politics", "comedyheaven", "science", "askreddit", "relationships", "getmotivated"])
            else:
                subreddit = 'all'
        else:
            username = st.text_input("User- oder Unternehmensname eingeben:")
            user_thema_option = st.checkbox("Nach einem spezifischen Thema in den Beiträgen suchen?")
            user_thema = ""
            if user_thema_option:
                user_thema = st.text_input("Thema oder Schlüsselwort in den Beiträgen:")
            # Optionen für den Suchbereich, wenn nach einem User gesucht wird
            user_suche_in = st.radio("Suche in:", ['Ganz Reddit', 'Bestimmtes Subreddit'])
            if user_suche_in == 'Bestimmtes Subreddit':
                subreddit = st.selectbox("Wähle ein Subreddit für die Usersuche:", ["news", "gaming", "technology", "politics", "comedyheaven", "science", "askreddit", "relationships", "getmotivated"])
            else:
                subreddit = 'all'
                
                
        include_text_only = st.checkbox("Nur Beiträge mit Textinhalt in die Analyse einbeziehen")
        limit = st.number_input("Anzahl der Beiträge, die max. analysiert werden sollen:", min_value=1, max_value=100, value=25)
        start_analysis = st.button("Sentimentanalyse starten")



######---Hauptinhalt der App basierend auf der Auswahl im Seitenbereich---######
# 1. Startseite
if st.session_state.current_page == 'Startseite':
    start.show_start_page()

# 2. Datenimport & Analyse
elif st.session_state.current_page == 'Datenimport & Analyse':
    st.markdown("<h1 class='title-text'>Eigene Daten analysieren</h1>", unsafe_allow_html=True)
    st.markdown("---")


    # Info zum Dateiformat in der Sidebar
    st.sidebar.markdown("---")
    st.sidebar.write("Die hochgeladene Datei sollte im TXT- oder CSV-Format vorliegen und pro Zeile einen zu analysierenden Beitrag enthalten.")
    st.sidebar.markdown("---")
        
    # Dateiupload in der Sidebar 
    uploaded_file = st.sidebar.file_uploader("Lade eine Datei hoch", type=["txt", "csv"])

    start_analysis_import = st.sidebar.button("Starte Sentimentanalyse")

    # Button zum Starten der Analyse im Seitenmenü
    if start_analysis_import:
        if uploaded_file is None:
            st.error("Bitte lade erst eine Datei hoch.")
        else:
            st.write(f"🔍  Analysiere Sentimente... 😀☹️")
            # Konvertieren der hochgeladenen Datei in einen String
            stringio = StringIO(uploaded_file.getvalue().decode("latin-1"))
            text_lines = stringio.getvalue().splitlines()

            sentiments = {'Positive': 0, 'Negative': 0}
            for line in text_lines:
                if line.strip():
                    sentiment = predict_sentiment(line)
                    if sentiment == 4:
                        sentiments['Positive'] += 1
                    elif sentiment == 0:
                        sentiments['Negative'] += 1

            # Speichern der Analyseergebnisse und der Zeilen im session_state
            st.session_state['sentiments_import'] = sentiments
            st.session_state['text_lines_import'] = text_lines
     
            
            
    # Anzeigen der Ergebnisse, wenn die Analyse durchgeführt wurde
    if 'sentiments_import' in st.session_state and 'text_lines_import' in st.session_state:
        st.write(f"✅ Analyse der Beiträge abgeschlossen")
        st.markdown("---")
        
        # Bestimme das häufigere Sentiment
        total_lines = len(st.session_state['text_lines_import'])
        percent_positive = (st.session_state['sentiments_import']['Positive'] / total_lines) * 100
        percent_negative = (st.session_state['sentiments_import']['Negative'] / total_lines) * 100
        
        if percent_positive > percent_negative:
            sentiment_result = "positiv"
            color = "green"
        elif percent_negative > percent_positive:
            sentiment_result = "negativ"
            color = "red"
        else:
            sentiment_result = "neutral"
            color = "yellow"
        
        # Anzeige des dominanten Sentiments
        if sentiment_result != "neutral":
            st.markdown(f"<p style='font-size: 22px; text-align: center;'>Die Sentimentanalyse der importierten Beiträge ergibt:</p>", unsafe_allow_html=True)
            st.markdown(f"<div style='background-color: #31333F; border: 2px solid black; padding: 10px; text-align: center;'>", unsafe_allow_html=True)
            st.markdown(f"<p style='font-size: 44px; color: {color}; text-align: center;'>{percent_positive if sentiment_result == 'positiv' else percent_negative:.1f}%</p>", unsafe_allow_html=True)
            st.markdown(f"<p style='font-size: 18px; text-align: center;'>der analysierten Beiträge sind </p>", unsafe_allow_html=True)
            st.markdown(f"<p style='font-size: 44px; color: {color}; text-align: center;'>{sentiment_result}</p>", unsafe_allow_html=True)
            st.markdown(f"<div style='background-color: #31333F; border: 2px solid black; padding: 10px; text-align: center;'>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
        
        else:
            st.markdown(f"<p style='font-size: 22px; text-align: center;'>Die Sentimentanalyse der importierten Beiträge ergibt:</p>", unsafe_allow_html=True)
            st.markdown(f"<div style='background-color: #31333F; border: 2px solid black; padding: 10px; text-align: center;'>", unsafe_allow_html=True)
            st.markdown(f"<p style='font-size: 44px; color: {color}; text-align: center;'>Die Ergebnisse sind neutral</p>", unsafe_allow_html=True)
            st.markdown(f"<div style='background-color: #31333F; border: 2px solid black; padding: 10px; text-align: center;'>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
            
        st.markdown("---")
        st.write(f"Anzahl positiver Sentiments: {st.session_state['sentiments_import']['Positive']}")
        st.write(f"Anzahl negativer Sentiments: {st.session_state['sentiments_import']['Negative']}")
        
        # Button und Anzeige der Details
        if st.button("Zeige Details zur Analyse", key="button_details_import"):
            st.session_state['show_details_import'] = not st.session_state['show_details_import']
        
        if st.session_state['show_details_import']:
            details = []
            for line in st.session_state['text_lines_import']:
                if line.strip():
                    sentiment = predict_sentiment(line)
                    details.append({'Text': line, 'Sentiment': '😀 Positiv' if sentiment == 4 else '☹️ Negativ'})
            
            # Erstelle DataFrame aus den Details
            df_details = pd.DataFrame(details)
            
            # Setze die Indizierung des DataFrames, sodass sie bei 1 beginnt
            df_details.index = df_details.index + 1
            
            # Zeige die Tabelle in Streamlit an
            st.dataframe(df_details)
        




# 3. Reddit-Recherche & Analyse     
elif st.session_state.current_page == 'Reddit-Recherche & Analyse':
    st.markdown("<h1 class='title-text'>Sentimentanalyse von Reddit-Beiträgen</h1>", unsafe_allow_html=True)
    st.markdown("---")
    

    # Button zur Auslösung der Sentimentanalyse
    if start_analysis:
        if suchmodus == 'User/Unternehmen' and not username.strip():
            st.error("Bitte gebe einen User- oder Unternehmensnamen ein.")
        else:
            st.session_state['start_analysis'] = True
            
                
    if st.session_state.get('start_analysis', False):
    
        # Abrufen von Posts basierend auf dem ausgewählten Suchmodus
        if suchmodus == 'Thema/Schlüsselwort' and suche_in == 'Bestimmtes Subreddit':
            st.write(f"🔍  Suche nach Beiträgen zum Thema '{thema}' im Subreddit '{subreddit}' und analysiere Sentimente... 😀☹️")
           
        elif suchmodus == 'Thema/Schlüsselwort' and suche_in == 'Ganz Reddit':
            st.write(f"🔍  Suche nach Beiträgen zum Thema '{thema}' und analysiere Sentimente... 😀☹️")
                
        elif suchmodus == 'User/Unternehmen' and user_suche_in == 'Ganz Reddit':
            st.write(f"🔍  Suche nach Beiträgen des Users '{username}' und analysiere Sentimente... 😀☹️")
                
        elif suchmodus == 'User/Unternehmen' and user_suche_in == 'Bestimmtes Subreddit':
            st.write(f"🔍  Suche nach Beiträgen des Users '{username}' auf der Userseite und analysiere Sentimente... 😀☹️")
    
        
        # Setze extended_limit basierend auf include_text_only
        extended_limit = 500 if include_text_only else limit
            
            
        # Abrufen von Posts basierend auf dem ausgewählten Suchmodus
        if suchmodus == 'Thema/Schlüsselwort':
            if suche_in == 'Bestimmtes Subreddit':
                posts = api.get_last_posts_by_topic_sub(subreddit, thema, extended_limit)
            else:
                posts = api.get_last_posts_by_topic_all(thema, extended_limit)
        else:
            if user_thema_option and user_suche_in != 'Nur User/Unternehmensseite':
                posts = api.get_last_posts_by_user_topic(username, user_thema, extended_limit)
            elif user_suche_in == 'Nur User/Unternehmensseite':
                posts = api.get_last_posts_by_user_on_profile(username, extended_limit)
            elif user_suche_in == 'Bestimmtes Subreddit':
                posts = api.get_last_posts_by_user_in_sub(username, subreddit, extended_limit)
            else:
                if username.strip():  # Hier prüfen, ob ein gültiger Benutzername eingegeben wurde
                    posts = api.get_last_posts_by_user(username, extended_limit)
                else:
                    st.error("Bitte geben Sie einen gültigen User- oder Unternehmensnamen ein.")
                    posts = []
                    
                 
    
        # Filtere Posts mit Textinhalt, falls gewünscht
        if include_text_only:
            posts = [post for post in posts if post['text'].strip()]
    
        # Begrenze die Posts auf die ursprünglich gewünschte Anzahl
        posts = posts[:limit]
    
        
        # Initialisiere das Dictionary für Sentiments
        sentiments = {4: 0, 0: 0}
        
        # Fülle das Dictionary basierend auf den Sentiment-Werten der Posts
        for post in posts:
            sentiment = predict_sentiment(post['text'])
            if sentiment in sentiments:
                sentiments[sentiment] += 1
                
                
        st.write(f"✅ Analyse der Beiträge abgeschlossen")
        st.markdown("---")
        total_posts = len(posts)
        if total_posts > 0:
            # Berechne Prozentsätze
            percent_positive = (sentiments[4] / total_posts) * 100
            percent_negative = (sentiments[0] / total_posts) * 100
                
            # Bestimme das Sentiment basierend auf den Prozentsätzen
            if percent_positive > percent_negative:
                sentiment_result = "positiv"
                color = "green"
                display_percent = percent_positive
            elif percent_negative > percent_positive:
                sentiment_result = "negativ"
                color = "red"
                display_percent = percent_negative
            else:
                sentiment_result = "neutral"
                color = "yellow"
                display_percent = percent_positive

            # Anzeige des Ergebnisses
            if sentiment_result == "neutral":
                if thema:
                    st.markdown(f"<p style='font-size: 22px; text-align: center;'>Die Sentimentanalyse von {total_posts} Beiträgen zum Thema '{thema}' ergibt:</p>", unsafe_allow_html=True)
                elif username:
                    st.markdown(f"<p style='font-size: 22px; text-align: center;'>Die Sentimentanalyse von {total_posts} Beiträgen des Users '{username}' ergibt:</p>", unsafe_allow_html=True)
               
                st.markdown(f"<div style='background-color: #31333F; border: 2px solid black; padding: 10px; text-align: center;'>", unsafe_allow_html=True)
                st.markdown(f"<p style='font-size: 44px; color: {color}; text-align: center;'>{display_percent:.1f}%</p>", unsafe_allow_html=True)
                st.markdown(f"<p style='font-size: 18px; text-align: center;'>der analysierten Beiträge sind positiv. </p>", unsafe_allow_html=True)
                st.markdown(f"<p style='font-size: 18px; text-align: center;'>Das Ergebnis ist </p>", unsafe_allow_html=True)

                st.markdown(f"<p style='font-size: 44px; color: {color}; text-align: center;'>{sentiment_result}</p>", unsafe_allow_html=True)
                st.markdown(f"<div style='background-color: #31333F; border: 2px solid black; padding: 10px; text-align: center;'>", unsafe_allow_html=True)
                st.markdown("</div>", unsafe_allow_html=True)
                    
            else:
                if thema:
                    st.markdown(f"<p style='font-size: 22px; text-align: center;'>Die Sentimentanalyse von {total_posts} Beiträgen zum Thema '{thema}' ergibt:</p>", unsafe_allow_html=True)
                elif username:
                    st.markdown(f"<p style='font-size: 22px; text-align: center;'>Die Sentimentanalyse von {total_posts} Beiträgen des Users '{username}' ergibt:</p>", unsafe_allow_html=True)
                   
                st.markdown(f"<div style='background-color: #31333F; border: 2px solid black; padding: 10px; text-align: center;'>", unsafe_allow_html=True)
                st.markdown(f"<p style='font-size: 44px; color: {color}; text-align: center;'>{display_percent:.1f}%</p>", unsafe_allow_html=True)
                st.markdown(f"<p style='font-size: 18px; text-align: center;'>der analysierten Beiträge sind</p>", unsafe_allow_html=True)
                st.markdown(f"<p style='font-size: 44px; color: {color}; text-align: center;'>{sentiment_result}</p>", unsafe_allow_html=True)
                st.markdown(f"<div style='background-color: #31333F; border: 2px solid black; padding: 10px; text-align: center;'>", unsafe_allow_html=True)
    
                st.markdown("</div>", unsafe_allow_html=True)
                st.markdown("---")
                
            
   
           
        else:
           st.markdown("Keine Posts gefunden. Bitte überprüfe deine Eingaben.")
           st.markdown("---")


        # Button zum Anzeigen der Details
        if st.button("Zeige Details zu den Beiträgen"):
            st.session_state['show_details'] = not st.session_state.get('show_details', False)


        # Zeige Details der Posts, basierend auf dem Zustand
        if st.session_state.get('show_details', False):
            post_data = []
        
            for post in posts:
                sentiment = predict_sentiment(post['text'])
                # Füge entsprechende Emojis zum Sentiment hinzu
                if sentiment == 4:
                    sentiment_text = '😀 Positiv'
                else:
                    sentiment_text = '☹️ Negativ'
        
                # Füge Post-Informationen zum post_data hinzu
                post_data.append({
                    'Titel': post['title'],
                    'Text': post['text'],
                    'Sentiment': sentiment_text
                })
        
            # Erstelle DataFrame aus der Liste post_data
            df = pd.DataFrame(post_data)
        
            # Setze die Indizierung des DataFrames, sodass sie bei 1 beginnt
            df.index = df.index + 1
        
            # Zeige die Tabelle in Streamlit an
            st.dataframe(df)  
            
    

    
    
