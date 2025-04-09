import pygame
from player import Player
from orientadora import Orientadora
from obstaculos import Obstaculo
from background import Background

# ========================
# Configurações e Constantes
# ========================
LARGURA_DA_TELA = 1280
ALTURA_DA_TELA = 720
FPS = 60

# Cores (R, G, B)
COR_BRANCA = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_RED = (255, 0, 0)

# Configurações dos objetos

ALTURA_PERSONAGEM = 140
LARGURA_PERSONAGEM = 140
ALTURA_OBSTACULO = 90
LARGURA_OBSTACULO = 90

# Posições Iniciais e Finais para os personagens
POSICAO_DOS_OBJETOS_NO_EIXO_Y = ALTURA_DA_TELA - 140
POSICAO_FINAL_PLAYER_EIXO_X= LARGURA_DA_TELA - 2*LARGURA_PERSONAGEM
POSICAO_FINAL_ORIENTADORA_EIXO_X = LARGURA_PERSONAGEM - 3//LARGURA_PERSONAGEM

# Velocidade de entrada dos personagens
VELOCIDADE_DE_ENTRADA = 8


# ========================
# Funções de Inicialização e Configuração
# ========================
def initialize_game():
    """Inicializa o pygame, a tela, os personagens, a fonte e o clock."""
    pygame.init()
    screen = pygame.display.set_mode((LARGURA_DA_TELA, ALTURA_DA_TELA))
    pygame.display.set_caption('Fugindo da Orientadora')

    # Inicializando personagens com suas posições iniciais
    player = Player(0, POSICAO_DOS_OBJETOS_NO_EIXO_Y, LARGURA_PERSONAGEM, ALTURA_PERSONAGEM, "assets/player.png")
    player.x = - LARGURA_PERSONAGEM # Inicia fora da tela à esquerda

    orientadora = Orientadora(0, POSICAO_DOS_OBJETOS_NO_EIXO_Y, LARGURA_PERSONAGEM, ALTURA_PERSONAGEM, "assets/orientadora.png")
    orientadora.x = -(2*LARGURA_PERSONAGEM) # Inicia fora da tela à esquerda

    obstaculo = Obstaculo(POSICAO_FINAL_ORIENTADORA_EIXO_X, POSICAO_DOS_OBJETOS_NO_EIXO_Y, 10, LARGURA_OBSTACULO, ALTURA_OBSTACULO, "assets/obstaculo.png")
    
    # Inicializando o fundo
    background = Background(LARGURA_DA_TELA, ALTURA_DA_TELA)

    # Inicializando fonte e pontuação
    font = pygame.font.SysFont(None, 50)
    score = 0

    clock = pygame.time.Clock()

    return screen, player, orientadora, obstaculo, background, font, score, clock


# ========================
# Funções de Atualização e Eventos
# ========================
def handle_events(player, is_entrance_active):
    """
    Processa a fila de eventos.
    Permite o pulo somente após a fase de entrada.
    Retorna False se o jogador solicitar fechar o jogo.
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
            return False
        
        if not is_entrance_active and event.type == pygame.KEYDOWN:
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
    screen.fill(COR_BRANCA)
    
    # Desenha o fundo com nuvens
    background.draw(screen)

    player.desenhar(screen)
    orientadora.desenhar(screen)
    
    if not entrance_active:
        obstaculo.desenhar(screen)

    # Renderização dos textos de pontuação e vidas
    score_text = font.render(f'Pontos: {score}', True, COLOR_BLACK)
    lives_text = font.render(f'Vidas: {player.vidas}', True, COLOR_RED)
    screen.blit(score_text, (LARGURA_DA_TELA - 200, 20))
    screen.blit(lives_text, (LARGURA_DA_TELA - 200, 60))

    pygame.display.flip()


# ========================
# Função Principal
# ========================
def main():
    screen, player, orientadora, obstaculo, background, font, score, clock = initialize_game()
    running = True
    entrance_active = True

    while running:
        running = handle_events(player, entrance_active)
        
        # Atualiza o fundo
        background.update()

        if entrance_active:
            entrance_active = update_entrance_phase(player, orientadora)
        else:
            score, running = update_game_state(player, obstaculo, score)

        render(screen, player, orientadora, obstaculo, background, font, score, entrance_active)
        clock.tick(FPS)

    pygame.quit()


if __name__ == '__main__':
    main()
