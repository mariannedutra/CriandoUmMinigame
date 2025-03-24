# player.py
import pygame
from utils.config import PLAYER_SPEED_X_INITIAL, WIDTH, HEIGHT, PLAYER_SPEED_X, PLAYER_JUMP_FORCE, PLAYER_KNOCKBACK

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/player.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (200, 200))
        self.rect = self.image.get_rect(midbottom=(200, HEIGHT))
        self.mask = pygame.mask.from_surface(self.image)
        
        self.speed_x = PLAYER_SPEED_X_INITIAL
        self.speed_y = 0
        self.gravity = 1
        self.jumping = False
        self.at_limit = False  # Flag para saber se chegou ao centro da tela

    def update(self):
        # Movimento horizontal até chegar ao meio da tela
        if not self.at_limit:
            self.rect.x += self.speed_x
            if self.rect.centerx >= WIDTH // 2:
                self.rect.centerx = WIDTH // 2
                self.at_limit = True
                self.speed_x = 0

        # Lógica de pular (simples)
        if self.jumping:
            self.speed_y += self.gravity
            self.rect.y += self.speed_y
            if self.rect.bottom >= HEIGHT:
                self.rect.bottom = HEIGHT
                self.jumping = False
                self.speed_y = 0

        # Limites de tela (opcional caso queira evitar que saia da tela)
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

    def jump(self):
        if not self.jumping:
            self.jumping = True
            self.speed_y = PLAYER_JUMP_FORCE

    def knockback(self):
        self.rect.x -= PLAYER_KNOCKBACK
        self.at_limit = False
        self.speed_x = PLAYER_SPEED_X
