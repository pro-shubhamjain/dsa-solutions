"""
Problem: Rock Paper Scissors
Pattern: Fundamentals (conditionals / lookup tables)
Time: O(1) | Space: O(1)

Two variants: 2-player, and player-vs-computer.

Input:  play_rps_two_player('rock', 'scissors')
Output: 'Player 1 wins!'
"""
import random

def play_rps_two_player(player1_choice, player2_choice):
    choices = ["rock", "paper", "scissors"]

    if player1_choice not in choices or player2_choice not in choices:
        return "Invalid choices. Please choose from rock, paper, or scissors."

    if player1_choice == player2_choice:
        return "It's a tie!"

    results = {
        "rock": {"scissors": "Player 1 wins!", "paper": "Player 2 wins!"},
        "paper": {"rock": "Player 1 wins!", "scissors": "Player 2 wins!"},
        "scissors": {"paper": "Player 1 wins!", "rock": "Player 2 wins!"},
    }

    return results[player1_choice][player2_choice]


def play_rps_vs_computer(player_choice):
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    results = {
        "rock": {"scissors": "You win!", "paper": "Computer wins!", "rock": "It's a tie!"},
        "paper": {"rock": "You win!", "scissors": "Computer wins!", "paper": "It's a tie!"},
        "scissors": {"paper": "You win!", "rock": "Computer wins!", "scissors": "It's a tie!"},
    }

    result = results[player_choice][computer_choice]
    return f"You chose {player_choice}, the computer chose {computer_choice}. {result}"


if __name__ == "__main__":
    print(play_rps_two_player('rock', 'scissors'))  # Player 1 wins!
