import pygame

class Orientadora:
    def __init__(self, x, y, largura, altura, imagem_inimigo=None):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura

        if imagem_inimigo:
            self.imagem = pygame.image.load(imagem_inimigo).convert_alpha()
            self.imagem = pygame.transform.scale(self.imagem, (80, 80))
            self.mask = pygame.mask.from_surface(self.imagem)
        else:
            self.imagem = None

    def desenhar(self, tela, cor):
        if self.imagem:
            tela.blit(self.imagem, (self.x, self.y))
        else:
            pygame.draw.rect(tela, cor, (self.x, self.y, self.largura, self.altura))
