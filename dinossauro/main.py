import pygame
from dinossauro import Dinossauro
from atirador import Atirador
from obstaculos import Obstaculo

# Inicialização do Pygame
pygame.init()

# Configuração da tela
largura, altura = 800, 300
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Dinossaurinho do Chrome - Versão Modular')

# Cores
branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (255, 0, 0)

# Inicializando personagens
dino = Dinossauro(largura - 90, altura - 70, 40, 60)
inimigo = Atirador(50, altura - 70, 40, 60)
obstaculo = Obstaculo(inimigo.x, altura - 50, 20, 10, 15)

# Pontuação e fonte
pontos = 0
fonte = pygame.font.SysFont(None, 30)

# Clock
clock = pygame.time.Clock()

# Loop principal do jogo
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
            dino.pular()

    # Aplicar gravidade ao dinossauro
    dino.aplicar_gravidade(altura)

    # Mover obstáculo e verificar pontuação
    if obstaculo.mover(largura, altura, inimigo.largura):
        pontos += 1

    # Checar colisões
    if dino.get_rect().colliderect(obstaculo.get_rect()):
        dino.vidas -= 1
        obstaculo.resetar(altura, inimigo.largura)
        if dino.vidas == 0:
            rodando = False

    # Desenhar elementos
    tela.fill(branco)
    dino.desenhar(tela, preto)
    inimigo.desenhar(tela, preto)
    obstaculo.desenhar(tela, vermelho)

    texto_pontos = fonte.render(f'Pontos: {pontos}', True, preto)
    texto_vidas = fonte.render(f'Vidas: {dino.vidas}', True, vermelho)
    tela.blit(texto_pontos, (650, 10))
    tela.blit(texto_vidas, (650, 40))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
