#!/usr/bin/env python
# coding: utf-8

# In[21]:


def verschluesseln(text,verschiebung):
    for e in text:
        zahl = ord(e)
        if zahl >= 97 and zahl <= 122:
            zahl += verschiebung
            if zahl > 122:
                zahl2 = zahl - 122
                verschluesselt = chr(96 + zahl2)
            else:
                verschluesselt = chr(zahl)
            print(verschluesselt, end="")
        else:
            ausnahme = chr(zahl)
            print(ausnahme, end="")


# In[54]:


print("\n********************************************************\n"
      "\nHallo! Ich kann dir helfen deine Texte zu verschlüsseln!\n"
      "\n********************************************************\n")

while True:
    
    text_alt = input("Gebe bitte den zu verschlüsselnden Text ein: ").lower()
    verschiebung = int(input("Gebe bitte ein um welche Zahl dein Text verschoben werden soll: "))
    if verschiebung <= 0:
        print("\nBitte gebe eine Zahl ein, die größer als 0 ist, sonst kann der Text nicht verschlüsselt werden!")
        verschiebung = int(input("Gebe bitte ein um welche Zahl dein Text verschoben werden soll: "))

    print("\n******************************* \n")
    print("Der verschlüsselte Text lautet:\n")
    verschluesseln(text_alt,verschiebung)
    print("\n\n******************************* \n")

    weiter = input("Möchtest du einen weiteren Text verschlüsseln? ").lower()
    if weiter == "ja":
        continue
    else:
        print("\nOkay, bis zum nächstes Mal! :)")
        break


# In[ ]:





# In[ ]:




