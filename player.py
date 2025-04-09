import pygame

class Player:
    def __init__(self, x, y, imagem_player=None):
        self.x = x
        self.y = y
        self.vel_y = 0
        self.gravity = 1
        self.pulando = False
        self.vidas = 3

        self.imagem = pygame.image.load(imagem_player).convert_alpha()
        self.imagem = pygame.transform.scale(self.imagem, (100, 100))
        self.largura = self.imagem.get_width()  # Atualiza largura
        self.altura = self.imagem.get_height()  # Atualiza altura
        self.mask = pygame.mask.from_surface(self.imagem)


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

    def desenhar(self, tela):

        tela.blit(self.imagem, (self.x, self.y))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.largura, self.altura)
