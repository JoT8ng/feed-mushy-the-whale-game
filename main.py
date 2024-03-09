# Example file showing a basic pygame "game loop"
import pygame
from fish import Fish

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

# Load images
background = pygame.image.load("assets/MushyGameBackground.jpg")
background = pygame.transform.scale(background, (1280, 720))

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player_radius = 40
fish = Fish(screen)
fish_list = []
fish_generation_timer = 0

while running:
    if fish_generation_timer > 300:
        fish_list.append(Fish(screen))
        fish_generation_timer = 0

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.blit(background, (0, 0))

    # RENDER YOUR GAME HERE
    pygame.draw.circle(screen, "red", player_pos, 40)
    
    # Draw all apples
    for simple_fish in fish_list:
        simple_fish.fall()  
        simple_fish.draw()

        if Fish.check_collision(simple_fish, player_pos, player_radius):
            print("Collision detected!")
            # Handle the collision (e.g., reset the apple, update the score, etc.)
            fish_list.remove(simple_fish)  # Example: remove the apple from the list

    # Game controls setup
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000
    fish_generation_timer += 1

pygame.quit()