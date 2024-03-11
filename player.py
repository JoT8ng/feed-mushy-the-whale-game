import pygame

class Player:

    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.NUM_FRAMES = 2
        self.player_frames = [pygame.image.load(f"assets/frames/MushyCharacter_{i}.png") for i in range(self.NUM_FRAMES)]
        self.player_rect = self.player_frames[0].get_rect()
        # Calculate the center of the screen
        self.screen_center_x = self.screen.get_width() // 2
        self.screen_center_y = self.screen.get_height() // 2
        # Set the initial position of the player at the center of the screen
        self.player_rect.center = (self.screen_center_x, self.screen_center_y)

        # Load player animation frames
        self.current_frame = 0
        self.frame_counter = 0
        self.ANIMATION_SPEED = 7
        # Set the initial player image
        self.player_image = self.player_frames[self.current_frame]

        # Initial player direction
        self.player_direction = 'right'

    def update(self, dt, keys):
        if keys[pygame.K_w]:
            if self.player_rect.top > 0:
                self.player_rect.y -= 300 * dt
        if keys[pygame.K_s]:
            if self.player_rect.bottom < self.screen.get_height():
                self.player_rect.y += 300 * dt
        if keys[pygame.K_a]:
            if self.player_rect.left > 0:
                self.player_rect.x -= 300 * dt
                self.player_direction = 'left'
        if keys[pygame.K_d]:
            if self.player_rect.right < self.screen.get_width():
                self.player_rect.x += 300 * dt
                self.player_direction = 'right'

        self.animate()

    def animate(self):
        # Animate player
        self.frame_counter += 1
        if self.frame_counter >= self.ANIMATION_SPEED:
            self.frame_counter = 0
            self.current_frame = (self.current_frame + 1) % self.NUM_FRAMES

    def draw(self):
        # Draw Player
        self.player_image = self.player_frames[self.current_frame]
        if self.player_direction == 'right':
            self.screen.blit(self.player_image, self.player_rect)
        else:  # Flip the image horizontally if the player is facing left
            flipped_player_image = pygame.transform.flip(self.player_image, True, False)
            self.screen.blit(flipped_player_image, self.player_rect)