[![CI / CD](https://github.com/software-students-spring2024/pysong/actions/workflows/build.yaml/badge.svg)](https://github.com/software-students-spring2024/pysong/actions/workflows/build.yaml)
# Rock Paper Scissors Game

A simple, interactive Rock, Paper, Scissors game implemented in Python. This package allows users to play against the computer or simulate a game between two computer-controlled players. The package also includes a scoreboard that the user can reset at will, and a tutorial to teach you how to play.


## Installation

You can install the Rock Paper Scissors game using pip:
```pip install rockpaperscissors2333```

## Usage

To use our game, simply import the package and select a number option from the list that appears!


### Code Snippet
```python
from rockpaperscissors2333.cli import play, simulate, tutorial
from rockpaperscissors2333.game import reset_scoreboard

while True:
    print("Welcome to Rock, Paper, Scissors!")
    print("1. Play against the computer")
    print("2. Simulate a game between two players")
    print("3. Reset the scoreboard")
    print("4. View tutorial")
    print("5. Quit")
    choice = input("Enter the number of your choice: ")
    if choice == "1":
        play()
    elif choice == "2":
        simulate()
    elif choice == "3":
        reset_scoreboard()
    elif choice == "4":
        tutorial()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")    
```

## Documentation

This package includes the following functions:

In "_main_.py", the "main" allows you to select an option for what function you want to access in the game. If an invalid option is selected, it will let you know.

In "cli.py":

    A function "play()" for allowing the player to play against the computer. It prompts a user input for their move and provides a computer move, then compares the two and lets you know who won, updating the scoreboard.

    A function "simulate()" for allowing the player to simulate a game between two computer players. It provides two computer moves, and offers the same comparison.

    A function "tutorial()" which includes print statements that explain how the game works to the user.


In "game.py":
    
    A function "determine_winner()" takes in the player's choice and the computer's choice. It completes the logic required for play() to select a winner between the two by returning the winner.

    "generate_computer_choice()" allows for geenration of a random option from the computer between "rock," "paper," and "scissors".

    "update_scoreboard()" takes the winner from determine_winner() and, depending on who it was, adds a win to the scoreboard for either the player or the computer.

    "reset_scoreboard()" clears the scoreboard.


## Teammates

Zijie Zhao ([github](https://github.com/ZijieZha0)), Nathan Daniel ([github](https://github.com/WayyGood)), Ellis Pinsky ([github](https://github.com/ellispinsky)), Kevin Li ([github](https://github.com/Kevinli712390))

