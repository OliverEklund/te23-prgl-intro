from random import randint

print("Hej och välkommen till tärnings spelet, två spelare kommer slå varsinn tärning, först till tre vinster vinner spelet")
player_one_name = input("Spelare Ett, skriv ditt namn: ")
player_two_name = input("spelare Två, skriv ditt namn: ")

player_one_score = 0
player_two_score = 0

play_game = "J"
while play_game == "J":

    player_one_roll = randint(1, 6)
    player_two_roll = randint(1, 6)
    
    if player_one_roll > player_two_roll:
        print(f"{player_one_name} ett vinner med slaget {player_one_roll}. {player_two_name} slog {player_two_roll}")
        player_one_score += 1
   
    elif player_two_roll > player_one_roll:
        print(f"{player_two_name} två vinner med slaget {player_two_roll}. {player_one_name} slog {player_one_roll}")
        player_two_score += 1

    else:
        print(f"Ingen spelare vinner, det är oavgjort, båda slog {player_one_roll}")
    play_game = input("Vill du spela igen(J/N): ")