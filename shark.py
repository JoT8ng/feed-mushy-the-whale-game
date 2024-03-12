import random
import pygame

class Shark(pygame.sprite.Sprite):
    
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.NUM_FRAMES = 2
        self.shark_frames = [pygame.image.load(f"assets/frames/SharkCharacter_{i}.png") for i in range(self.NUM_FRAMES)]
        self.shark_rect = self.shark_frames[0].get_rect()
        self.mask = pygame.mask.from_surface(self.shark_frames[0])
        self.shark_rect.x = random.randint(0, screen.get_width() - self.shark_rect.width)
        self.shark_rect.y = random.randint(0, screen.get_height() - self.shark_rect.height)
        self.speedx = random.randint(-5, 5)
        self.speedy = random.randint(-5, 5)

        # Load player animation frames
        self.current_frame = 0
        self.frame_counter = 0
        self.ANIMATION_SPEED = 15
        # Set the initial player image
        self.shark_image = self.shark_frames[self.current_frame]

        # Initial player direction
        self.shark_direction = 'right'

    def update(self):
        # Update position based on speed
        self.shark_rect.x += self.speedx
        self.shark_rect.y += self.speedy

        # Reverse direction if hitting the screen edge
        if self.shark_rect.left < 0 or self.shark_rect.right > self.screen.get_width():
            self.speedx *= -1
            if self.speedx > 0:
                self.shark_direction = 'left'
            else:
                self.shark_direction = 'right'

        if self.shark_rect.top < 0 or self.shark_rect.bottom > self.screen.get_height():
            self.speedy *= -1

    def animate(self):
        # Animate player
        self.frame_counter += 1
        if self.frame_counter >= self.ANIMATION_SPEED:
            self.frame_counter = 0
            self.current_frame = (self.current_frame + 1) % self.NUM_FRAMES

    def draw(self):
        # Draw sharks
        self.shark_image = self.shark_frames[self.current_frame]
        if self.shark_direction == 'right':
            self.screen.blit(self.shark_image, self.shark_rect)
        else:  # Flip the image horizontally if the player is facing left
            flipped_player_image = pygame.transform.flip(self.shark_image, True, False)
            self.screen.blit(flipped_player_image, self.shark_rect)

    def check_collision(self, player_mask, player_positionx, player_positiony):
        # Get the offset between the player and the shark
        offset_x = player_positionx - self.shark_rect.x
        offset_y = player_positiony - self.shark_rect.y

        # Check if the player mask overlaps with the shark mask
        overlap_area = self.mask.overlap(player_mask, (offset_x, offset_y))

        # If there is an overlap, return True
        if overlap_area:
            return True
        else:
            return False