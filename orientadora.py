# orientadora.py
import pygame
from utils.config import WIDTH, HEIGHT, ORIENTADORA_SPEED

class Orientadora(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.image = pygame.image.load("assets/orientadora.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (200, 200))
        self.rect = self.image.get_rect(midbottom=(0, HEIGHT))
        self.mask = pygame.mask.from_surface(self.image)

        self.player = player
        self.speed = ORIENTADORA_SPEED

    def update(self):
        # Movimenta-se em direção ao player enquanto o player não estiver parado no meio
        if self.rect.x < self.player.rect.x and not self.player.at_limit:
            self.rect.x += self.speed
        # Caso queira mais comportamento, adicione mais lógicas aqui
