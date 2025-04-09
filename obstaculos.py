import pygame
import random

class Obstaculo:
    def __init__(self, x, y, velocidade, largura_obstaculo, altura_obstaculo, imagem_obstaculo=None):
        self.inicial_x = x
        self.x = x
        self.y = y
        self.altura_obstaculo = altura_obstaculo
        self.largura_obstaculo = largura_obstaculo
        self.velocidade = velocidade
        
        if imagem_obstaculo:
            self.imagem = pygame.image.load(imagem_obstaculo).convert_alpha()
            self.imagem = pygame.transform.scale(self.imagem, (largura_obstaculo, altura_obstaculo))
            self.mask = pygame.mask.from_surface(self.imagem)
        else:
            self.imagem = None

    def mover(self, largura_tela, altura_tela, posicao_orientadora):
        self.x += self.velocidade
        if self.x > largura_tela + self.largura_obstaculo:
            self.resetar(altura_tela, posicao_orientadora)
            return True  # Obstáculo passou pela tela
        return False

    def resetar(self, altura_tela, posicao_orientadora):
        self.x = posicao_orientadora
        self.y = altura_tela - random.randint(self.altura_obstaculo - 10, self.altura_obstaculo)

    def desenhar(self, tela):
        tela.blit(self.imagem, (self.x, self.y))
        
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.largura_obstaculo, self.altura_obstaculo)
