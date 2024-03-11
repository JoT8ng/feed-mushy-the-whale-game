import random
import pygame

class Fish(pygame.sprite.Sprite): 
    
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load("assets/MushyFoodFishy.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screen.get_width() - self.rect.width)
        self.rect.y = random.randint(0, screen.get_height() - self.rect.height)
        self.speedx = random.randint(-4, 4)
        self.speedy = random.randint(-4, 4)

    def update(self):
        # Update position based on speed
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        # Reverse direction if hitting the screen edge
        if self.rect.left < 0 or self.rect.right > self.screen.get_width():
            self.speedx *= -1
        if self.rect.top < 0 or self.rect.bottom > self.screen.get_height():
            self.speedy *= -1

    def check_collision(self, player_rect):
        # Check collision with the player's rect
        return self.rect.colliderect(player_rect)