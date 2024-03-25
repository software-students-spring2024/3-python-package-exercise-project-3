import random

def determine_winner(player_choice , computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif player_choice == "rock":
        if computer_choice == "scissors":
            return "You win!"
        else:
            return "Computer wins!"
    elif player_choice == "paper":
        if computer_choice == "rock":
            return "You win!"
        else:
            return "Computer wins!"
    elif player_choice == "scissors":
        if computer_choice == "paper":
            return "You win!"
        else:
            return "Computer wins!"
        
def generate_computer_choice():
    choices = ["rock" , "paper" , "scissors"]
    return random.choice(choices)
