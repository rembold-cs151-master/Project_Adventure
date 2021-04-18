# File: Adventure.py
# ------------------
# This program plays the CS 151 Adventure game.

from AdvGame import AdvGame

# Constants

DATA_FILE_PREFIX = "Tiny"

# Main program

def adventure():
    game = read_game_file()
    game.run()

def read_game_file():
    """
    Reads in the given game using the above established
    DATA_FILE_PREFIX. Exits with a warning if file does
    not exist.
    """
    try:
        with open(DATA_FILE_PREFIX + "Rooms.txt") as f:
            return AdvGame.read_game(f)
    except IOError:
        print(f"No file called {DATA_FILE_PREFIX + 'Rooms.txt'} found.")

# Startup code

if __name__ == "__main__":
    adventure()
