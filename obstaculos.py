import pygame
import random

class Obstaculo:
    def __init__(self, x, y, velocidade, imagem_obstaculo=None):
        self.inicial_x = x
        self.x = x
        self.y = y
        self.velocidade = velocidade
        
        if imagem_obstaculo:
            self.imagem = pygame.image.load(imagem_obstaculo).convert_alpha()
            self.imagem = pygame.transform.scale(self.imagem, (90, 90))
            self.largura = self.imagem.get_width()  # Atualiza largura
            self.altura = self.imagem.get_height()  # Atualiza altura
            self.mask = pygame.mask.from_surface(self.imagem)
        else:
            self.imagem = None

    def mover(self, largura_tela, altura_tela, pocicao_orientadora):
        self.x += self.velocidade
        if self.x > largura_tela + self.largura:
            self.resetar(altura_tela, pocicao_orientadora)
            return True  # Obstáculo passou pela tela
        return False

    def resetar(self, altura_tela, pocicao_orientadora):
        self.x = pocicao_orientadora
        self.y = altura_tela - random.randint(80, 90)

    def desenhar(self, tela):
        tela.blit(self.imagem, (self.x, self.y))
        
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.largura, self.altura)
