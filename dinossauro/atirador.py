import pygame

class Atirador:
    def __init__(self, x, y, largura, altura):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura

    def desenhar(self, tela, cor):
        pygame.draw.rect(tela, cor, (self.x, self.y, self.largura, self.altura))
