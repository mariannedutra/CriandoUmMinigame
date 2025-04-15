import pygame
from .base import GameState
from constants import *

class TitleScreen(GameState):
    def __init__(self):
        self.font  = pygame.font.SysFont(None, 120)
        self.small = pygame.font.SysFont(None, 60)
        self.button_rect = pygame.Rect(0, 0, 280, 80)
        self.button_rect.center = (LARGURA_DA_TELA//2, ALTURA_DA_TELA//2 + 120)
        self.next_state = self     # começa apontando para si mesmo

    def handle_events(self, events):
        for ev in events:
            if ev.type == pygame.QUIT:
                self.next_state = None
                quit()
            elif ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                if self.button_rect.collidepoint(ev.pos):
                    from .play import PlayState
                    self.next_state = PlayState()   # troca de tela

    def update(self, dt): pass

    def render(self, screen):
        screen.fill(COR_AZUL_CLARO)
        title = self.font.render("Fugindo da Orientadora", True, COR_PRETO)
        screen.blit(title, title.get_rect(center=(LARGURA_DA_TELA//2, ALTURA_DA_TELA//2 - 60)))

        pygame.draw.rect(screen, COR_PRETO, self.button_rect, border_radius=12)
        txt = self.small.render("PLAY", True, COR_BRANCO)
        screen.blit(txt, txt.get_rect(center=self.button_rect.center))
        pygame.display.flip()
