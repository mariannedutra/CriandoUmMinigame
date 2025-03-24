import pygame, sys
pygame.init()

WIDTH, HEIGHT = 1920, 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fugindo da Orientadora")
clock = pygame.time.Clock()

GRAVITY = 1

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/player.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect(midbottom=(200, HEIGHT))
        self.vel_y = 0
        self.speed = 2  # Velocidade horizontal automática
    
    def update(self):
        self.rect.x += self.speed  # Movimento automático para a direita
        
        # Salto
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= HEIGHT:
            self.vel_y = -20

        # Aplicar gravidade
        self.vel_y += GRAVITY
        self.rect.y += self.vel_y

        # Colisão com o chão
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT
            self.vel_y = 0

class Orientadora(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.image = pygame.image.load("assets/orientadora.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect(midbottom=(50, HEIGHT))
        self.player = player
        self.speed = 1.5  # Velocidade constante da orientadora
    
    def update(self):
        if self.rect.x < self.player.rect.x - 50:
            self.rect.x += self.speed

class Obstaculo(pygame.sprite.Sprite):
    def __init__(self, x):
        super().__init__()
        self.image = pygame.image.load("assets/obstaculo.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect(midbottom=(x, HEIGHT))
    
    def update(self, speed):
        self.rect.x -= speed
        if self.rect.right < 0:
            self.kill()

# Instâncias e grupos
player = Player()
orientadora = Orientadora(player)

player_group = pygame.sprite.GroupSingle(player)
orientadora_group = pygame.sprite.GroupSingle(orientadora)
obstaculos_group = pygame.sprite.Group()

# Variáveis do jogo
game_active = True
score = 0
obst_speed = 10
spawn_timer = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if game_active:
        player_group.update()
        orientadora_group.update()

        # Gerar obstáculos periodicamente
        spawn_timer += 1
        if spawn_timer > 90:
            obstaculos_group.add(Obstaculo(WIDTH + 100))
            spawn_timer = 0

        obstaculos_group.update(obst_speed)

        # Colisão jogador-obstáculo
        if pygame.sprite.spritecollide(player, obstaculos_group, False):
            player.speed = 1  # Reduz momentaneamente a velocidade
        else:
            player.speed = 2  # Velocidade normal
        
        # Colisão jogador-orientadora
        if pygame.sprite.spritecollide(player, orientadora_group, False):
            game_active = False

        # Score baseado em tempo
        score += 1
        if score % 600 == 0:
            obst_speed += 1  # Aumenta dificuldade progressivamente

        # Desenho
        screen.fill((255, 255, 255))
        player_group.draw(screen)
        orientadora_group.draw(screen)
        obstaculos_group.draw(screen)

        font = pygame.font.SysFont(None, 36)
        text_surface = font.render(f"Tempo: {score//60}s", True, (0, 0, 0))
        screen.blit(text_surface, (20, 20))
    
    else:
        # Game Over
        screen.fill((255, 255, 255))
        font = pygame.font.SysFont(None, 48)
        msg = font.render(f"Game Over! Sobreviveu {score//60}s. Pressione Espaço p/ reiniciar.", True, (0, 0, 0))
        screen.blit(msg, (WIDTH//2 - msg.get_width()//2, HEIGHT//2))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            game_active = True
            score = 0
            obst_speed = 10
            obstaculos_group.empty()
            player.rect.midbottom = (200, HEIGHT)
            orientadora.rect.midbottom = (50, HEIGHT)

    pygame.display.update()
    clock.tick(60)
