# core.py
import pygame
from constants import *
from background import Background
from gameObjects import Player, Orientadora, Obstaculo

def initialize_game():
    """Cria player, orientadora, obstáculo, fundo, fonte, etc."""
    player = Player(-LARGURA_PERSONAGEM, POSICAO_DOS_OBJETOS_NO_EIXO_Y,
                    LARGURA_PERSONAGEM, ALTURA_PERSONAGEM, "assets/player.png")
    orientadora = Orientadora(-(2*LARGURA_PERSONAGEM), POSICAO_DOS_OBJETOS_NO_EIXO_Y,
                              LARGURA_PERSONAGEM, ALTURA_PERSONAGEM, "assets/orientadora.png")
    obstaculo = Obstaculo(POSICAO_FINAL_ORIENTADORA_EIXO_X, POSICAO_DOS_OBJETOS_NO_EIXO_Y,
                          10, LARGURA_OBSTACULO, ALTURA_OBSTACULO, "assets/obstaculo.png")
    background = Background(LARGURA_DA_TELA, ALTURA_DA_TELA)
    font = pygame.font.SysFont(None, 50)
    score = 0
    return player, orientadora, obstaculo, background, font, score

# ========================
# Funções de Atualização e Eventos
# ========================
def handle_events(events, player, entrance_active):
    """
    Agora recebe a lista de eventos já capturada em main.py.
    """
    for event in events:
        if event.type == pygame.QUIT:
            return False          # sinaliza para encerrar o jogo

        if not entrance_active and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.pular()
    return True



def update_entrance_phase(player, orientadora):
    """
    Atualiza a fase de entrada, movendo os personagens até suas posições padrão.
    Retorna True enquanto a fase de entrada estiver ativa.
    """
    if player.x < POSICAO_FINAL_PLAYER_EIXO_X:
        player.x += VELOCIDADE_DE_ENTRADA
        if player.x > POSICAO_FINAL_PLAYER_EIXO_X:
            player.x = POSICAO_FINAL_PLAYER_EIXO_X

    if orientadora.x < POSICAO_FINAL_ORIENTADORA_EIXO_X:
        orientadora.x += VELOCIDADE_DE_ENTRADA - 2
        if orientadora.x > POSICAO_FINAL_ORIENTADORA_EIXO_X:
            orientadora.x = POSICAO_FINAL_ORIENTADORA_EIXO_X

    # Fim da fase de entrada quando ambos alcançam a posição padrão
    return not (player.x >= POSICAO_FINAL_PLAYER_EIXO_X and orientadora.x >= POSICAO_FINAL_ORIENTADORA_EIXO_X)


def update_game_state(player, obstaculo, score):
    """
    Atualiza a lógica principal do jogo após a fase de entrada.
    Aplica gravidade, movimenta o obstáculo e trata de colisões.
    Retorna a pontuação atualizada e um flag indicando se o jogo continua rodando.
    """
    # Aplica gravidade ao player
    player.aplicar_gravidade(ALTURA_DA_TELA)

    # Atualiza o obstáculo e incrementa a pontuação se necessário
    
    if obstaculo.mover(LARGURA_DA_TELA, ALTURA_DA_TELA, POSICAO_FINAL_ORIENTADORA_EIXO_X):
        score += 1

    # Checa colisões utilizando máscaras (pixel-perfect)
    offset_x = obstaculo.x - player.x
    offset_y = obstaculo.y - player.y
    if player.mask.overlap(obstaculo.mask, (offset_x, offset_y)) is not None:
        player.vidas -= 1
        obstaculo.resetar(ALTURA_DA_TELA, POSICAO_FINAL_ORIENTADORA_EIXO_X)
        if player.vidas == 0:
            return score, False  # Finaliza o jogo se as vidas acabarem

    return score, True


def render(screen, player, orientadora, obstaculo, background, font, score, entrance_active):
    """
    Renderiza os elementos do jogo na tela,
    incluindo personagens, obstáculo, pontuação e vidas.
    O obstáculo só é desenhado se a fase de entrada já terminou.
    """
    screen.fill(COR_AZUL_CLARO)
     
    # Desenha o fundo com nuvens
    background.draw(screen)

    player.desenhar(screen)
    orientadora.desenhar(screen)
    
    if not entrance_active:
        obstaculo.desenhar(screen)

    # Renderização dos textos de pontuação e vidas
    score_text = font.render(f'Pontos: {score}', True, COR_PRETO)
    lives_text = font.render(f'Vidas: {player.vidas}', True, COR_VERMELHO)
    screen.blit(score_text, (LARGURA_DA_TELA - 200, 20))
    screen.blit(lives_text, (LARGURA_DA_TELA - 200, 60))

    pygame.display.flip()

