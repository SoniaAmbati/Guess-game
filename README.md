# Guess Game

Simple command-line number guessing game written in Python.

## Features

- Choose difficulty: Easy (unlimited), Medium (10 tries), Hard (7 tries)
- Guess a number between 1 and 100
- Input validation and helpful prompts
- Press `q` to quit at any time
- Persistent best score saved to `best_score.txt`

## Requirements

- Python 3.8 or newer

## Usage

Run the game from the project folder:

```bash
python guess.py
```

Follow the prompts to select a difficulty and enter guesses. After a round you can choose to play again.

## Files

- [guess.py](guess.py) — main game script
- [best_score.txt](best_score.txt) — created after a winning game; stores the best (lowest) number of attempts
- [README.md](README.md) — this file

## Notes

- The game stores the best score as a plain integer in `best_score.txt` in the current working directory. Deleting that file will reset the best score.

Enjoy! 🎯
