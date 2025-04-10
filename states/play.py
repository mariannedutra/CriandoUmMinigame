# states/play.py
import pygame
from .base import GameState
from constants import *
from core import (initialize_game, handle_events, update_entrance_phase,
                  update_game_state, render)

class PlayState(GameState):
    def __init__(self):
        (self.player, self.orientadora, self.obstaculo,
         self.background, self.font, self.score) = initialize_game()
        self.entrance_active = True
        super().__init__()

    # -----------------------------------------------------------------
    def handle_events(self, events):
        # repasse a lista de eventos para a função utilitária
        if not handle_events(events, self.player, self.entrance_active):
            self.next_state = None

    def update(self, dt):
        self.background.update()
        if self.entrance_active:
            self.entrance_active = update_entrance_phase(self.player,
                                                         self.orientadora)
        else:
            self.score, alive = update_game_state(self.player,
                                                  self.obstaculo,
                                                  self.score)
            if not alive:
                from .gameover import GameOverScreen
                self.next_state = GameOverScreen(self.score)

    def render(self, screen):
        render(screen, self.player, self.orientadora, self.obstaculo,
               self.background, self.font, self.score, self.entrance_active)
