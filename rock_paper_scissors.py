import random

YELLOW = "\033[93m"
BLUE = "\033[94m"
RED = "\033[91m"
GREEN = "\033[92m"
END = "\033[00m"

player_points = 0
computer_points = 0

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
        print(f"{BLUE}The Computer chose: {computer_move}.{END}")
        print(f"Bot: {YELLOW}Draw!{END} Let's play again, and see the actual winner!")

    elif (player_move == scissors and computer_move == rock) or \
            (player_move == rock and computer_move == paper) or \
            (player_move == paper and computer_move == scissors):
        computer_points += 1
        print(f"{BLUE}The Computer chose: {computer_move}.{END}")
        print(f"Bot: {RED}You lose!{END} It looks like I'm better!")
    else:
        player_points += 1
        print(f"{BLUE}The Computer chose: {computer_move}.{END}")
        print(f"Bot: {GREEN}You win!{END} There's no way, next time you are cooked!")

    if player_points == computer_points:
        print(f"Your points: {YELLOW}{player_points}{END} | Computer points: {YELLOW}{computer_points}{END}")
    elif player_points > computer_points:
        print(f"Your points: {GREEN}{player_points}{END} | Computer points: {RED}{computer_points}{END}")
    else:
        print(f"Your points: {RED}{player_points}{END} | Computer points: {GREEN}{computer_points}{END}")


    play_again = input(f"Bot: Type [{GREEN}Yes{END}] to Play Again or [{RED}No{END}] to quit: ").lower()

    if play_again == "yes":
        continue
    elif play_again == "no":
        break
    else:
        raise SystemExit("Invalid input. Try again...")



