import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Pfad zur Datei
file_path = 'C:\\Users\\tami9\\OneDrive\\Desktop\\Data Scienctist\\Karrierechoaching\\Projekt Autoscout\\autoscout24.csv'
    
# Laden der Daten aus dem absoluten Pfad
df = pd.read_csv(file_path)

# Bereinigen der Daten
df = df.dropna()


# Wie viele Autos verkauft wurden und über welchen Zeitraum
def overview():
    autos_verkauft = df.shape[0]
    zeitraum = (df['year'].min(), df['year'].max())
    return zeitraum, autos_verkauft



# Top 25 meistverkaufte Marken & die restlichen Marken als "Andere" zusammengefasst
def plot_top_makes():
    # Zählen, wie oft jede Marke vorkommt
    marken_verfuegbarkeit = df['make'].value_counts()

    # Auswahl der Top 25 Marken und Zusammenfassung der restlichen als "Andere"
    top_marken = marken_verfuegbarkeit.head(25)
    andere_marken = pd.Series(marken_verfuegbarkeit[25:].sum(), index=['Andere Marken'])

    # Kombinieren der Top 25 Marken mit "Andere"
    marken_verteilung = pd.concat([top_marken, andere_marken])

    # Visualisierung der Daten
    plt.figure(figsize=(6, 8))
    sns.barplot(x=marken_verteilung.values, y=marken_verteilung.index, palette="viridis")
    plt.title('Top 25 der meistverkauften Marken', fontsize=16)
    plt.ylabel('Marke')
    plt.xlabel('Anzahl der verkauften Autos')
    plt.show()

    # Anzeige des Diagramms in der Streamlit-Oberfläche
    st.pyplot(plt)



# Korrelationen zwischen den Features als Heatmap
def correlations():
    # Auswahl der numerischen Features
    numerische_features = df.select_dtypes(include=['float64', 'int64'])
    # Berechnung der Korrelationsmatrix
    korrelationsmatrix = numerische_features.corr()
    
    # Erstellen einer Heatmap der Korrelationsmatrix, um Korrelationen übersichtlicher darzustellen
    plt.figure(figsize=(8, 6))
    heatmap = sns.heatmap(korrelationsmatrix, annot=True, fmt=".2f", cmap='YlOrRd')
    plt.title('Heatmap der Korrelationsmatrix')
    
    # Speichern der Heatmap als Bild im Streamlit-Verzeichnis
    heatmap.figure.savefig("heatmap.png")
    
    return "heatmap.png"  # Rückgabe des Dateinamens des gespeicherten Bilds

  
# Kilometerstand und Jahr korrelieren negativ mit -0.68 (neuere Autos haben tendenziell eine geringere Laufleistung)
# PS & Preis korrelieren positiv mit 0.75 (Autos mit mehr Leistung sind tendenziell teurer)
# Preis & Jahr korrelieren positiv mit 0.41 (neue Autos sind tendenziell teurer)


# Veränderungen über die Jahre im Preis, Kilometerstand und PS
def show_changes():
    # Visualisierung der jahres_trends für durchschnittlichen Preis, Laufleistung und PS über die Jahre
    jahres_trends = df.groupby('year').agg({'price':'mean', 'mileage':'mean', 'hp':'mean'}).reset_index()
    
    # Setzen des Stils für die Plots
    sns.set(style="whitegrid")
    
    # Erstellen von drei Subplots
    fig, ax = plt.subplots(3, 1, figsize=(10, 14), sharex=True)
    
    # Durchschnittspreis über die Jahre
    sns.lineplot(x='year', y='price', data=jahres_trends, ax=ax[0], marker='o')
    ax[0].set_title('Durchschnittspreis der Autos über die Jahre')
    ax[0].set_ylabel('Durchschnittspreis (€)')
    
    # Durchschnittliche Laufleistung über die Jahre
    sns.lineplot(x='year', y='mileage', data=jahres_trends, ax=ax[1], color='orange', marker='o')
    ax[1].set_title('Durchschnittliche Laufleistung der Autos über die Jahre')
    ax[1].set_ylabel('Durchschnittliche Laufleistung (km)')
    
    # Durchschnittliche PS über die Jahre
    sns.lineplot(x='year', y='hp', data=jahres_trends, ax=ax[2], color='green', marker='o')
    ax[2].set_title('Durchschnittliche PS der Autos über die Jahre')
    ax[2].set_ylabel('Durchschnittliche PS (hp)')
    
    # Setzen der x-Achse Label
    for axe in ax:
        axe.set_xlabel('Baujahr')
    
    # Anzeigen des Plots in Streamlit
    st.pyplot(fig)




# Top 10 Modelle inkl. Marke 
def top_10_model():
        
    # Erstellung einer übersichtlichen Tabelle für die meistverkauften Modelle und deren Marken
    # Zuerst fügen wir eine Hilfsspalte hinzu, die 'make' und 'model' kombiniert
    df['make_model'] = df['make'] + " " + df['model']
    
    # Jetzt zählen wir die Top 10 der kombinierten Werte
    top_modelle = df['make_model'].value_counts().head(10).index.tolist()
    
    # Erstellen einer neuen DataFrame, die nur Einträge für die Top 10 Modelle enthält
    top_modelle_df = df[df['make_model'].isin(top_modelle)]
    
    # Gruppieren nach 'make_model' und zählen der Einträge
    top_modelle_verkaufszahlen = top_modelle_df['make_model'].value_counts().reset_index()
    top_modelle_verkaufszahlen.columns = ['Make and Model', 'Verkaufszahlen']
    
    # Visualisierung der meistverkauften Modelle in einem Barplot
    plt.figure(figsize=(10, 14))
    sns.barplot(x='Verkaufszahlen', y='Make and Model', data=top_modelle_verkaufszahlen, palette="viridis")
    plt.title('Top 10 der meistverkauften Modelle', fontsize=16)
    plt.xlabel('Anzahl der verkauften Autos')
    plt.ylabel('Modell')
    
    # Anzeigen des Plots in Streamlit
    st.pyplot(plt)



# Zählen, wie oft jede Marke und jedes Modell vorkommt
marken_verfuegbarkeit = df['make'].value_counts()
modelle_verfuegbarkeit = df['model'].value_counts()
 
# Untersuchung der Veränderung der Popularität über die Zeit für die Top-Marken
top_marken = marken_verfuegbarkeit.head(5).index.tolist()  # Auswahl der Top 5 Marken


# Markenentwicklung über die Jahre
def makes_per_time():
   
    marken_trend_ueber_zeit = df[df['make'].isin(top_marken)].groupby(['year', 'make']).size().unstack().fillna(0)
    
    # Visualisierung der Ergebnisse
    # Popularität und Verfügbarkeit
    plt.figure(figsize=(14, 7))
    sns.lineplot(data=marken_trend_ueber_zeit)
    plt.title('Popularität der Top 5 Marken über die Zeit', fontsize=16)
    plt.ylabel('Anzahl der verkauften Autos')
    plt.xlabel('Baujahr')
    plt.gca().xaxis.labelpad = 20  # Abstand ändern zwischen der X-Achsen-Beschriftung und dem Achsentitel
    plt.gca().yaxis.labelpad = 20  # Abstand ändern zwischen der Y-Achsen-Beschriftung und dem Achsentitel
    
    
    # Anzeigen des Plots in Streamlit
    st.pyplot(plt)
    


# Durchschnittspreis und durchschnittliche Laufleistung für jeden Kraftstofftyp 
def influence_fuel_types():
    kraftstoff_preise = df.groupby('fuel').agg({'price':'mean'}).reset_index()
    kraftstoff_laufleistung = df.groupby('fuel').agg({'mileage':'mean'}).reset_index()
        
    
    # Erster Plot: Durchschnittspreis nach Kraftstofftyp
    plt.figure(figsize=(14, 7))
    sns.barplot(x='fuel', y='price', data=kraftstoff_preise)
    plt.title('Durchschnittspreis nach Kraftstofftyp', fontsize=16)
    plt.ylabel('Durchschnittspreis (€)')
    plt.xlabel('Kraftstofftyp')
    plt.xticks(rotation=90)  # Beschriftungen um 90 Grad drehen
    plt.gca().xaxis.labelpad = 20  # Abstand ändern zwischen der X-Achsen-Beschriftung und dem Achsentitel
    plt.gca().yaxis.labelpad = 20  # Abstand ändern zwischen der Y-Achsen-Beschriftung und dem Achsentitel
    st.pyplot(plt)  # Anzeigen des ersten Plots

    # Zweiter Plot: Durchschnittliche Laufleistung nach Kraftstofftyp
    plt.figure(figsize=(14, 7))
    sns.barplot(x='fuel', y='mileage', data=kraftstoff_laufleistung)
    plt.title('Durchschnittliche Laufleistung nach Kraftstofftyp', fontsize=16)
    plt.ylabel('Durchschnittliche Laufleistung (km)')
    plt.xlabel('Kraftstofftyp')
    plt.xticks(rotation=90)  # Beschriftungen um 90 Grad drehen
    plt.gca().xaxis.labelpad = 20  # Abstand ändern zwischen der X-Achsen-Beschriftung und dem Achsentitel
    plt.gca().yaxis.labelpad = 20  # Abstand ändern zwischen der Y-Achsen-Beschriftung und dem Achsentitel
    st.pyplot(plt) # Anzeigen des zweiten Plots
    

# Durchschnittspreise der Top 5 Marken
def top_marken_avgprice():
    top_marken_avgprice = df[df['make'].isin(top_marken)].groupby('make')['price'].mean().sort_values(ascending=False).reset_index()
    
    # Visualisierung der Durchschnittspreise der Top 5 Marken in einem Barplot
    plt.figure(figsize=(10, 5))
    sns.barplot(x='price', y='make', data=top_marken_avgprice, palette="mako")
    plt.title('Durchschnittspreise der Top 5 Marken')
    plt.xlabel('Durchschnittspreis (€)')
    plt.ylabel('Marke')
    st.pyplot(plt) 



