/**
 * Problem: Rock Paper Scissors
 * Pattern: Fundamentals (conditionals / object lookup tables)
 *
 * Two variants: 2-player, and player-vs-computer.
 * NOTE: originally both functions were named `playRPS`, which is a bug --
 * the second declaration silently overwrote the first (same-name function
 * redeclaration in the same scope). Renamed to keep both usable and testable.
 */

// 2-player version
function playRPSTwoPlayer(player1Choice, player2Choice) {
  const choices = ["rock", "paper", "scissors"];

  if (!choices.includes(player1Choice) || !choices.includes(player2Choice)) {
    return "Invalid choices. Please choose from rock, paper, or scissors.";
  }

  if (player1Choice === player2Choice) {
    return "It's a tie!";
  }

  const results = {
    rock: { scissors: "Player 1 wins!", paper: "Player 2 wins!" },
    paper: { rock: "Player 1 wins!", scissors: "Player 2 wins!" },
    scissors: { paper: "Player 1 wins!", rock: "Player 2 wins!" },
  };

  return results[player1Choice][player2Choice];
}

// vs Computer version
function playRPSVsComputer(playerChoice) {
  const choices = ["rock", "paper", "scissors"];
  const computerChoice = choices[Math.floor(Math.random() * 3)];

  const results = {
    rock: {
      scissors: "You win!",
      paper: "Computer wins!",
      rock: "It's a tie!",
    },
    paper: {
      rock: "You win!",
      scissors: "Computer wins!",
      paper: "It's a tie!",
    },
    scissors: {
      paper: "You win!",
      rock: "Computer wins!",
      scissors: "It's a tie!",
    },
  };

  const result = results[playerChoice][computerChoice];

  return `You chose ${playerChoice}, the computer chose ${computerChoice}. ${result}`;
}

module.exports = { playRPSTwoPlayer, playRPSVsComputer };
