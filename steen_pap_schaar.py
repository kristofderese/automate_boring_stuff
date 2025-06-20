import random, sys

print('BLAD   STEEN   SCHAAR')

wins = 0
losses = 0
ties = 0

while True:
    print("Gewonnen: " + str(wins) + " Verloren: " + str(losses) + " Gelijkspel: " + str(ties))
    while True:
        user_choice = input("Kies b voor blad, r voor steen of s voor schaar. Geef q in om te stoppen.   ")
        if user_choice == "q":
            print("Vaarwel!")
            sys.exit()
        if user_choice == "r" or user_choice == "s" or user_choice == "b":
            break
        print("Kies q, b, s of r")

    if user_choice == "r":
        print("Je hebt gekozen voor steen! Steen tegen ....")
    elif user_choice == "s":
        print("Je hebt gekozen voor schaar! Schaar tegen ....")
    if user_choice == "b":
        print("Je hebt gekozen voor blad! Blad tegen ....")

    comp_number = random.randint(1, 3)
    if comp_number == 1:
        comp_move = "r"
        print("Steen")
    elif comp_number == 2:
        comp_move = "s"
        print("Schaar")
    elif comp_number == 3:
        comp_move = "b"
        print("Blad")

    if comp_move == user_choice:
        print("Gelijk!")
        ties = ties +1
    elif comp_move  == "r" and user_choice == "s":
        print("Je bent verloren! Steen wint tegen schaar...")
        losses = losses +1
    elif comp_move  == "r" and user_choice == "b":
        print("Je bent gewonnen! Blad wint tegen steen...")
        wins = wins + 1
    elif comp_move == "b" and user_choice == "s":
        print("Je bent gewonnen! Schaar wint tegen blad...")
        wins = wins + 1
    elif comp_move == "b" and user_choice == "r":
        print("Je bent verloren! Blad wint tegen steen...")
        losses = losses +1
    elif comp_move  == "s" and user_choice == "b":
        print("Je bent verloren! Schaar wint tegen blad...")
        losses = losses +1
    elif comp_move  == "s" and user_choice == "r":
        print("Je bent gewonnen! Steen wint tegen schaar...")
        wins = wins + 1


