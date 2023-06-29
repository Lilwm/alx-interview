Prime Number Game
This program determines the winner of a game played between two players, Maria and Ben. In the game, they take turns choosing a prime number from a set of consecutive integers and removing that number and its multiples from the set. The player who cannot make a move loses the game. The program simulates multiple rounds of the game and determines the player with the most wins.

Game Rules
Maria always goes first.
Players take turns choosing a prime number from the set of consecutive integers starting from 1 up to and including n.
The chosen prime number and its multiples are removed from the set.
The player who cannot make a move (no prime numbers left) loses the game.
Both players play optimally.
Usage
The isWinner(x, nums) function determines the winner of each game round.

Parameters
x (int): The number of rounds to be played.
nums (list): An array of integers n representing the upper bounds of each round.
Return Value
The function returns the name of the player who won the most rounds. If the winner cannot be determined, None is returned.
