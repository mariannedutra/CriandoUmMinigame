import pygame
from player import Player
from orientadora import Orientadora
from obstaculos import Obstaculo

# Inicialização do Pygame
pygame.init()

# Configuração da tela
largura, altura = 1280, 720
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Fugindo da orientadora')

# Cores
branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (255, 0, 0)

# Inicializando personagens proporcionalmente
player = Player(largura - 200, altura, "assets/player.png")
orientadora = Orientadora(80, altura - 140, 60, 90, "assets/orientadora.png")
obstaculo = Obstaculo(orientadora.x, altura - 100, 30, 20, 20, "assets/obstaculo.png")

# Pontuação e fonte
pontos = 0
fonte = pygame.font.SysFont(None, 50)

# Clock
clock = pygame.time.Clock()

# Loop principal do jogo
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
            player.pular()

    # Aplicar gravidade ao player
    player.aplicar_gravidade(altura)

    # Mover obstáculo e verificar pontuação
    if obstaculo.mover(largura, altura, orientadora.largura):
        pontos += 1

    # Checar colisões
    if player.get_rect().colliderect(obstaculo.get_rect()):
        player.vidas -= 1
        obstaculo.resetar(altura, orientadora.largura)
        if player.vidas == 0:
            rodando = False

    # Desenhar elementos
    tela.fill(branco)
    player.desenhar(tela)
    orientadora.desenhar(tela, preto)
    obstaculo.desenhar(tela, vermelho)

    texto_pontos = fonte.render(f'Pontos: {pontos}', True, preto)
    texto_vidas = fonte.render(f'Vidas: {player.vidas}', True, vermelho)
    tela.blit(texto_pontos, (largura - 200, 20))
    tela.blit(texto_vidas, (largura - 200, 60))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()