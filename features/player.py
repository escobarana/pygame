# Import the pygame module
import pygame
from config import SCREEN_HEIGHT, SCREEN_WIDTH, MOVE_DOWN_SOUND, MOVE_UP_SOUND, PLAYER_PNG
# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT
)

# Setup for sounds. Defaults are good.
pygame.mixer.init()

# Load all sound files
# Sound sources: Jon Fincher
MOVE_UP_SOUND = pygame.mixer.Sound(MOVE_UP_SOUND)
MOVE_DOWN_SOUND = pygame.mixer.Sound(MOVE_DOWN_SOUND)


# Define a player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self):
        """
            Initialization of the class Player
        """
        super(Player, self).__init__()
        img = pygame.image.load(PLAYER_PNG)
        self.surf = pygame.transform.scale(img, (55, 45))
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()

    # Move the sprite based on user keypresses
    def update(self, pressed_keys):
        """
            This function updates the player position depending on the pressed_keys param
        :param pressed_keys: disctionary storing the pressed keys of the player
        """
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
            MOVE_UP_SOUND.play()
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
            MOVE_DOWN_SOUND.play()
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
