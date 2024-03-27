# test_cli.py

import pytest
from unittest.mock import patch
from src.rockpaperscissors.cli import play, simulate

def test_play(mocker, capsys):
    mocker_input = mocker.patch('builtins.input', return_value='rock')
    mocker_generate_computer_choice = mocker.patch('src.rockpaperscissors.cli.generate_computer_choice', return_value='scissors')

    play()

    captured = capsys.readouterr()
    assert "Computer chose scissors" in captured.out
    assert "You win!" in captured.out

def test_simulate(mocker, capsys):
    mocker_generate_computer_choice = mocker.patch('src.rockpaperscissors.cli.generate_computer_choice', side_effect=['rock', 'scissors'])

    simulate()
    
    captured = capsys.readouterr()
    assert "Player One chose rock" in captured.out
    assert "Player Two chose scissors" in captured.out
    assert "You win!" in captured.out
