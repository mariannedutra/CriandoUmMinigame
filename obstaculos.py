import pygame
import random

class Obstaculo:
    def __init__(self, x, y, largura, altura, velocidade, imagem_obstaculo=None):
        self.inicial_x = x
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.velocidade = velocidade
        
        if imagem_obstaculo:
            self.imagem = pygame.image.load(imagem_obstaculo).convert_alpha()
            self.imagem = pygame.transform.scale(self.imagem, (100, 100))
            self.mask = pygame.mask.from_surface(self.imagem)
        else:
            self.imagem = None

    def mover(self, largura_tela, altura_tela, inimigo_largura):
        self.x += self.velocidade
        if self.x > largura_tela + self.largura:
            self.resetar(altura_tela, inimigo_largura)
            return True  # Obstáculo passou pela tela
        return False

    def resetar(self, altura_tela, inimigo_largura):
        self.x = self.inicial_x + inimigo_largura
        self.y = altura_tela - random.randint(40, 70)

    def desenhar(self, tela, cor=(255,0,0)):
        if self.imagem:
            tela.blit(self.imagem, (self.x, self.y))
        else:
            pygame.draw.rect(tela, cor, (self.x, self.y, self.largura, self.altura))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.largura, self.altura)
