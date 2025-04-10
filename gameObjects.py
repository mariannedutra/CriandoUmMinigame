import random
import pygame

# ========================
# Classe Base para Objetos do Jogo
# ========================
class GameObjects:
    def __init__(self, x, y, largura, altura, imagem=None):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        if imagem:
            self.imagem = pygame.image.load(imagem).convert_alpha()
            self.imagem = pygame.transform.scale(self.imagem, (largura, altura))
            self.mask = pygame.mask.from_surface(self.imagem)
        else:
            self.imagem = None
            self.mask = None

    def desenhar(self, tela):
        if self.imagem:
            tela.blit(self.imagem, (self.x, self.y))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.largura, self.altura)
    
# ========================
# Classes Específicas para o Jogo
# ========================
# Classe do Jogador
# ========================

class Player(GameObjects):
    def __init__(self, x, y, largura_player, altura_player, imagem_player):
        super().__init__(x, y, largura_player, altura_player, imagem_player)
        self.vel_y = 0
        self.gravity = 1
        self.pulando = False
        self.vidas = 3

    def pular(self):
        if not self.pulando:
            self.vel_y = -20
            self.pulando = True

    def aplicar_gravidade(self, altura_tela):
        self.vel_y += self.gravity
        self.y += self.vel_y
        if self.y >= altura_tela - self.altura:
            self.y = altura_tela - self.altura
            self.vel_y = 0
            self.pulando = False

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.largura, self.altura)

# ========================
# Classe do inimigo - Orientadora
# ========================

class Orientadora(GameObjects):
    def __init__(self, x, y, largura_orientadora, altura_orientadora, imagem_inimigo=None):
        super().__init__(x, y, largura_orientadora, altura_orientadora, imagem_inimigo)
        
# ========================
# Classe para Obstáculos
# ========================
        
class Obstaculo(GameObjects):
    def __init__(self, x, y, velocidade, largura_obstaculo, altura_obstaculo, imagem_obstaculo=None):
        super().__init__(x, y, largura_obstaculo, altura_obstaculo, imagem_obstaculo)
        self.inicial_x = x
        self.velocidade = velocidade

    def mover(self, largura_tela, altura_tela, posicao_orientadora):
        self.x += self.velocidade
        if self.x > largura_tela + self.largura:
            self.resetar(altura_tela, posicao_orientadora)
            return True  # Obstáculo passou pela tela
        return False

    def resetar(self, altura_tela, posicao_orientadora):
        self.x = posicao_orientadora
        self.y = altura_tela - random.randint(self.altura - 10, self.altura)