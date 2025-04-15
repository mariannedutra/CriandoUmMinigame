# states/base.py
import pygame
from typing import Optional

class GameState:
    """
    Classe‑mãe para todos os estados da aplicação (tela de título, jogo,
    tela de game‑over, pausa, etc.).

    Cada subclasse deve sobrescrever os três métodos principais:
    - handle_events
    - update
    - render

    O atributo `next_state` deve apontar para o próximo estado desejado.
    Se continuar apontando para si mesma, o loop permanece no mesmo estado.
    Quando for definido como None, o jogo é encerrado.
    """

    def __init__(self) -> None:
        # Por padrão, continua no mesmo estado
        self.next_state: Optional["GameState"] = self

    # ---------- Interface pública que as subclasses devem implementar ----------

    def handle_events(self, events: list[pygame.event.Event]) -> None:
        """Processa a fila de eventos do pygame."""
        raise NotImplementedError

    def update(self, dt: float) -> None:
        """Atualiza a lógica interna do estado.
        `dt` é o delta‑time em segundos desde o último quadro."""
        raise NotImplementedError

    def render(self, screen: pygame.Surface) -> None:
        """Desenha o estado na tela (não chamar `pygame.display.flip()` aqui
        se preferir centralizar isso no loop principal)."""
        raise NotImplementedError
