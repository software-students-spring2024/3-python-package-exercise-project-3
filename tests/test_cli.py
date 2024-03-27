# test_cli.py

import pytest
from unittest.mock import patch
from src.rockpaperscissors2333.cli import play, simulate, stats

def test_play_scissors_vs_rock(mocker, capsys):
    mocker_input = mocker.patch('builtins.input', return_value='scissors')
    mocker_generate_computer_choice = mocker.patch('src.rockpaperscissors2333.cli.generate_computer_choice', return_value='rock')

    play()

    captured = capsys.readouterr()
    assert "Computer chose rock" in captured.out
    assert "Computer wins!" in captured.out

def test_play_rock_vs_paper(mocker, capsys):
    mocker_input = mocker.patch('builtins.input', return_value='rock')
    mocker_generate_computer_choice = mocker.patch('src.rockpaperscissors2333.cli.generate_computer_choice', return_value='paper')

    play()

    captured = capsys.readouterr()
    assert "Computer chose paper" in captured.out
    assert "Computer wins!" in captured.out

def test_play_paper_vs_scissors(mocker, capsys):
    mocker_input = mocker.patch('builtins.input', return_value='paper')
    mocker_generate_computer_choice = mocker.patch('src.rockpaperscissors2333.cli.generate_computer_choice', return_value='scissors')

    play()

    captured = capsys.readouterr()
    assert "Computer chose scissors" in captured.out
    assert "Computer wins!" in captured.out

def test_play_both_choose_rock(mocker, capsys):
    mocker_input = mocker.patch('builtins.input', return_value='rock')
    mocker_generate_computer_choice = mocker.patch('src.rockpaperscissors2333.cli.generate_computer_choice', return_value='rock')

    play()

    captured = capsys.readouterr()
    assert "Computer chose rock" in captured.out
    assert "It's a tie!" in captured.out

def test_simulate_scissors_rock_then_rock_paper(mocker, capsys):
    mocker_generate_computer_choice = mocker.patch('src.rockpaperscissors2333.cli.generate_computer_choice', side_effect=['scissors', 'rock'])
    
    simulate()
    
    captured = capsys.readouterr()
    assert "You chose scissors" in captured.out
    assert "Computer chose rock" in captured.out
    assert "Computer wins!" in captured.out

def test_simulate_paper_scissors_then_rock_rock(mocker, capsys):
    mocker_generate_computer_choice = mocker.patch('src.rockpaperscissors2333.cli.generate_computer_choice', side_effect=['paper', 'scissors'])
    
    simulate()
    
    captured = capsys.readouterr()
    assert "You chose paper" in captured.out
    assert "Computer chose scissors" in captured.out
    assert "Computer wins!" in captured.out

def test_simulate_rock_rock_then_rock_rock(mocker, capsys):
    mocker_generate_computer_choice = mocker.patch('src.rockpaperscissors2333.cli.generate_computer_choice', side_effect=['rock', 'rock'])

    simulate()
    
    captured = capsys.readouterr()
    assert "You chose rock" in captured.out
    assert "Computer chose rock" in captured.out
    assert "It's a tie!" in captured.out

def test_stats_no_games(capsys):
    stats()
    captured = capsys.readouterr()
    assert "You haven't played any games yet!" in captured.out

def test_stats_with_games(mocker, capsys):
    mocker.patch('src.rockpaperscissors2333.cli.total_games', return_value=10)
    mocker.patch('src.rockpaperscissors2333.cli.player_choices', return_value=['rock', 'paper', 'rock', 'scissors'])
    
    stats()
    
    captured = capsys.readouterr()
    assert "Your statistics:" in captured.out
    assert "Rock: 2 times" in captured.out
    assert "Paper: 1 times" in captured.out
    assert "Scissors: 1 times" in captured.out