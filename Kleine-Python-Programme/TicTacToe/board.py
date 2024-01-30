# Zeichnet das Spielfeld
def draw_board(position):
    print("_____________\n")
    print(position[0], " | ", position[1], " | ", position[2])
    print("---|-----|---")
    print(position[3], " | ", position[4], " | ", position[5])
    print("---|-----|---")
    print(position[6], " | ", position[7], " | ", position[8])
    print("_____________")

    

# Prüft, ob ein Zug im Spielfeld ist
def check_if_valid(position, move):
    if move < 0 or move > 8:
        print("\n***********************************\n")
        print("Du versuchst gerade deinen Zug außerhalb des Spielfeldes zu setzen ;)\n\nWähle bitte eine der folgenden Positionen aus:")
        print("_____________\n")
        print(" 0 | 1 | 2 ")
        print("---|---|---")
        print(" 3 | 4 | 5 ")
        print("---|---|---")
        print(" 6 | 7 | 8 ")
        print("_____________")
        print("\n***********************************\n")
        return False
    
    elif position[move] != " ":
        print("\nDer gewählte Platz ist bereits belegt. Wähle bitte einen anderen Platz :)")
        return False
        
    else:
        return True

# Prüft, ob jemand gewonnen hat
def check_win_condition(position):
    # Horizontaler Gewinn
    if position[0] == position[1] == position[2] and position[0] != " ":
        return True
    elif position[3] == position[4] == position[5] and position[3] != " ":
        return True    
    elif position[6] == position[7] == position[8] and position[6] != " ":
        return True

    # Vertikaler Gewinn
    elif position[0] == position[3] == position[6] and position[0] != " ":
        return True
    elif position[1] == position[4] == position[7] and position[1] != " ":
        return True    
    elif position[2] == position[5] == position[8] and position[2] != " ":
        return True
    
    # Diagonaler Gewinn
    elif position[0] == position[4] == position[8] and position[0] != " ":
        return True
    elif position[6] == position[4] == position[2] and position[6] != " ":
        return True    

    else:
        return False
