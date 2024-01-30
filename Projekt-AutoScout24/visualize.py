import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_absolute_error

def write_info():
    st.markdown(
        """

        ##### Welche Kategorie von Machine Learning ist dieses Problem?

        Das Problem fällt unter die Kategorie des überwachten maschinellen Lernens (Supervised Learning). 
        Beim überwachten Lernen wird das Modell anhand von Beispieldaten trainiert, bei denen sowohl die Eingaben 
        als auch die gewünschten Ausgaben bekannt sind. Hier ist das Ziel, das Modell so zu trainieren, dass es 
        den Preis von Autos auf Basis ihrer Eigenschaften vorhersagen kann.

        """,
        unsafe_allow_html=True
    )
    

def write_eva():
    st.markdown(
        """

        ##### Wie wird die Güte des Modells evaluiert? Was sind die Fehlermetriken?

        Die Güte des Modells wird mit Fehlermetriken wie dem Mean Squared Error (MSE), dem Root Mean Squared Error (RMSE) 
        und dem Mean Absolute Error (MAE) bewertet. 

        - **MSE und RMSE**: Der MSE berechnet den Durchschnitt der quadrierten Abweichungen zwischen den vorhergesagten und den tatsächlichen Werten, 
        während der RMSE die Quadratwurzel des MSE ist und in derselben Einheit wie die Zielvariable ist.
        
        - **MAE**: Der MAE misst die durchschnittliche absolute Abweichung zwischen den vorhergesagten Werten und den tatsächlichen Werten. 
        Im Gegensatz zum RMSE, der größere Fehler stärker gewichtet, behandelt der MAE alle Fehler gleich.

        """,
        unsafe_allow_html=True
    )
    
    
    
# Pfad zur Datei
file_path = 'C:\\Users\\tami9\\OneDrive\\Desktop\\Data Scienctist\\Karrierechoaching\\Projekt Autoscout\\autoscout24.csv'
    
# Laden der Daten aus dem absoluten Pfad
df = pd.read_csv(file_path)

# Bereinigen der Daten
df = df.dropna()



# Für das ML Modell werden nur noch die Top 5 Marken betrachtet
# Zählen, wie oft jede Marke und jedes Modell vorkommt
marken_verfuegbarkeit = df['make'].value_counts()
 
# Auswahl der Top 5 Marken
top_marken = marken_verfuegbarkeit.head(5).index.tolist()  


# 1. Modell trainieren (Lineare Regression), um den Verkaufspreis eines Autos vorherzusagen
# Filtern des Datensatzes für nur Top 5 Marken
df_top5 = df[df['make'].isin(top_marken)]

# Auswahl von Features und Zielvariable
X = df_top5[['mileage', 'hp', 'year']]
y = df_top5['price']

# Entfernen von Zeilen mit fehlenden Werten (NaNs) in den ausgewählten Features und der Zielvariable
X = X.dropna()
y = y[X.index]

# Aufteilung der Daten in Trainings- und Testsets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


###### ------ Erstes Modell: Lineare Regression ------ ######

lr_model = LinearRegression()

# Trainieren des Modells
lr_model.fit(X_train, y_train)

# Vorhersagen auf den Testdaten
y_pred = lr_model.predict(X_test)

# Evaluierung des Modells
mse = mean_squared_error(y_test, y_pred)
lr_rmse = mse ** 0.5



# Funktion zur Erstellung eines Line Charts für die Vorhersagen
def plot_lr_predictions(X_test, y_test, y_pred):
    predictions_df = pd.DataFrame({'Index': X_test.index, 'Tatsächliche Preise': y_test, 'Vorhergesagte Preise': y_pred}).melt('Index', var_name='Typ', value_name='Preis')
    
    plt.figure(figsize=(12, 6))
    sns.lineplot(x='Index', y='Preis', hue='Typ', data=predictions_df)
    plt.title('Vorhersagen des Linearen Regressionsmodells')
    plt.xlabel('Index')
    plt.ylabel('Preis')
    plt.legend(title='')
    plt.tight_layout()
    st.pyplot(plt)


# Funktion zur Erstellung eines Histogramms für die Fehlerverteilung
def plot_lr_error_distribution(y_test, y_pred):
    errors = y_test - y_pred
    plt.figure(figsize=(12, 6))
    sns.histplot(errors, kde=True, bins=30)
    plt.title('Fehlerverteilung des Linearen Regressionsmodells')
    plt.xlabel('Fehler (Tatsächlicher Preis - Vorhergesagter Preis)')
    plt.ylabel('Häufigkeit')
    plt.tight_layout()
    st.pyplot(plt)


def show_lr_results():
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: yellow;'>Modell: Lineare Regression</h3>", unsafe_allow_html=True)
    lr_rmse_str = f"{lr_rmse:.2f}€".replace('.', ',')
    st.write(f"RMSE für Lineare Regression: {lr_rmse_str}")
    plot_lr_predictions(X_test, y_test, y_pred)
    plot_lr_error_distribution(y_test, y_pred)


###### ------Zweites Modell: Random Forest ------ ######

rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
rf_y_pred = rf_model.predict(X_test)
rf_mse = mean_squared_error(y_test, rf_y_pred)
rf_rmse = rf_mse ** 0.5


# Detailansicht der Vorhersagen des Random Forest-Modells
def plot_rf_predictions(X_test, y_test, rf_y_pred):
    predictions_df = pd.DataFrame({'Tatsächliche Preise': y_test, 'Vorhergesagte Preise': rf_y_pred})
    
    # Erstellen eines Line Charts
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=predictions_df)
    plt.title('Vorhersagen des Random Forest-Modells')
    plt.xlabel('Index')
    plt.ylabel('Preis')
    plt.tight_layout()
    st.pyplot(plt)



# Fehlerverteilung des Random Forest-Modells
def plot_rf_error_distribution(y_test, rf_y_pred):
    # Berechnen der Fehler
    errors = y_test - rf_y_pred
    
    # Erstellen eines Histogramms für die Fehlerverteilung
    plt.figure(figsize=(12, 6))
    sns.histplot(errors, kde=True, bins=30)
    plt.title('Fehlerverteilung des Random Forest-Modells')
    plt.xlabel('Fehler (Tatsächlicher Preis - Vorhergesagter Preis)')
    plt.ylabel('Häufigkeit')
    plt.tight_layout()
    st.pyplot(plt)
    

def show_rf_results():
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: yellow;'>Modell: Random Forest</h3>", unsafe_allow_html=True)
    # Anzeigen der Modellergebnisse
    rf_rmse_str = f"{rf_rmse:.2f}€".replace('.', ',')
    st.write(f"RMSE für Random Forest: {rf_rmse_str}")
    plot_rf_predictions(X_test, y_test, rf_y_pred)
    plot_rf_error_distribution(y_test, rf_y_pred)
    



###### ------ Drittes Modell: K-Nearest Neighbors ------ ######

knn_model = KNeighborsRegressor(n_neighbors=5)
knn_model.fit(X_train, y_train)
knn_y_pred = knn_model.predict(X_test)
knn_mse = mean_squared_error(y_test, knn_y_pred)
knn_rmse = knn_mse ** 0.5


def knn_interactive(X_train, y_train, X_test, y_test):
    # Interaktives Element zur Auswahl der Anzahl der Nachbarn
    n_neighbors = st.slider('Anzahl der Nachbarn für KNN', min_value=1, max_value=20, value=5)

    # KNN-Modell mit der gewählten Anzahl von Nachbarn
    knn_model = KNeighborsRegressor(n_neighbors=n_neighbors)
    knn_model.fit(X_train, y_train)
    knn_y_pred = knn_model.predict(X_test)
    
    # Berechnung der Fehlermetriken
    knn_mse = mean_squared_error(y_test, knn_y_pred)
    knn_rmse = knn_mse ** 0.5

    # Anzeigen der Modellergebnisse
    knn_rmse_str = f"{knn_rmse:.2f}€".replace('.', ',')
    st.write(f"RMSE für KNN mit {n_neighbors} Nachbarn: {knn_rmse_str}")
    

    # Detailansicht der Vorhersagen des KNN-Modells
    predictions_df = pd.DataFrame({'Tatsächliche Preise': y_test, 'Vorhergesagte Preise': knn_y_pred})
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=predictions_df)
    plt.title('Vorhersagen des KNN-Modells')
    plt.xlabel('Index')
    plt.ylabel('Preis')
    st.pyplot(plt)

    # Fehlerverteilung des KNN-Modells
    errors = y_test - knn_y_pred
    plt.figure(figsize=(12, 6))
    sns.histplot(errors, kde=True, bins=30)
    plt.title('Fehlerverteilung des KNN-Modells')
    plt.xlabel('Fehler (Tatsächlicher Preis - Vorhergesagter Preis)')
    plt.ylabel('Häufigkeit')
    st.pyplot(plt)




def ml_analyse():
    st.header('Modellbewertungen und Vergleiche')
    st.write("""
            - Kategorie: Überwachtes Lernen
            - Ziel: Vorhersage des Autoverkaufspreises
        """)

    # Tabs für verschiedene Abschnitte
    tab1, tab2, tab3 = st.tabs(["Übersicht", "Modell Ergebnisse", "Modell Vergleich"])

    # Tab 1: Übersicht
    with tab1:
        
        st.markdown("<h3 style='color: yellow;'>Überwachtes maschinelles Lernen</h3>", unsafe_allow_html=True)
        write_info()
        
        
        # Hinzufügen eines horizontalen Linien-Elements
        st.markdown("<hr>", unsafe_allow_html=True)
        st.markdown("<h3 style='color: yellow;'>Modelltraining: Top 5 Marken</h3>", unsafe_allow_html=True)
        # Informationen zu den Top 5 Marken
        st.markdown("""
            Das Modelltraining konzentriert sich auf die **Top 5 Automarken**:
            - Volkswagen
            - Ford
            - Skoda
            - Renault
            - Opel
            
            Ziel ist es, den Verkaufspreis von Autos basierend auf ihren Merkmalen vorherzusagen.
            """)
        
        # Hinzufügen eines horizontalen Linien-Elements
        st.markdown("<hr>", unsafe_allow_html=True)
        st.markdown("<h3 style='color: yellow;'>Modell Evaluation: Fehlermetriken</h3>", unsafe_allow_html=True)
        write_eva()
        
                    
            
            
            
    # Tab 2: Modellergebnisse
    with tab2:
        st.markdown("<h3 style='color: yellow;'>Ergebnisse der trainierten Modelle</h3>", unsafe_allow_html=True)
        # Informationen zu den trainierten Modellen
        st.markdown("""
            Für die Preisvorhersage wurden verschiedene Modelle trainiert und evaluiert:
            - **Lineare Regression**
            - **Random Forest**
            - **K-Nearest Neighbors**
    
            Hier werden die spezifischen Ergebnisse und Metriken jedes Modells dargestellt.
            """)
            
        menu = st.selectbox('Wähle bitte ein Modell:', 
            ['Lineare Regression', 
             'Random Forest', 
             'K-Nearest Neighbors'])
        
        if menu == 'Lineare Regression':
            # Detailansicht der Modellvorhersagen und Fehlerverteilung
            show_lr_results()
            
        
        elif menu == 'Random Forest':
            show_rf_results()



        elif menu == 'K-Nearest Neighbors':
            # Hinzufügen eines horizontalen Linien-Elements
            st.markdown("<hr>", unsafe_allow_html=True)
            st.markdown("<h3 style='color: yellow;'>Modell: K-Nearest Neighbors</h3>", unsafe_allow_html=True)
            # Anzeigen der Modellergebnisse (interaktiv)
            knn_interactive(X_train, y_train, X_test, y_test)
            
        
        

    #  # Tab 3: Modell Vergleich
    with tab3:
        st.markdown("<h3 style='color: yellow;'>Vergleich der Modelle</h3>", unsafe_allow_html=True)
        st.write("""
            In diesem Abschnitt werden die Modelle anhand ihrer Fehlermetriken (RMSE und MAE) miteinander verglichen.
            Ziel ist es, das präziseste Modell für die Preisvorhersage zu identifizieren.
        """)
        
        menu = st.selectbox('Wähle bitte eine Fehlermetrik:',
                            ['RMSE (Root Mean Square Error)', 
                             'MAE (Mean Absolute Error)'])
        
        # Anzeigen der Modellvergleiche
        if menu == 'RMSE (Root Mean Square Error)':
            rmse_comp()
                
        elif menu == 'MAE (Mean Absolute Error)':
            mae_comp()
        



# Berechnung des Durchschnittspreises der Autos in der Top 5 Marken
durchschnittspreis = df_top5['price'].mean()


# Berechnung des Mean Absolute Error (MAE) für jedes Modell
lr_mae = mean_absolute_error(y_test, lr_model.predict(X_test))
rf_mae = mean_absolute_error(y_test, rf_model.predict(X_test))
knn_mae = mean_absolute_error(y_test, knn_model.predict(X_test))



####### ------ Visualisierung der Güte der Modelle ------ ######

# 1. Erstellen eines Balkendiagramms für die prozentualen RMSE-Werte der verschiedenen Modelle
def rmse_comp():
    
    # RNSE-Ergebnisse von Linear Regression, Random Forest und KNN
    model_results = {
        'Lineare Regression': lr_rmse,
        'Random Forest': rf_rmse,
        'KNN': knn_rmse
    }
    # Prozentuale RMSE-Werte für jedes Modell
    model_results_percent = {model: (rmse / durchschnittspreis) * 100 for model, rmse in model_results.items()}
    
    plt.figure(figsize=(8, 4))
    bars = plt.bar(model_results_percent.keys(), model_results_percent.values(), color=['blue', 'green', 'red'])
    plt.xlabel('Modell')
    plt.ylabel('RMSE in Prozent des Durchschnittspreises')
    plt.title('Prozentualer Vergleich der RMSE-Werte der drei Modelle')
    plt.ylim(0, max(model_results_percent.values()) + 5)  # Setzen des y-Achsen-Limits etwas höher als den höchsten Wert
    
    # Anzeigen der genauen prozentualen RMSE-Werte und der RMSE-Werte in Euro über den Balken
    for bar, (model, rmse_percent) in zip(bars, model_results_percent.items()):
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 1, f'{rmse_percent:.2f}%', ha='center', va='bottom', color='black')
        plt.text(bar.get_x() + bar.get_width()/2, yval / 2, f'{model_results[model]:.2f} €', ha='center', va='center', color='white')
    
    # Anzeigen des Plots
    st.pyplot(plt)
    
    st.write("Ein RMSE von 4.625,82 Euro bedeutet, dass die durchschnittlichen Vorhersagen des Modells um diesen Betrag vom tatsächlichen Preis abweichen. Die prozentualen Werte geben eine klare Vorstellung davon, wie groß der durchschnittliche Vorhersagefehler im Verhältnis zum Durchschnittspreis der Autos ist. Ein niedrigerer Prozentsatz bedeutet eine höhere Genauigkeit. Random Forest hat den geringsten prozentualen Fehler, was ihn zum präzisesten Modell unter den dreien macht. ")




# 2. MAE-Ergebnisse von Linear Regression, Random Forest und KNN
def mae_comp():
    mae_results = {
        'Lineare Regression': lr_mae,
        'Random Forest': rf_mae,
        'KNN': knn_mae
    }
    
    # Prozentuale MAE-Werte für jedes Modell
    mae_results_percent = {model: (mae / durchschnittspreis) * 100 for model, mae in mae_results.items()}
    
    # Erstellen eines Balkendiagramms für die prozentualen MAE-Werte der verschiedenen Modelle
    plt.figure(figsize=(8, 4))
    mae_bars = plt.bar(mae_results_percent.keys(), mae_results_percent.values(), color=['blue', 'green', 'red'])
    plt.xlabel('Modell')
    plt.ylabel('MAE in Prozent des Durchschnittspreises')
    plt.title('Prozentualer Vergleich der MAE-Werte der drei Modelle')
    plt.ylim(0, max(mae_results_percent.values()) + 5)  # Setzen des y-Achsen-Limits etwas höher als den höchsten Wert
    
    # Anzeigen der genauen prozentualen MAE-Werte und der MAE-Werte in Euro über den Balken
    for bar, (model, mae_percent) in zip(mae_bars, mae_results_percent.items()):
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 1, f'{mae_percent:.2f}%', ha='center', va='bottom', color='black')
        plt.text(bar.get_x() + bar.get_width()/2, yval / 2, f'{mae_results[model]:.2f} €', ha='center', va='center', color='white')
    
    # Anzeigen des Plots
    st.pyplot(plt)

    st.write('Die Mean Absolute Error (MAE)-Werte der drei Modelle (Lineare Regression, Random Forest und K-Nearest Neighbors) geben Aufschluss über den durchschnittlichen absoluten Fehler jeder Vorhersage im Vergleich zu den tatsächlichen Werten.')




###### ------ Autoverkaufspreisvorhersage ------ ######

# Funktion zur Preisvorhersage
def predict_price(mileage, hp, year):
    input_data = [[mileage, hp, year]]
    prediction = rf_model.predict(input_data)
    return prediction[0]  # Da es nur eine Vorhersage gibt, soll das erste Element zurückgegeben werden

# Streamlit-Seitenlayout für Preisvorhersagen
def show_price_prediction_page():
    st.markdown("<h3 style='color: yellow;'>Autoverkaufspreis-Vorhersage</h3>", unsafe_allow_html=True)
    
    # Eingabefelder für die Merkmale des Autos
    st.markdown("<h5>Gebe bitte die Merkmale des Autos ein</h5>", unsafe_allow_html=True)
    mileage = st.number_input("Laufleistung (km)", min_value=0, max_value=1111111, value=50000)
    hp = st.number_input("Leistung (PS)", min_value=1, max_value=850, value=50)
    year = st.number_input("Baujahr", min_value=2011, max_value=2021, value=2015)

    # Vorhersage-Button
    if st.button("Preis vorhersagen"):
        prediction = predict_price(mileage, hp, year)
        st.success(f"Der vorhergesagte Preis des Autos beträgt: {prediction:.2f}€")
