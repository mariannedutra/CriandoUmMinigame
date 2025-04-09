import pygame
import random

# Inicialização do Pygame
pygame.init()

# Configuração da tela
largura, altura = 800, 300
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Dinossaurinho do Chrome - Versão Invertida')

# Cores
branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (255, 0, 0)

# Dinossauro Principal (direita)
dino_x, dino_y = largura - 90, altura - 70
dino_largura, dino_altura = 40, 60
dino_vel_y = 0
gravity = 1
pulando = False
vidas = 3

# Dinossauro Secundário (Atirador, esquerda)
inimigo_x, inimigo_y = 50, altura - 70
inimigo_largura, inimigo_altura = 40, 60

# Obstáculos ("Tiros")
obstaculo_x = inimigo_x + inimigo_largura
obstaculo_y = altura - 50
obstaculo_largura, obstaculo_altura = 20, 10
obstaculo_vel = 15

# Pontuação
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
            if not pulando:
                dino_vel_y = -15
                pulando = True

    # Gravidade
    dino_vel_y += gravity
    dino_y += dino_vel_y

    if dino_y >= altura - dino_altura - 10:
        dino_y = altura - dino_altura - 10
        pulando = False

    # Movendo obstáculos (tiros)
    obstaculo_x += obstaculo_vel
    if obstaculo_x > largura + obstaculo_largura:
        obstaculo_x = inimigo_x + inimigo_largura
        obstaculo_y = altura - random.randint(40, 70)
        pontos += 1

    # Checagem de colisão
    dino_rect = pygame.Rect(dino_x, dino_y, dino_largura, dino_altura)
    obst_rect = pygame.Rect(obstaculo_x, obstaculo_y, obstaculo_largura, obstaculo_altura)
    if dino_rect.colliderect(obst_rect):
        vidas -= 1
        obstaculo_x = inimigo_x + inimigo_largura
        obstaculo_y = altura - random.randint(40, 70)
        if vidas == 0:
            rodando = False

    # Desenhando elementos
    tela.fill(branco)
    pygame.draw.rect(tela, preto, (dino_x, dino_y, dino_largura, dino_altura))
    pygame.draw.rect(tela, vermelho, (obstaculo_x, obstaculo_y, obstaculo_largura, obstaculo_altura))
    pygame.draw.rect(tela, preto, (inimigo_x, inimigo_y, inimigo_largura, inimigo_altura))

    texto_pontos = fonte.render(f'Pontos: {pontos}', True, preto)
    texto_vidas = fonte.render(f'Vidas: {vidas}', True, vermelho)
    tela.blit(texto_pontos, (650, 10))
    tela.blit(texto_vidas, (650, 40))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()