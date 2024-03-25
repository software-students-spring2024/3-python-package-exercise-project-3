import pytest
from src.rockpaperscissors.game import determine_winner, generate_computer_choice

def test_determine_winner():
    assert determine_winner("rock", "rock") == "It's a tie!"
    assert determine_winner("rock", "scissors") == "You win!"
    assert determine_winner("rock", "paper") == "Computer wins!"

    assert determine_winner("paper", "paper") == "It's a tie!"
    assert determine_winner("paper", "rock") == "You win!"
    assert determine_winner("paper", "scissors") == "Computer wins!"

    assert determine_winner("scissors", "scissors") == "It's a tie!"
    assert determine_winner("scissors", "paper") == "You win!"
    assert determine_winner("scissors", "rock") == "Computer wins!"

def test_generate_computer_choice():
    choices = ["rock", "paper", "scissors"]
    for i in range(100):
        computer_choice = generate_computer_choice()
        assert computer_choice in choices