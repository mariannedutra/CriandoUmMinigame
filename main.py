import pygame
from constants import *
from states.title import TitleScreen

def main():
    pygame.init()
    screen = pygame.display.set_mode((LARGURA_DA_TELA, ALTURA_DA_TELA))
    clock  = pygame.time.Clock()
    state  = TitleScreen()

    while state:
        dt     = clock.tick(FPS) / 1000
        events = pygame.event.get()

        state.handle_events(events)
        state.update(dt)
        state.render(screen)

        state = state.next_state

    pygame.quit()

if __name__ == "__main__":
    main()
