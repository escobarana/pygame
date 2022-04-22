# Import the pygame module
import pygame

from config import SCREEN_WIDTH, SCREEN_HEIGHT, APOXODE_MUSIC, COLLISION_SOUND
from features.cloud import Cloud
from features.player import Player, MOVE_DOWN_SOUND, MOVE_UP_SOUND
from features.enemy import Enemy
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)


def play_game():
    """
        This function starts the game when executed
    """
    # Setup for sounds. Defaults are good.
    pygame.mixer.init()

    # Initialize pygame
    pygame.init()

    # Setup the clock for a decent framerate
    clock = pygame.time.Clock()

    # Create the screen object
    # The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Create a custom event for adding a new enemy
    add_enemy = pygame.USEREVENT + 1
    pygame.time.set_timer(add_enemy, 250)
    add_cloud = pygame.USEREVENT + 2
    pygame.time.set_timer(add_cloud, 1000)

    # Instantiate player. Right now, this is just a rectangle.
    player = Player()

    # Create groups to hold enemy sprites and all sprites
    # - enemies is used for collision detection and position updates
    # - all_sprites is used for rendering
    enemies = pygame.sprite.Group()
    clouds = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    # Variable to keep the main loop running
    running = True

    # Main loop
    while running:
        # for loop through the event queue
        for event in pygame.event.get():
            # Check for KEYDOWN event
            if event.type == KEYDOWN:
                # If the Esc key is pressed, then exit the main loop
                if event.key == K_ESCAPE:
                    running = False
            # Check for QUIT event. If QUIT, then set running to false.
            elif event.type == QUIT:
                running = False
            # Add a new enemy?
            elif event.type == add_enemy:
                # Create the new enemy and add it to sprite groups
                new_enemy = Enemy()
                enemies.add(new_enemy)
                all_sprites.add(new_enemy)
            # Add a new cloud?
            elif event.type == add_cloud:
                # Create the new cloud and add it to sprite groups
                new_cloud = Cloud()
                clouds.add(new_cloud)
                all_sprites.add(new_cloud)

        # Get the set of keys pressed and check for user input
        pressed_keys = pygame.key.get_pressed()

        # Update the player sprite based on user keypresses
        player.update(pressed_keys)

        # Update the position of enemies and clouds
        enemies.update()
        clouds.update()

        # Fill the screen with sky blue
        screen.fill((135, 206, 250))

        # Load all sound files
        # Sound sources: Jon Fincher
        collision_sound = pygame.mixer.Sound(COLLISION_SOUND)

        # Draw all sprites
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)

        # Check if any enemies have collided with the player
        if pygame.sprite.spritecollideany(player, enemies):
            # If so, then remove the player and stop the loop
            player.kill()

            # Stop any moving sounds and play the collision sound
            MOVE_UP_SOUND.stop()
            MOVE_DOWN_SOUND.stop()
            collision_sound.play()

            # Stop the loop
            running = False

        # Flip everything to the display
        pygame.display.flip()

        # Ensure program maintains a rate of 30 frames per second
        clock.tick(30)

        # Load and play background music
        # Sound source: http://ccmixter.org/files/Apoxode/59262
        # License: https://creativecommons.org/licenses/by/3.0/
        pygame.mixer.music.load(APOXODE_MUSIC)
        pygame.mixer.music.play(loops=-1)

    # All done! Stop and quit the mixer.
    pygame.mixer.music.stop()
    pygame.mixer.quit()
