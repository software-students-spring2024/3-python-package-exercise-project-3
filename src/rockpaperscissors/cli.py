import argparse
from src.rockpaperscissors.game import determine_winner , generate_computer_choice

def play():
    player_choice = input("Choose rock , paper , or scissors:").lower()
    computer_choice = generate_computer_choice()
    print(f"Computer chose {computer_choice}")
    print(determine_winner(player_choice , computer_choice))

def simulate():
    choice_one = generate_computer_choice()
    choice_two = generate_computer_choice()
    print(f"Player One chose {choice_one}")
    print(f"Player Two chose {choice_two}")
    print(determine_winner(choice_one, choice_two))

def main():
    parser = argparse.ArgumentParser(description="Play Rock , Paper, Scissors")
    subparsers = parser.add_subparsers(dest="command")
    parser_play = subparsers.add_parser('play', help='Play against the computer')
    parser_play.set_defaults(func=play)

    parser_simulate = subparsers.add_parser('simulate' , help='Simulate a game between two players')
    parser_simulate.set_defaults(func="simulate")

    args = parser.parse_args()
    if hasattr(args , 'func'):
        args.func()
    else:
        parser.print_help()
