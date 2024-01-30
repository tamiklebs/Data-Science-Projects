from random import randint

def kluge_kira(position):
    # Überprüfe horizontale Gewinnbedingungen
    for i in range(0, 9, 3):
        if position[i] == position[i + 1] == "X" and position[i + 2] == " ":
            return i + 2
        elif position[i] == position[i + 2] == "X" and position[i + 1] == " ":
            return i + 1
        elif position[i + 1] == position[i + 2] == "X" and position[i] == " ":
            return i
    
    # Überprüfe vertikale Gewinnbedingungen
    for i in range(3):
        if position[i] == position[i + 3] == "X" and position[i + 6] == " ":
            return i + 6
        elif position[i] == position[i + 6] == "X" and position[i + 3] == " ":
            return i + 3
        elif position[i + 3] == position[i + 6] == "X" and position[i] == " ":
            return i

    # Überprüfe diagonale Gewinnbedingungen
    if position[0] == position[4] == "X" and position[8] == " ":
        return 8
    elif position[0] == position[8] == "X" and position[4] == " ":
        return 4
    elif position[4] == position[8] == "X" and position[0] == " ":
        return 0
    if position[2] == position[4] == "X" and position[6] == " ":
        return 6
    elif position[2] == position[6] == "X" and position[4] == " ":
        return 4
    elif position[4] == position[6] == "X" and position[2] == " ":
        return 2

    return None



def make_random_move(position):
    zug = kluge_kira(position)
    if zug == None:
        zug = randint(0,9)
        while True:
            if position[zug] != " ":
                zug = randint(0,9)
            else:
                break
    return zug
        