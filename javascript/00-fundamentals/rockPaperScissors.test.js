const { playRPSTwoPlayer, playRPSVsComputer } = require('./rockPaperScissors');

test('playRPSTwoPlayer declares a winner', () => {
  expect(playRPSTwoPlayer('rock', 'scissors')).toEqual('Player 1 wins!');
  expect(playRPSTwoPlayer('paper', 'rock')).toEqual('Player 1 wins!');
});

test('playRPSTwoPlayer detects a tie', () => {
  expect(playRPSTwoPlayer('rock', 'rock')).toEqual("It's a tie!");
});

test('playRPSTwoPlayer rejects invalid choices', () => {
  expect(playRPSTwoPlayer('lizard', 'rock')).toEqual(
    'Invalid choices. Please choose from rock, paper, or scissors.'
  );
});

test('playRPSVsComputer returns a result string mentioning the player choice', () => {
  const result = playRPSVsComputer('rock');
  expect(result).toContain('You chose rock');
});
