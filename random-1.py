from random import randint
rule = input("skriv om ni ska spela udda eller jämnt: ")
computer = randint(1,6)
player = randint(1,6)

if rule == "udda":
    computer_result = computer % 2
    player_result = player % 2
    if computer_result == 0 and player
else:
    computer_result = computer % computer
    player_result = player % player