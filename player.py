import pygame

class Player:
    def __init__(self, x, y, largura_player, altura_player, imagem_player):
        self.x = x
        self.y = y
        self.vel_y = 0
        self.gravity = 1
        self.pulando = False
        self.vidas = 3
        self.largura_player = largura_player
        self.altura_player = altura_player

        self.imagem = pygame.image.load(imagem_player).convert_alpha()
        self.imagem = pygame.transform.scale(self.imagem, (largura_player, altura_player))
        self.mask = pygame.mask.from_surface(self.imagem)

    def pular(self):
        if not self.pulando:
            self.vel_y = -20
            self.pulando = True

    def aplicar_gravidade(self, altura_tela):
        self.vel_y += self.gravity
        self.y += self.vel_y
        if self.y >= altura_tela - self.altura_player:
            self.y = altura_tela - self.altura_player
            self.vel_y = 0
            self.pulando = False

    def desenhar(self, tela):
        tela.blit(self.imagem, (self.x, self.y))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.largura_player, self.altura_player)
