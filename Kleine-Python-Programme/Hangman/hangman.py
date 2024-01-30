import hangman_functions as hf


print("\n ********************************************")
print("***********************************************\n")
print("\n Hey! Lass' uns eine Runde Hangman spielen! :)\n")
print("\n***********************************************")
print(" ********************************************\n")



while True:
    # Spieler nach der Wortlänge fragen
    word_length = hf.get_word_length()
    
    # Ein zufälliges Wort auswählen
    new_word = hf.find_word(word_length)
    
    # Das Spiel starten
    hf.play_hangman(new_word)

    user_input = input("Möchtest du noch eine Runde spielen? ").lower()
    
    if user_input != "ja":
        print("Okay, schade. Bis zum nächsten Mal! :)")
        break
    
    
