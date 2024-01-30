import requests

base_url = "https://pokeapi.co/api/v2/pokemon/"

def fetch_data(name):
    
    poke_url = f"{base_url}{name}"
    res = requests.get(poke_url)
    
    if res.status_code == 200:        
        data = res.json()
        return data    
    else:
        print("Fehler! Ist der eingegebene Name richtig geschrieben?")        
        return None