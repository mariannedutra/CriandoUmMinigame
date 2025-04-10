import pygame
from .base import GameState
from constants import *

class GameOverScreen(GameState):
    def __init__(self, final_score):
        self.score = final_score
        self.font_big  = pygame.font.SysFont(None, 100)
        self.font_small = pygame.font.SysFont(None, 60)
        self.button_rect = pygame.Rect(0, 0, 380, 80)
        self.button_rect.center = (LARGURA_DA_TELA//2, ALTURA_DA_TELA//2 + 290)
        self.image = pygame.image.load("assets/orientadora.png")
        self.next_state = self

    def handle_events(self, events):
        for ev in events:
            if ev.type == pygame.QUIT:
                self.next_state = None
                quit()
            elif ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                if self.button_rect.collidepoint(ev.pos):
                    from .title import TitleScreen
                    self.next_state = TitleScreen()   # reinicia

    def update(self, dt): pass

    def render(self, screen):
        screen.fill(COR_AZUL_CLARO)
        txt1 = self.font_big.render("Fim de Jogo!", True, COR_PRETO)
        txt2 = self.font_small.render(f"Pontos: {self.score}", True, COR_PRETO)
        screen.blit(txt1, txt1.get_rect(center=(LARGURA_DA_TELA//2, ALTURA_DA_TELA//2 - 250)))
        screen.blit(txt2, txt2.get_rect(center=(LARGURA_DA_TELA//2, ALTURA_DA_TELA//2 - 150)))

        # pequena imagem ilustrativa
        img_rect = self.image.get_rect(center=(LARGURA_DA_TELA//2, ALTURA_DA_TELA//2 + 200))
        screen.blit(self.image, img_rect)

        pygame.draw.rect(screen, COR_VERMELHO, self.button_rect, border_radius=12)
        bt_txt = self.font_small.render("REINICIAR", True, COR_BRANCO)
        screen.blit(bt_txt, bt_txt.get_rect(center=self.button_rect.center))
        pygame.display.flip()
