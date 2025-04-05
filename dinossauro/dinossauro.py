import pygame

class Dinossauro:
    def __init__(self, x, y, largura, altura):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.vel_y = 0
        self.gravity = 1
        self.pulando = False
        self.vidas = 3

    def pular(self):
        if not self.pulando:
            self.vel_y = -15
            self.pulando = True

    def aplicar_gravidade(self, altura_tela):
        self.vel_y += self.gravity
        self.y += self.vel_y
        if self.y >= altura_tela - self.altura - 10:
            self.y = altura_tela - self.altura - 10
            self.pulando = False

    def desenhar(self, tela, cor):
        pygame.draw.rect(tela, cor, (self.x, self.y, self.largura, self.altura))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.largura, self.altura)
