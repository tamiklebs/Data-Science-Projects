import streamlit as st
import pandas as pd
import analysis
import visualize



# Fügen Sie das Bild oben im Seitenmenü ein
st.sidebar.image('https://seekvectorlogo.net/wp-content/uploads/2020/03/autoscout24-gmbh-vector-logo.png')


# Seitenmenü für die Navigation
menu = st.sidebar.selectbox('Menü', 
    ['Startseite', 
     'Analyse des Datensatzes', 
     'Visualisierung der Modellergebnisse', 
     'Autoverkaufspreis-Vorhersage'])

# Logik für das Seitenmenü
if menu == 'Startseite':
    st.title('Willkommen auf der Analyse- und Vorhersageplattform')
    st.markdown("<h3 style='color: yellow;'>AutoScout24-Datensatz</h3>", unsafe_allow_html=True)

    st.markdown("""
    Willkommen auf der interaktiven Analyse- und Vorhersageplattform für den AutoScout24-Datensatz. Diese Anwendung bietet Dir einen umfassenden Einblick in den Automobilmarkt.

    Unter **"Analyse des Datensatzes"** findest du eine detaillierte Untersuchung der AutoScout24-Daten. Hier kannst Du die meistverkauften Marken und Modelle entdecken, Korrelationen zwischen verschiedenen Merkmalen wie Preis, Leistung und Baujahr erkunden und vieles mehr.

    Im Bereich **"Visualisierung der Modellergebnisse"** werden die Ergebnisse der verschiedenen maschinellen Lernmodelle dargestellt.

    Anschließend kannst du unter dem Abschnitt **"Autoverkaufspreis-Vorhersage"** das trainierte Random Forest-Modell nutzen, um den Verkaufspreis eines Autos basierend auf spezifischen Merkmalen wie Laufleistung, Leistung und Baujahr vorherzusagen.

    Viel Spaß beim Erkunden! :)
    """)
    
    
elif menu == 'Analyse des Datensatzes':
    st.header('Analyse des Datensatzes')
    st.markdown("<h3 style='color: yellow;'>Details zu den bereinigten Daten</h3>", unsafe_allow_html=True)
    
    zeitraum, autos_verkauft = analysis.overview()
  
    # Formatiere die Anzahl verkaufter Autos
    autos_verkauft_formatted = f"<span style='font-weight: bold; color: yellow;'>{autos_verkauft:,}".replace(",", ".") + "</span>"
  
    # Formatiere den Zeitraum
    zeitraum_formatted = f"<span style='font-weight: bold; color: yellow;'>{zeitraum[0]} - {zeitraum[1]}</span>"
  
    st.markdown(f"<b>Anzahl verkaufter Autos:</b> {autos_verkauft_formatted}", unsafe_allow_html=True)
    st.markdown(f"<b>Zeitraum der Datenerfassung:</b>  {zeitraum_formatted}", unsafe_allow_html=True)
    
    # Top Marken Übersicht Checkbox
    show_marken = st.checkbox('Zeige eine Übersicht der meistverkauften Marken & Modelle')
    if show_marken:
        analysis.plot_top_makes()
        analysis.top_10_model()
    
    analysis.top_marken_avgprice()
    
    
    # Hinzufügen eines horizontalen Linien-Elements
    st.markdown("<hr>", unsafe_allow_html=True)
    
    st.markdown("<h3 style='color: yellow;'>Korrelationen zwischen den Merkmalen</h3>", unsafe_allow_html=True)
    
    # Informationen je verkauftem Auto
    st.markdown("<h5>Merkmale je Auto</h5>", unsafe_allow_html=True)

    
    # Liste der Features
    features = [
        {'Merkmal': 'Mileage', 'Beschreibung': 'Laufleistung in Kilometern'},
        {'Merkmal': 'Make', 'Beschreibung': 'Marke/Hersteller des Autos'},
        {'Merkmal': 'Model', 'Beschreibung': 'Modell des Autos'},
        {'Merkmal': 'Fuel', 'Beschreibung': 'Art des Kraftstoffs'},
        {'Merkmal': 'Gear', 'Beschreibung': 'Art des Getriebes'},
        {'Merkmal': 'Offer Type', 'Beschreibung': 'Art des Angebots'},
        {'Merkmal': 'Price', 'Beschreibung': 'Verkaufspreis in Euro'},
        {'Merkmal': 'HP', 'Beschreibung': 'Pferdestärken (PS) des Motors'},
        {'Merkmal': 'Year', 'Beschreibung': 'Baujahr des Autos'}
    ]
    
    # Erstelle eine Tabelle für die Features, beginnend bei 1
    feature_df = pd.DataFrame(features, index=range(1, len(features) + 1))
    st.table(feature_df)

    # Heatmap Checkbox
    show_correlations = st.checkbox('Zeige Heatmap der Korrelationen')
    if show_correlations:
        heatmap_file = analysis.correlations()
        st.image(heatmap_file)  
    
    # Auswertung
    st.markdown("<h5>Zusammenfassung der Korrelationen:</h5>", unsafe_allow_html=True)
    st.markdown("- **Kilometerstand und Jahr** korrelieren negativ mit **-0.68** ( >> neuere Autos haben tendenziell eine geringere Laufleistung)")
    st.markdown("- **PS & Preis** korrelieren positiv mit **0.75** ( >> Autos mit mehr Leistung sind tendenziell teurer)")
    st.markdown("- **Preis & Jahr** korrelieren positiv mit **0.41** ( >> neue Autos sind tendenziell teurer)")

    # Hinzufügen eines horizontalen Linien-Elements
    st.markdown("<hr>", unsafe_allow_html=True)
    
    
    st.markdown("<h3 style='color: yellow;'>Veränderungen über die Jahre</h3>", unsafe_allow_html=True)
    analysis.makes_per_time()
    analysis.show_changes()
    
    
    # Hinzufügen eines horizontalen Linien-Elements
    st.markdown("<hr>", unsafe_allow_html=True)
    
    st.markdown("<h3 style='color: yellow;'>Unterschiedliche Preise und Laufleistung nach Kraftstofftypen</h3>", unsafe_allow_html=True)
    analysis.influence_fuel_types()
    
    # Hinzufügen eines horizontalen Linien-Elements
    st.markdown("<hr>", unsafe_allow_html=True)
    

elif menu == 'Visualisierung der Modellergebnisse':
    visualize.ml_analyse()
   
    

elif menu == 'Autoverkaufspreis-Vorhersage':
    visualize.show_price_prediction_page()

# Footer
st.sidebar.write('Erstellt mit ❤️ von Tami')
