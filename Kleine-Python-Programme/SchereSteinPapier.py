#!/usr/bin/env python
# coding: utf-8

# In[2]:


from random import randint


# In[30]:


print("Hallo! ^_______^")
print()
print("Lass' uns Schere Stein Papier spielen! :)")
print()

siege_comp = 0
siege_user = 0 
unentschieden = 0

while True:
    print("***********************")
    print()
    print("Du kannst folgende Züge spielen:")
    print()
    print("1 = Schere")
    print("2 = Stein")
    print("3 = Papier")
    print("4 = Beenden")
    print()
    print("***********************")
    user_zug = int(input("Welche Nummer wählst du? "))
    print()

    if user_zug == 1:
        print("Du hast Schere gewählt!")
        print()
        comp_zug = randint(1,3)
        if comp_zug == 1:
            print("Ich habe auch Schere gewählt.")
            print()
            print("Also: Unentschieden!")
            unentschieden = unentschieden + 1
            print()
            print("***********************")
            print()
            print("Der Spielzwischenstand ist:")
            print("Du hast bisher", siege_user, "Mal gewonnen.")
            print("Ich habe bisher", siege_comp, "Mal gewonnen.")
            print("Es stand", unentschieden, "Mal unentschieden.")
            print()
            print("***********************")
            print()
            print("Weiter geht's!")
            print()
            
        elif comp_zug == 2:
            print("Ich habe Stein gewählt.")
            print()
            print("Stein schlägt Schere.")
            print()
            print("***********************")
            print()
            print("Ich habe gewonnen! :)")
            siege_comp = siege_comp + 1
            print()
            print("***********************")
            print()
            print("Der Spielzwischenstand ist:")
            print("Du hast bisher", siege_user, "Mal gewonnen.")
            print("Ich habe bisher", siege_comp, "Mal gewonnen.")
            print("Es stand", unentschieden, "Mal unentschieden.")
            print()
            print("***********************")
            print()
            print("Weiter geht's!")
            print()
            
        else:
            print("Ich habe Papier gewählt.")
            print()
            print("Schere schneidet Papier.")
            print()
            print("***********************")
            print()
            print("Du hast gewonnen!")
            siege_user = siege_user + 1
            print()
            print("***********************")
            print()
            print("Der Spielzwischenstand ist:")
            print("Du hast bisher", siege_user, "Mal gewonnen.")
            print("Ich habe bisher", siege_comp, "Mal gewonnen.")
            print("Es stand", unentschieden, "Mal unentschieden.")
            print()
            print("***********************")
            print()
            print("Weiter geht's!")
            print()
    
    
    elif user_zug == 2:
        print("Du hast Stein gewählt!")
        print()
        comp_zug = randint(1,3)
        if comp_zug == 1:
            print("Ich habe Schere gewählt.")
            print()
            print("Stein schlägt Schere.")
            print()
            print("***********************")
            print()
            print("Du hast gewonnen!")
            siege_user = siege_user + 1
            print()
            print("***********************")
            print()
            print("Der Spielzwischenstand ist:")
            print("Du hast bisher", siege_user, "Mal gewonnen.")
            print("Ich habe bisher", siege_comp, "Mal gewonnen.")
            print("Es stand", unentschieden, "Mal unentschieden.")
            print()
            print("***********************")
            print()
            print("Weiter geht's!")
            print()
            
        elif comp_zug == 2:
            print("Ich habe auch Stein gewählt.")
            print()
            print("Also: Unentschieden!")
            unentschieden = unentschieden + 1
            print()
            print("***********************")
            print()
            print("Der Spielzwischenstand ist:")
            print("Du hast bisher", siege_user, "Mal gewonnen.")
            print("Ich habe bisher", siege_comp, "Mal gewonnen.")
            print("Es stand", unentschieden, "Mal unentschieden.")
            print()
            print("***********************")
            print()
            print("Weiter geht's!")
            print()
            
        else:
            print("Ich habe Papier gewählt.")
            print()
            print("Papier umwickelt Stein.")
            print()
            print("***********************")
            print()
            print("Ich habe gewonnen!")
            siege_comp = siege_comp + 1
            print()
            print("***********************")
            print()
            print("Der Spielzwischenstand ist:")
            print("Du hast bisher", siege_user, "Mal gewonnen.")
            print("Ich habe bisher", siege_comp, "Mal gewonnen.")
            print("Es stand", unentschieden, "Mal unentschieden.")
            print()
            print("***********************")
            print()
            print("Weiter geht's!")
            print()
    
    elif user_zug == 3:
        print("Du hast Papier gewählt!")
        print()
        comp_zug = randint(1,3)
        if comp_zug == 1:
            print("Ich habe Schere gewählt.")
            print()
            print("Schere schneidet Papier.")
            print()
            print("***********************")
            print()
            print("Ich habe gewonnen!")
            siege_comp = siege_comp + 1
            print()
            print("***********************")
            print()
            print("Der Spielzwischenstand ist:")
            print("Du hast bisher", siege_user, "Mal gewonnen.")
            print("Ich habe bisher", siege_comp, "Mal gewonnen.")
            print("Es stand", unentschieden, "Mal unentschieden.")
            print()
            print("***********************")
            print()
            print("Weiter geht's!")
            print()
            
        elif comp_zug == 2:
            print("Ich habe Stein gewählt.")
            print()
            print("Papier umwickelt Stein.")

            print("Du hast gewonnen!")
            siege_user = siege_user + 1
            print()
            print("***********************")
            print()
            print("Der Spielzwischenstand ist:")
            print("Du hast bisher", siege_user, "Mal gewonnen.")
            print("Ich habe bisher", siege_comp, "Mal gewonnen.")
            print("Es stand", unentschieden, "Mal unentschieden.")
            print()
            print("***********************")
            print()
            print("Weiter geht's!")
            print()
            
        else:
            print("Ich habe auch Papier gewählt.")
            print()
            print("Also: Unentschieden!")
            unentschieden = unentschieden + 1
            print()
            print("***********************")
            print()
            print("Der Spielzwischenstand ist:")
            print("Du hast bisher", siege_user, "Mal gewonnen.")
            print("Ich habe bisher", siege_comp, "Mal gewonnen.")
            print("Es stand", unentschieden, "Mal unentschieden.")
            print()
            print("***********************")
            print()
            print("Weiter geht's!")
            print()


    elif user_zug == 4:
        print("Okay, schade ._. ")
        print()
        comp_zug = randint(1,3)
        if comp_zug == 1:
            print("Mein Zug wäre Schere gewesen.")
            print()
            print("***********************")
            print()
            print("Das Spielergebnis steht fest:")
            print("Du hast", siege_user, "Mal gewonnen.")
            print("Ich habe", siege_comp, "Mal gewonnen.")
            print("Es stand", unentschieden, "Mal unentschieden.")
            print()
            print("***********************")
            print()
            print("Bis zum nächsten Mal! :)")
            break
        elif comp_zug == 2:
            print("Mein Zug wäre Stein gewesen.")
            print()
            print("***********************")
            print()
            print("Das Spielergebnis steht fest:")
            print("Du hast", siege_user, "Mal gewonnen.")
            print("Ich habe", siege_comp, "Mal gewonnen.")
            print("Es stand", unentschieden, "Mal unentschieden.")
            print()
            print("***********************")
            print()
            print("Bis zum nächsten Mal! :)")
            break
        else:
            print("Mein Zug wäre Papier gewesen.")
            print()
            print("***********************")
            print()
            print("Das Spielergebnis steht fest:")
            print("Du hast", siege_user, "Mal gewonnen.")
            print("Ich habe", siege_comp, "Mal gewonnen.")
            print("Es stand", unentschieden, "Mal unentschieden.")
            print()
            print("***********************")
            print()
            print("Bis zum nächsten Mal! :)")
            break
            
    else:
        print("Bitte gebe eine Zahl zwischen 1 und 4 ein, sonst können wir nicht spielen :)")
        continue


# In[ ]:




