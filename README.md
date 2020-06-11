# Halma AI Game Playing Agent

<div align="center"><img src="https://res.cloudinary.com/rajshah/image/upload/v1591917869/68747470733a2f2f692e696d6775722e636f6d2f644950424135482e676966_uiokih.gif"/></div>

A **Python programmed** AI will play the game of Halma, an adversarial game with some similarities to checkers. The game uses a 16x16 checkered gameboard. Each player starts with 19 game pieces clustered in diagonally opposite corners of the board. To win the game, a player needs to transfer all of their pieces from their starting corner to the opposite corner, into the positions that were initially occupied by the opponent. Read [this](https://en.wikipedia.org/wiki/Halma) article for further details on Halma and its rules.

Essentially, our agent will evaluate the gameboard and output the **best / optimal** move by using [Alpha Beta Pruning](https://en.wikipedia.org/wiki/Alpha_beta_pruning) Minimax algorithm upto 3-ply.

PS. This was homework #2 of CSCI 561 - Fall 2019 - Foundations of Artificial Intelligence - under [Professor Laurent Itti](http://ilab.usc.edu/itti/).

## Setup

- Using Python 3.6 or higher
- Run using - python Halma.py
- The program will auto-generate an "output.txt" file with the results inside the text file.

### input.txt Format

- **First line:** A string SINGLE or GAME to let the AI know whether we are playing a single move (and can use all of the available time for it) of playing a full game with potentially many moves.
- **Second line:** A string BLACK or WHITE indicating which color the agent will play. 
- **Third line:** A strictly positive floating point number indicating the amount of total play time remaining for the agent.
- **Next 16 lines:** Description of the game board, with 16 lines of 16 symbols each:
	* W for a grid cell occupied by a white piece
	* B for a grid cell occupied by a black piece
	* . (a dot) for an empty grid cell

Sample input.txt file:
```
SINGLE
WHITE
100.0
BBBBB...........
BBBBB...........
BBBB............
BBB.............
BB..............
................
................
................
................
................
................
..............WW
.............WWW
............WWWW
...........WWWWW
...........WWWWW
```

### output.txt Format

**1 or more lines:** There are two possible types of moves (Empty E, Jump J):
- **E FROM_X,FROM_Y TO_X,TO_Y** – your agent moves one of your pieces from location FROM_X, FROM_Y to adjacent empty location TO_X, TO_Y. We will again use zero-based, horizontal-first, start at the top-left indexing in the board. So, location 0,0 is the top-left corner of the board; location 15,0 of the top-right corner; location 0,15 is the bottom-left corner, and location 15,15 the bottom-right corner. As explained above, TO_X,TO_Y should be adjacent to FROM_X,FROM_Y (8-connected) and should be empty. If we make such a move, we can only make one per turn.

- **J FROM_X,FROM_Y TO_X,TO_Y** – agent moves one of the pieces from location FROM_X,FROM_Y to empty location TO_X,TO_Y by jumping over a piece in between. We could make several such jumps using the same piece, as explained above, and should write out one jump per line in output.txt.

Sample output.txt file:
```
J 14,13 12,11
```

## Miscellaneous Notes
- In order to avoid deadlock in a game, you can create a "playdata.txt" file that stores the previous move's starting and ending X Y co-ordinates.
- The agent could take anywhere from 0.002s to 30s, it highly depends on the gameboard and the CPU.
- The visualization GIF displayed above is a fast forwarded game of our AI agent VS our AI agent, the actual duration was total 6 minutes (3 minutes per side). - hence the initial moves are symmetric
- Works on a file named "input.txt", **NOT** "input50.txt" or "inputXYZ.txt".
- The "input.txt" file has to be on the same directory level as that of "Halma.py".
- The program will overwrite the "output.txt" file if one already exists.
- The contents of "input.txt" should strictly follow the format mentioned [above](#inputtxt-format), otherwise you may run into an unexpected error.

## Credits
- [Halma Editor Gameboard](https://github.com/panyz522/CS561-HalmaEditor): For visualizing the gameboard and to make AI play against another AI / player.