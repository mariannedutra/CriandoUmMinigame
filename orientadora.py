import pygame

class Orientadora:
    def __init__(self, x, y, largura_orientadora, altura_orientadora, imagem_inimigo=None):
        self.x = x
        self.y = y
        self.altura_orientadora = altura_orientadora 
        self.largura = largura_orientadora
        if imagem_inimigo:
            self.imagem = pygame.image.load(imagem_inimigo).convert_alpha()
            self.imagem = pygame.transform.scale(self.imagem, (largura_orientadora, altura_orientadora))
            
            self.mask = pygame.mask.from_surface(self.imagem)
        else:
            self.imagem = None

    def desenhar(self, tela):
        tela.blit(self.imagem, (self.x, self.y))
