import pygame
import random

# Inicialização do Pygame
pygame.init()

# Configuração da tela
largura, altura = 800, 300
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Dinossaurinho do Chrome')

# Cores
branco = (255, 255, 255)
preto = (0, 0, 0)

# Dinossauro
dino_x, dino_y = 50, altura - 70
dino_largura, dino_altura = 40, 60
dino_vel_y = 0
gravity = 1
pulando = False

# Obstáculos
obstaculo_x = largura
obstaculo_y = altura - 50
obstaculo_largura, obstaculo_altura = 20, 40
obstaculo_vel = 10

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

    # Movendo obstáculos
    obstaculo_x -= obstaculo_vel
    if obstaculo_x < -obstaculo_largura:
        obstaculo_x = largura + random.randint(0, 400)
        pontos += 1

    # Checagem de colisão
    dino_rect = pygame.Rect(dino_x, dino_y, dino_largura, dino_altura)
    obst_rect = pygame.Rect(obstaculo_x, obstaculo_y, obstaculo_largura, obstaculo_altura)
    if dino_rect.colliderect(obst_rect):
        rodando = False

    # Desenhando elementos
    tela.fill(branco)
    pygame.draw.rect(tela, preto, (dino_x, dino_y, dino_largura, dino_altura))
    pygame.draw.rect(tela, preto, (obstaculo_x, obstaculo_y, obstaculo_largura, obstaculo_altura))

    texto_pontos = fonte.render(f'Pontos: {pontos}', True, preto)
    tela.blit(texto_pontos, (650, 10))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
