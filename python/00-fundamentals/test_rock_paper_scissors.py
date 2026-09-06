from rock_paper_scissors import play_rps_two_player, play_rps_vs_computer

def test_two_player_winner():
    assert play_rps_two_player('rock', 'scissors') == 'Player 1 wins!'
    assert play_rps_two_player('paper', 'rock') == 'Player 1 wins!'

def test_two_player_tie():
    assert play_rps_two_player('rock', 'rock') == "It's a tie!"

def test_two_player_invalid():
    assert play_rps_two_player('lizard', 'rock') == \
        'Invalid choices. Please choose from rock, paper, or scissors.'

def test_vs_computer_mentions_choice():
    result = play_rps_vs_computer('rock')
    assert 'You chose rock' in result
