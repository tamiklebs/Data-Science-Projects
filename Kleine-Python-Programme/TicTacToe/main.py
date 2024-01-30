from board import draw_board, check_if_valid, check_win_condition
from KI import make_random_move


# Startet ein neuen Spiel   
def new_game():
    
    gewinne_spieler = 0
    gewinne_kira = 0
    unentschieden = 0
    
    position = [" "] * 9
    print("\nLass' uns TicTacToe spielen! :) \n")
    spieler = input("Wie heißt du? ")
    print("\n***********************************\n")
    print(f"\nHallo {spieler}! Ich heiße KIra :)\n")
    print("Folgende Spielzüge sind möglich:")
    print("_____________\n")
    print(" 0 | 1 | 2 ")
    print("---|---|---")
    print(" 3 | 4 | 5 ")
    print("---|---|---")
    print(" 6 | 7 | 8 ")
    print("_____________")
    print("\n***********************************\n")
    print("...\n")
    print("Los geht's!\n")
    print("...")
    
    
    while True:
        
        print("\nSo sieht unser aktuelles Spielfeld aus:")
        draw_board(position)

        # Spieler 
        print("\n***********************************\n")
        print(f"{spieler}, du bist am Zug! :)")
        move_p1 = int(input("\nWohin möchtest du deinen Zug setzen? "))

        while check_if_valid(position, move_p1) == False:
            move_p1 = int(input("\nWohin möchtest du deinen Zug setzen? "))
        
        position[move_p1] = "X"
        draw_board(position)
        
        # Check ob Spieler gewonnen hat
        if check_win_condition(position) == True:
            gewinne_spieler += 1
            print("\n***********************************\n")            
            print(f"{spieler}, du hast gewonnen! :) ")
            print("\n----------Ergebnisse----------\n")
            print(f"{spieler} hat {gewinne_spieler} Mal gewonnen\nKIra hat {gewinne_kira} Mal gewonnen\nEs stand {unentschieden} Mal unentschieden")
            print("\n***********************************\n")  

            neues_spiel = input("Möchtest du noch eine Runde spielen? ")
            if neues_spiel.lower() == "ja":
                position = [" "] * 9
                print("Unser Spielfeld ist wieder wie neu:")
                draw_board(position)
            else:
                print("\nOkay, schade. Bis zum nächsten Mal! :)")
                break
        
        # Prüft, ob unentschieden ist
        elif position[0] != " " and position[1] != " " and position[2] != " " and position[3] != " " and position[4] != " " and position[5] != " " and position[6] != " " and position[7] != " " and position[8] != " ":
            unentschieden += 1
            print("\n***********************************\n")
            print("Es steht unentschieden! :) ")
            print("\n----------Ergebnisse----------\n")
            print(f"{spieler} hat {gewinne_spieler} Mal gewonnen\nKIra hat {gewinne_kira} Mal gewonnen\nEs stand {unentschieden} Mal unentschieden")
            print("\n***********************************\n") 

            neues_spiel = input("Möchtest du noch eine Runde spielen? ")
            if neues_spiel.lower() == "ja":
                position = [" "] * 9
                print("Unser Spielfeld ist wieder wie neu:")
                draw_board(position)
            else:
                print("Okay, schade. Bis zum nächsten Mal! :)")
                break   
                
                
        # KIra
        print("\n***********************************\n")
        print(f"KIra ist am Zug! :)\n\nKIra überlegt...\n\n...\n\nKIra hat ihren Zug gesetzt!\n")
     #######################################################################
        
        # KIra ist am Zug
        
        move_kira = make_random_move(position)
        position[move_kira] = "0"
      #  draw_board(position)
###################################################################
        
        # Check ob KIra gewonnen hat
        if check_win_condition(position) == True:
            draw_board(position)
            gewinne_kira += 1
            print("\n***********************************\n")            
            print(f"KIra hat gewonnen! :) ")
            print("\n----------Ergebnisse----------\n")
            print(f"{spieler} hat {gewinne_spieler} Mal gewonnen\nKIra hat {gewinne_kira} Mal gewonnen\nEs stand {unentschieden} Mal unentschieden")
            print("\n***********************************\n") 
            
            neues_spiel = input("Möchtest du noch eine Runde spielen? ")
            if neues_spiel.lower() == "ja":
                position = [" "] * 9
                print("Unser Spielfeld ist wieder wie neu:")
                draw_board(position)
            else:
                print("\nOkay, schade. Bis zum nächsten Mal! :)")
                break
        
        # Prüft, ob unentschieden ist
        elif position[0] != " " and position[1] != " " and position[2] != " " and position[3] != " " and position[4] != " " and position[5] != " " and position[6] != " " and position[7] != " " and position[8] != " ":
            unentschieden += 1
            print("\n***********************************\n")
            print("Es steht unentschieden! :) ")
            print("\n***********************************\n")  
            neues_spiel = input("Möchtest du noch eine Runde spielen? ")
            if neues_spiel.lower() == "ja":
                position = [" "] * 9
                print("Unser Spielfeld ist wieder wie neu:")
                draw_board(position)
            else:
                print("Okay, schade. Bis zum nächsten Mal! :)")
                break   


new_game()