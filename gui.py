from constants import *
import time
from time import perf_counter

class Window:
    """Base class for creating all GUI windows."""

    def __init__(self, background, elements):
        """ """
        if background is None:
            background = SPRITES / "GameBackground.png"
        if elements is None:
            elements = {}

        self._background = pygame.transform.scale(
            pygame.image.load(background).convert(),
            (WIDTH, HEIGHT),
        )

        self.running = True
        self._last_click = None
        self.elements = elements

    def update_elements(self, game):
        """Updates each element every frame."""
        for name, element in self.elements.items():
            element.on_update()
            if element.is_pressed:
                if self._last_click is None or perf_counter() - self._last_click > 0.2:
                    element.on_click()
                    self._last_click = time.perf_counter()
    

    def display_elements(self):
        """Display each element every frame."""
        SCREEN.blit(self._background, (0, 0))
        for element in self.elements.values():
            element.show()
        pygame.display.update()


    def on_update(self):
        """Can be redefined, called each frame."""

class Element:
    """The base UI object from which all others are made from."""

    def __init__(
        self, position: Rect, border_radius=50, on_update: Function = None
    ):
        """
        :param position: The and y of the top left and the width and height
        :param border_radius: How rounded the edges of the element are
        :param on_update: A function called each frame
        """

        if on_update is not None:
            self.on_update = on_update
        self.position = position
        self._rect = pygame.Rect(position)
        self._border_radius = border_radius
        self.broken = None

    def show(self):
        """Display an element to the screen"""
        pygame.draw.rect(
            SCREEN, (0, 0, 0), self._rect, border_radius=self._border_radius
        )

    def move(self, x: int, y: int):
        """Move the element by the specified amount."""
        self._rect.move_ip(x, y)

    @property
    def is_pressed(self):
        """Determine whether the mouse is pressing an element."""
        return pygame.mouse.get_pressed()[0] and self._rect.collidepoint(
            pygame.mouse.get_pos()
        )

    def on_click(self):
        """Called when an element is clicked on"""

    @property
    def center(self):
        """The center of the element."""
        return self._rect.center

    def on_update(self):
        """Called every frame."""



class Button(Element):
    """A UI element that displays an image and performs an action when clicked."""

    def __init__(
        self,
        path: Path,
        top_left: Coordinate,
        border_radius=5,
        angle=0,
        scale=2.5,
        on_update: Function = None,
        on_click: Function = None,
    ):
        """
        :param path: The file path to the image of the button
        :param top_left: The coordinate of the top left of the element
        :param border_radius: How rounded the edges are
        :param angle: The counterclockwise rotation of the image, in degrees
        :param on_update: A function called each frame
        :param on_click: A function called each time the button is pressed
        """
        self.path = path
        self.angle = angle
        self.scale = scale
        sp = pygame.image.load(path)
        original_width, original_height = sp.get_size()
        self._width = int(original_width * self.scale)
        self._height = int(original_height * self.scale)
        super().__init__(
            self.sprite.get_rect().move(top_left), border_radius, on_update
        )
        if on_click is not None:
            self.on_click = on_click

    def get_button_height(self):
        sprite_image = pygame.image.load(SPRITES / self.path)
        sprite = pygame.sprite.Sprite()
        sprite.image = sprite_image
        sprite.rect = sprite.image.get_rect()
        return sprite.rect.height

    def get_button_width(self):
        sprite_image = pygame.image.load(SPRITES / self.path)
        sprite = pygame.sprite.Sprite()
        sprite.image = sprite_image
        sprite.rect = sprite.image.get_rect()
        return sprite.rect.width

    def show(self):
        image = pygame.transform.rotate(self.sprite, self.angle)
        rect = image.get_rect(center=self.center)

        SCREEN.blit(image, rect)

    def on_click(self):
        """Called whenever the button is pressed"""

    @property
    def sprite(self):
        return pygame.transform.scale(
            pygame.image.load(self.path), (self._width, self._height)
        )