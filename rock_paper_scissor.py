# incomplete program   Need to be 9 condtional statrements
import random
choices=['Rock','Paper','Scissor']
computer=random.choice(choices)
player = False
cpu_score  = 0
player_score = 0
while True:
    player = input("Rock, Paper and Scissor?").capitalize()
    # Conditions of Rock,Paper and Scissor
    if player == computer:
        print('Tie!')
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!",computer,"covers",player)
            cpu_score+=1
        else:
            print("You win!",player,"smashes",computer)
            player_score+=1
    elif player == "Paper":
        if computer == "Scissor":
            print("You lose!",computer,"cut",player)
            cpu_score+=1
        else:
            print("You win!",player,"covers",computer)
            player_score+=1
    elif player == "Scissor":
        if computer =="Rock":
            print("You lose...",computer,"smashes",player)
            cpu_score+=1
        else:
            print("You win!",player,"cut",computer)
            player_score+=1
    elif player =='End':
        print("Final Scores:")
        print(f"CPU:{cpu_score}")
        print(f"Player:{player_score}")
        break