# Example file showing a basic pygame "game loop"
import pygame
from fish import Fish
from player import Player
from shark import Shark

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

# Load images
background = pygame.image.load("assets/MushyGameBackground.jpg")
background = pygame.transform.scale(background, (1280, 720))

player = Player(screen)

fish_list = pygame.sprite.Group()
fish_generation_timer = 0

shark_list = pygame.sprite.Group()

# Initialize fish sprites
for _ in range(4):
    fish = Fish(screen)
    fish_list.add(fish)

# Initialize shark sprites
for _ in range(3):
    shark = Shark(screen)
    shark_list.add(shark)

while running:
    if fish_generation_timer > 200:
        fish_list.add(Fish(screen))
        fish_generation_timer = 0

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.blit(background, (0, 0))
    
    # Update and draw player
    keys = pygame.key.get_pressed()
    player.update(dt, keys)
    player.draw()

    # Update and draw all fishes
    fish_list.update()
    fish_list.draw(screen)

    # Update and draw all sharks
    for shark in shark_list:
        shark.update()
        shark.animate()
        shark.draw()

    # Check collision with fish
    for fish in fish_list:
        if fish.check_collision(player.player_rect):
            print("Collision detected!")
            fish_list.remove(fish) 

    # Game controls setup
    keys = pygame.key.get_pressed()


    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000
    fish_generation_timer += 1

pygame.quit()