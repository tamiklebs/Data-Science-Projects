import streamlit as st
from api import fetch_data

st.title("Pokédex App")

# Input des Users
user_input = st.text_input("Über welches Pokémon möchtest du mehr erfahren?")
name = user_input.lower()
data = fetch_data(name)

if user_input:
    if data is not None:
        if 'sprites' in data and 'front_default' in data['sprites']:
            # Index vom Ende der URL 
            pokemon_index = int(data['species']['url'].split('/')[-2])


            # Spalte 1: Bild und grundlegende Informationen
            st.header("Informationen")
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"Pokédex Nr: {pokemon_index}")
                st.write(f"Gewicht: {data['weight']/10} kg")
                st.write(f"Größe: {data['height']/10} m")
            with col2:
                st.image(data['sprites']['front_default'], caption=data['name'].upper(), width=100)
           

            # Spalte 2: Typ und Fähigkeiten
            st.header("Weitere Details")
            col1, col2 = st.columns(2)
            with col1:
                st.subheader("Typ")
                if 'types' in data:
                    for pokemon_type in data['types']:
                        type_colors = {
                            'electric': '#DAA520',    # Electric: Yellow
                            'normal': '#D3D3D3',      # Normal: LightGray
                            'fire': '#FF4500',        # Fire: Orange-Red
                            'water': '#0000FF',       # Water: Blue
                            'grass': '#008000',       # Grass: Green
                            'ice': '#00BFFF',         # Ice: DeepSkyBlue
                            'fighting': '#800000',    # Fighting: Maroon
                            'poison': '#800080',      # Poison: Purple
                            'ground': '#8B4513',      # Ground: SaddleBrown
                            'flying': '#87CEEB',      # Flying: SkyBlue
                            'psychic': '#FF69B4',     # Psychic: HotPink
                            'bug': '#008080',         # Bug: Teal
                            'rock': '#A52A2A',        # Rock: Brown
                            'ghost': '#4B0082',       # Ghost: Indigo
                            'dragon': '#483D8B',      # Dragon: DarkSlateBlue
                            'dark': '#2F4F4F',        # Dark: DarkSlateGray
                            'steel': '#B0C4DE',       # Steel: LightSteelBlue
                            'fairy': '#FFC0CB'        # Fairy: Pink
                        }

                  
                        # Hintergrundfarbe basierend auf dem Typ setzen
                        background_color = type_colors.get(pokemon_type['type']['name'], 'white')
                    
                        # Den Namen des Typs mit Hintergrundfarbe rendern
                        st.markdown(f"<span style='background-color: {background_color}; color: white; padding: 5px; border-radius: 5px;'>{pokemon_type['type']['name'].capitalize()}</span>", unsafe_allow_html=True)

                        
            with col2:
                st.subheader("Fähigkeiten")
                if 'abilities' in data:
                    for ability in data['abilities']:
                        if 'ability' in ability and 'name' in ability['ability']:
                            st.write(ability['ability']['name'])
            st.write("")
            st.write("")
                  
            # Spalte 3: Statistiken
            st.header("Statistik")
            col1, col2 = st.columns(2)
            with col1:
                if 'stats' in data:
                    for stat in data['stats']:
                        if 'stat' in stat and 'name' in stat['stat'] and 'base_stat' in stat:
                            st.write(f"{stat['stat']['name']}: {stat['base_stat']}")
           
            # Platzhalter für Abstand
            st.write("")
            st.write("")
            st.write("")
            
# Liste mit Beispielnamen
pokemon_names = [
    "Pikachu",
    "Charmander",
    "Bulbasaur",
    "Squirtle",
    "Jigglypuff",
    "Eevee",
    "Snorlax",
    "Gyarados",
    "Meowth",
    "Psyduck"
]


st.subheader("10 Pokémon Namen zum Ausprobieren")

# Anzeigen der Liste
st.write("Dir fällt kein Pokémon ein? Schau' dir Infos zu einem dieser Pokémon an:")
for name in pokemon_names:
    st.write(f"- {name}")