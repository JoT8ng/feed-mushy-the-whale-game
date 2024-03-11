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

player_rect = pygame.Rect(screen.get_width() / 2, screen.get_height() / 2, 40, 40)
fish_list = pygame.sprite.Group()
fish_generation_timer = 0

# Initialize fish sprites
for _ in range(4):
    fish = Fish(screen)
    fish_list.add(fish)

while running:
    if fish_generation_timer > 300:
        fish_list.add(Fish(screen))
        fish_generation_timer = 0

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.blit(background, (0, 0))

    # RENDER YOUR GAME HERE
    pygame.draw.rect(screen, "red", player_rect)
    
    # Update and draw all fish
    fish_list.update()
    fish_list.draw(screen)

    # Check collision with fish
    for fish in fish_list:
        if fish.check_collision(player_rect):
            print("Collision detected!")
            fish_list.remove(fish) 

    # Game controls setup
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_rect.y -= 300 * dt
    if keys[pygame.K_s]:
        player_rect.y += 300 * dt
    if keys[pygame.K_a]:
        player_rect.x -= 300 * dt
    if keys[pygame.K_d]:
        player_rect.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000
    fish_generation_timer += 1

pygame.quit()