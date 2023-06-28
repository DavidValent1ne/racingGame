import pygame
import asyncio
import sys
from gui import Window, Button
from constants import *
from functions import exit_game

class Game:
    """The grouping class for specifying the windows and the running loop."""

    def __init__(self):
        self.windows = {}
        self.running_window = None
        self._clock = pygame.time.Clock()

        pygame.init()

    async def run(self):
        while True:
            window = self.get_window(self.running_window)

            self._clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit()

            window.on_update()
            window.update_elements(self)
            window.display_elements()

            await asyncio.sleep(0)

    def get_window(self, name) -> Window:
        """
        Retrieve the window object with the given name.

        :param name: The name of the window.
        :returns: The desired Window object.
        """
        return self.windows.get(name)

    def open(self, name) -> None:
        """
        Sets a new window as the window to be displayed and updated.

        :param name: The name of the window to display.
        """

        self.running_window = name
        pygame.display.set_caption(f"{NAME} | {name}")

        window = self.get_window(name)

    @staticmethod
    def exit() -> None:
        """
        End the game.
        """
        
        pygame.quit()
        sys.exit()

game = Game()

game.windows = {
    "Menu": Window(
        SPRITES+"sbg.png",
        {
            "open": Button(
                SPRITES+"startButton.png",
                (WIDTH // 2 - 100, 100),
                scale=2,
            ),
            "settings": Button(
                SPRITES+"settingsButton.png",
                (WIDTH // 2 - 150, 300),
                scale=2,
            ),
            "exit": Button(
                SPRITES+"exitButton.png",
                (WIDTH // 2 - 50, 500),
                scale=2,
                on_click=exit_game(game),
            )
        }
    )
}

def main():
    game.running_window = "Menu"
    asyncio.run(game.run())


if __name__ == "__main__":
    main()