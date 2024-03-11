import pygame
import os

class Score:
    def __init__(self, screen):
        self.screen = screen
        self.score = 0
        self.font = pygame.font.Font(os.path.join("fonts", "PressStart2P.ttf"), 28)
        self.color = (255, 255, 255)  # White color

    def update(self, collision_type):
        if collision_type == 'fish':
            self.score += 1
        elif collision_type == 'shark':
            self.score = 0

    def draw(self):
        score_text = self.font.render("Score: " + str(self.score), True, self.color)
        self.screen.blit(score_text, (10, 10))
