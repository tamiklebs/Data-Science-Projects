import sqlite3
from random import choice

# Ganzer Dateipfad, weil es anders nicht funktionieren will (trotz gleicher Ordner, etc.)
connection = sqlite3.connect("C:\\Users\\tami9\\OneDrive\\Desktop\\Data Scienctist\\Python\\Hausaufgaben 11\\database.db")
cur = connection.cursor()


# Spieler nach Wortlänge fragen und Zahl überprüfen 
def get_word_length():
    while True:
        length = input("Gebe bitte eine Wortlänge ein (3-10): ")
        if length.isdigit() and 3 <= int(length) <= 10:
            return int(length)
        else:
            print("Ungültige Eingabe. Die Wortlänge muss zwischen 3 und 10 liegen.")


# Lädt alle Wörter mit der gewünschten Buchstabenanzahl aus der Datenbank 
# und wählt ein zufälliges Wort aus
def find_word(length):
    cur.execute("SELECT word FROM words WHERE letters = ?", (length,))
    words = cur.fetchall()
    word = choice(words)
    return word[0].upper()


# Startet ein neues Spiel mit dem übergebenen Wort und max. Versuchen
def play_hangman(wort, max_versuche=5):
    gesuchtes_wort = ['_'] * len(wort)
    
    falsche_versuche = 0

    while '_' in gesuchtes_wort and falsche_versuche < max_versuche:
        print("\nAktuelles Wort:", " ".join(gesuchtes_wort))
        buchstabe = input("\nWähle einen Buchstaben: ").upper()

        if len(buchstabe) == 1 and buchstabe.isalpha():
            if buchstabe in wort:
                for i in range(len(wort)):
                    if wort[i] == buchstabe:
                        gesuchtes_wort[i] = buchstabe
            else:
                falsche_versuche += 1
                print(f"\nFalsch geraten! Du hast noch {max_versuche - falsche_versuche} Versuche übrig.")
        else:
            print("\nEingabe fehlerhaft! Bitte gebe nur einen Buchstaben ein.")

    if '_' not in gesuchtes_wort:
        print("\n*****************************************\n")
        print(f" Herzlichen Glückwunsch, du hast gewonnen!\n Das gesuchte Wort lautet: {wort}")
        print("\n*****************************************\n")

    else:
        print("\n*******************************\n")
        print(f" Du hast verloren! \n Das gesuchte Wort war: {wort}")
        print("\n*******************************\n")




