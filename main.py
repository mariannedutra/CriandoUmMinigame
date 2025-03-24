import pygame
import sys

# Inicialização do Pygame
pygame.init()
WIDTH, HEIGHT = 1920, 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fugindo da Orientadora")
clock = pygame.time.Clock()

# Classe Player com movimento automático, pulo e limite no meio da tela
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/player.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))  # Escala para 100x100
        self.rect = self.image.get_rect(midbottom=(200, HEIGHT))  # Posição inicial
        self.speed_x = 5  # Velocidade horizontal automática
        self.speed_y = 0  # Velocidade vertical para pulo
        self.gravity = 1  # Gravidade
        self.jumping = False  # Controle do pulo
        self.at_limit = False  # Indica se está no meio da tela

    def update(self):
        # Movimento automático para a direita até o meio da tela
        if not self.at_limit:
            self.rect.x += self.speed_x
            if self.rect.centerx >= WIDTH // 2:
                self.rect.centerx = WIDTH // 2
                self.at_limit = True
                self.speed_x = 0  # Para de avançar

        # Aplicar gravidade ao pulo
        if self.jumping:
            self.speed_y += self.gravity
            self.rect.y += self.speed_y
            if self.rect.bottom >= HEIGHT:  # Ao tocar o chão
                self.rect.bottom = HEIGHT
                self.jumping = False
                self.speed_y = 0

        # Limitar aos bounds da tela
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

    def jump(self):
        if not self.jumping:  # Só pula se estiver no chão
            self.jumping = True
            self.speed_y = -20  # Impulso inicial do pulo

    def knockback(self):
        # Empurra o Player para trás
        self.rect.x -= 200  # Recua 200 pixels (ajustável)
        self.at_limit = False
        self.speed_x = 5  # Recupera a velocidade para voltar ao meio

# Classe Orientadora com perseguição
class Orientadora(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.image = pygame.image.load("assets/orientadora.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))  # Escala para 100x100
        self.rect = self.image.get_rect(midbottom=(50, HEIGHT))  # Posição inicial
        self.player = player
        self.speed = 3  # Velocidade de perseguição

    def update(self):
        # Persegue a jogadora
        if self.rect.x < self.player.rect.x and not self.player.at_limit:
            self.rect.x += self.speed
        else:
            self.speed_x = 0

# Classe Obstaculo
class Obstaculo(pygame.sprite.Sprite):
    def __init__(self, x):
        super().__init__()
        self.image = pygame.image.load("assets/obstaculo.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))  # Escala para 100x100
        self.rect = self.image.get_rect(midbottom=(x, HEIGHT))  # Alinhado ao chão

    def update(self, speed):
        self.rect.x -= speed  # Move para a esquerda
        if self.rect.right < 0:  # Remove ao sair da tela
            self.kill()

# Instanciar objetos
player = Player()
orientadora = Orientadora(player)

player_group = pygame.sprite.GroupSingle(player)
orientadora_group = pygame.sprite.GroupSingle(orientadora)
obstaculos_group = pygame.sprite.Group()

# Variáveis do jogo
run = True
game_active = True
base_obstacle_speed = 5  # Velocidade base dos obstáculos
score = 0
spawn_timer = 0

# Loop principal
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                player.jump()

    if game_active:
        # Atualizar lógica
        player.update()
        orientadora.update()

        # Aumentar pontuação
        score += 1

        # Gerar obstáculos
        spawn_timer += 1
        if spawn_timer > 100:  # Intervalo de spawn
            obstaculo = Obstaculo(WIDTH + 50)
            obstaculos_group.add(obstaculo)
            spawn_timer = 0

        # Ajustar velocidade dos obstáculos
        if player.at_limit:
            obstacle_speed = base_obstacle_speed + 2  # Aumenta velocidade no limite
        else:
            obstacle_speed = base_obstacle_speed  # Velocidade normal

        obstaculos_group.update(obstacle_speed)

        # Verificar colisões
        if pygame.sprite.spritecollide(player, orientadora_group, False):
            game_active = False  # Fim de jogo se a orientadora alcançar a jogadora

        if player.at_limit and pygame.sprite.spritecollide(player, obstaculos_group, False):
            player.knockback()  # Empurra o Player para trás ao colidir

        # Desenhar na tela
        screen.fill((255, 255, 255))  # Fundo branco
        player_group.draw(screen)
        orientadora_group.draw(screen)
        obstaculos_group.draw(screen)

        # Exibir pontuação
        font = pygame.font.SysFont(None, 36)
        text_surface = font.render(f"Tempo: {score}", True, (0, 0, 0))
        screen.blit(text_surface, (10, 10))

    else:
        # Tela de Game Over
        screen.fill((255, 255, 255))
        font = pygame.font.SysFont(None, 48)
        msg = font.render("Game Over! Pressione qualquer tecla para reiniciar", True, (0, 0, 0))
        screen.blit(msg, (50, HEIGHT // 2))

        # Reiniciar ao pressionar tecla
        keys = pygame.key.get_pressed()
        if any(keys):
            game_active = True
            score = 0
            obstaculos_group.empty()
            player.rect.midbottom = (200, HEIGHT)
            orientadora.rect.midbottom = (50, HEIGHT)
            player.speed_x = 5
            player.at_limit = False

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()