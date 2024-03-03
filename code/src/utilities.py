# utilities.py

# This module can include various utility functions and classes that can be used throughout the game.

# Example utility functions:
def load_image(path):
    """
    Load an image from a given path.

    :param path: str - Path to the image file.
    :return: Surface - The loaded image.
    """
    # Implement image loading logic
    # Example: return pygame.image.load(path)
    pass

def load_sound(path):
    """
    Load a sound from a given path.

    :param path: str - Path to the sound file.
    :return: Sound - The loaded sound.
    """
    # Implement sound loading logic
    # Example: return pygame.mixer.Sound(path)
    pass

# Example utility classes:
class Button:
    """
    A simple button class for creating interactive buttons in the game.
    """
    def __init__(self, x, y, width, height, text):
        """
        Initialize the button.

        :param x: int - X position of the button.
        :param y: int - Y position of the button.
        :param width: int - Width of the button.
        :param height: int - Height of the button.
        :param text: str - Text displayed on the button.
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, screen):
        """
        Draw the button on the screen.

        :param screen: Surface - The screen to draw the button on.
        """
        # Implement button drawing logic
        pass

    def is_clicked(self, pos):
        """
        Check if the button is clicked.

        :param pos: tuple - The position of the mouse click.
        :return: bool - True if the button is clicked, else False.
        """
        # Implement click detection logic
        pass

# More utility functions or classes can be added as needed for the game.
