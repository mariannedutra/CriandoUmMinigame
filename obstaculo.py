# obstaculo.py
import pygame
from utils.config import WIDTH, HEIGHT

class Obstaculo(pygame.sprite.Sprite):
    def __init__(self, x):
        super().__init__()
        self.image = pygame.image.load("assets/obstaculo.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.rect = self.image.get_rect(midbottom=(x, HEIGHT))
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, speed):
        self.rect.x -= speed
        if self.rect.right < 0:
            self.kill()
