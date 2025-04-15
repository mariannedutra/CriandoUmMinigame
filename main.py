import pygame
import asyncio
from constants import *
from states.title import TitleScreen

async def main():
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
        await asyncio.sleep(0)

    pygame.quit()

asyncio.run(main())
