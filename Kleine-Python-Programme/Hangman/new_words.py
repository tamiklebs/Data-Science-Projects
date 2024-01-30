import sqlite3

connection = sqlite3.connect("C:\\Users\\tami9\\OneDrive\\Desktop\\Data Scienctist\\Python\\Hausaufgaben 11\\database.db")
cur = connection.cursor()

# Wort und Anzahl der Buchstaben zur Tabelle hinzufügen
def add_new_word(word):
    cur.execute("INSERT INTO words (word, letters) VALUES (?, ?)", (word.upper(), len(word)))
    connection.commit()
    connection.close()

# Nutzer neues Wort eingeben lassen
def get_new_word():
    while True:
        new_word = input("Bitte gebe das neue Wort ein: ")
        if new_word.isalpha():
            return new_word.upper()
        else:
            print("Ungültige Eingabe. Bitte gebe nur Buchstaben ein.")


new_word = get_new_word()
add_new_word(new_word)
print(f"{new_word} wurde zur Datenbank hinzugefügt :)")
