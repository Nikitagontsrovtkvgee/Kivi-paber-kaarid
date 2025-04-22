import random

# M‰ngu valikud
choices = ["kivi", "k‰‰rid", "paber"]

# Funktsioon, mis m‰‰rab vooru vıitja
def determine_winner(p1, p2):
    if p1 == p2:
        return "viik"
    elif (p1 == "kivi" and p2 == "k‰‰rid") or (p1 == "k‰‰rid" and p2 == "paber") or (p1 == "paber" and p2 == "kivi"):
        return "m‰ngija1"
    else:
        return "m‰ngija2"

# Punktide salvestamine
def print_scores(player_names, scores):
    print("\nSeis:")
    for i in range(len(player_names)):
        print(f"{player_names[i]}: {scores[i]} punkti")
    print()

# M‰ngu k‰ivitamine
def play_game():
    print("Tere tulemast m‰ngu 'Kivi-K‰‰rid-Paber'!")
    mode = input("Vali m‰ngure˛iim (1 = inimene vs robot, 2 = inimene vs inimene): ")

    if mode == "1":
        player_names = [input("Sisesta oma nimi: "), "Robot"]
    else:
        player_names = [input("M‰ngija 1 nimi: "), input("M‰ngija 2 nimi: ")]

    scores = [0, 0]
    round_number = 1

    while True:
        print(f"\nVoor {round_number}:")
        if mode == "1":
            p1_choice = input(f"{player_names[0]}, vali (kivi/k‰‰rid/paber): ").lower()
            p2_choice = random.choice(choices)
            print(f"{player_names[1]} valis: {p2_choice}")
        else:
            p1_choice = input(f"{player_names[0]}, vali (kivi/k‰‰rid/paber): ").lower()
            p2_choice = input(f"{player_names[1]}, vali (kivi/k‰‰rid/paber): ").lower()

        if p1_choice not in choices or p2_choice not in choices:
            print("Vigane sisend! Palun kasuta ainult: kivi, k‰‰rid vıi paber.")
            continue

        winner = determine_winner(p1_choice, p2_choice)
        if winner == "viik":
            print("Viik! M‰ngime uuesti.")
        elif winner == "m‰ngija1":
            print(f"{player_names[0]} vıitis selle vooru!")
            scores[0] += 1
        else:
            print(f"{player_names[1]} vıitis selle vooru!")
            scores[1] += 1

        print_scores(player_names, scores)

        cont = input("Kas m‰ngida uus voor? (jah/ei): ").lower()
        if cont != "jah":
            print("M‰ng lıppes. Lıppskoor:")
            print_scores(player_names, scores)
            break

        round_number += 1

play_game()