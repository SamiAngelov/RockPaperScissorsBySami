import random

while True:
    rock = "rock"
    paper = "paper"
    scissors = "scissors"
    print("Bot: Choose [r]ock, [p]aper, or [s]cissors!")
    player_move = input("You: ")

    if player_move == "r":
        player_move = rock
    elif player_move == "p":
        player_move = paper
    elif player_move == "s":
        player_move = scissors
    else:
        raise SystemExit("Invalid input. Try again...")

    computer_move = random.choice([rock, paper, scissors])

    if computer_move == player_move:
        print(f"The Computer chose: {computer_move}")
        print("Bot: Draw! Let's play again, and see the actual winner!")
    elif (player_move == scissors and computer_move == rock) or \
            (player_move == rock and computer_move == paper) or \
            (player_move == scissors and computer_move == rock):
        print(f"The Computer chose: {computer_move}")
        print("Bot: You loose! It looks like I'm better! I see that you want a rematch, don't you?")
    else:
        print(f"The Computer chose: {computer_move}")
        print("Bot: You win! There's no way, next time you are cooked!")

