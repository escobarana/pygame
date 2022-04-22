# Import the pygame module
import pygame
# Import random for random numbers
import random
from config import SCREEN_HEIGHT, SCREEN_WIDTH, ENEMY_PNG
# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import RLEACCEL


# Define the enemy object by extending pygame.sprite.Sprite
# The surface you draw on the screen is now an attribute of 'enemy'
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        """
            Initialization of the class Enemy
        """
        super(Enemy, self).__init__()
        img = pygame.image.load(ENEMY_PNG)
        self.surf = pygame.transform.scale(img, (55, 45))
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(5, 20)

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        """
            Function to update the enemy
        """
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
