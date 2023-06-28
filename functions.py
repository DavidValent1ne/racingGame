from constants import *
def exit_game(game) -> Function:
    """Closes the game and thanks the player."""
    def inner():
        game.exit()

    return inner