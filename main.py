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

NUM_FRAMES = 2
player_frames = [pygame.image.load(f"assets/frames/MushyCharacter_{i}.png") for i in range(NUM_FRAMES)]
player_rect = player_frames[0].get_rect()
# Calculate the center of the screen
screen_center_x = screen.get_width() // 2
screen_center_y = screen.get_height() // 2
# Set the initial position of the player at the center of the screen
player_rect.center = (screen_center_x, screen_center_y)

# Load player animation frames
current_frame = 0
frame_counter = 0
ANIMATION_SPEED = 7
# Set the initial player image
player_image = player_frames[current_frame]

# Initial player direction
player_direction = 'right'

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

    # Animate player
    frame_counter += 1
    if frame_counter >= ANIMATION_SPEED:
        frame_counter = 0
        current_frame = (current_frame + 1) % NUM_FRAMES
    player_image = player_frames[current_frame]

    # Draw Player
    if player_direction == 'right':
        screen.blit(player_image, player_rect)
    else:  # Flip the image horizontally if the player is facing left
        flipped_player_image = pygame.transform.flip(player_image, True, False)
        screen.blit(flipped_player_image, player_rect)
    
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
        if player_rect.top > 0:
            player_rect.y -= 300 * dt
    if keys[pygame.K_s]:
        if player_rect.bottom < screen.get_height():
            player_rect.y += 300 * dt
    if keys[pygame.K_a]:
        if player_rect.left > 0:
            player_rect.x -= 300 * dt
            player_direction = 'left'
    if keys[pygame.K_d]:
        if player_rect.right < screen.get_width():
            player_rect.x += 300 * dt
            player_direction = 'right'

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000
    fish_generation_timer += 1

pygame.quit()