# config.py
import pygame

pygame.init()

# Tamanho da tela
WIDTH = 1920
HEIGHT = 1080

# Tela e relógio
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fugindo da Orientadora")
clock = pygame.time.Clock()

# Valores de jogo
# Player
PLAYER_SPAWN_X = 200
PLAYER_SPAWN_Y = HEIGHT

BASE_OBSTACLE_SPEED = 3
SPAWN_INTERVAL = 130  # Intervalo para spawn de obstáculos
PLAYER_SPEED_X = 2
PLAYER_SPEED_X_INITIAL = 8
PLAYER_JUMP_FORCE = -30
PLAYER_KNOCKBACK = 200
ORIENTADORA_SPEED = 2

# Cores e fontes (opcional, para centralizar estilos)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT = pygame.font.SysFont(None, 36)
FONT_LARGE = pygame.font.SysFont(None, 48)
