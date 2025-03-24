import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 1920, 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fugindo da Orientadora")
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/player.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (200,200))
        self.rect = self.image.get_rect(midbottom=(100, HEIGHT))
        self.mask = pygame.mask.from_surface(self.image)  # Máscara adicionada
        self.speed_x = 2
        self.speed_y = 0
        self.gravity = 1
        self.jumping = False
        self.at_limit = False

    def update(self):
        if not self.at_limit:
            self.rect.x += self.speed_x
            if self.rect.centerx >= WIDTH // 2:
                self.rect.centerx = WIDTH // 2
                self.at_limit = True
                self.speed_x = 0

        if self.jumping:
            self.speed_y += self.gravity
            self.rect.y += self.speed_y
            if self.rect.bottom >= HEIGHT:
                self.rect.bottom = HEIGHT
                self.jumping = False
                self.speed_y = 0

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

    def jump(self):
        if not self.jumping:
            self.jumping = True
            self.speed_y = -30

    def knockback(self):
        self.rect.x -= 50
        self.at_limit = False
        self.speed_x = 2

class Orientadora(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.image = pygame.image.load("assets/orientadora.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (200,200))
        self.rect = self.image.get_rect(midbottom=(50, HEIGHT))
        self.mask = pygame.mask.from_surface(self.image)  # Máscara adicionada
        self.player = player
        self.speed = 1.5

    def update(self):
        if self.rect.x < self.player.rect.x and not self.player.at_limit:
            self.rect.x += self.speed
        else:
            self.speed_x = 0

class Obstaculo(pygame.sprite.Sprite):
    def __init__(self, x):
        super().__init__()
        self.image = pygame.image.load("assets/obstaculo.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.rect = self.image.get_rect(midbottom=(x, HEIGHT))
        self.mask = pygame.mask.from_surface(self.image)  # Máscara adicionada

    def update(self, speed):
        self.rect.x -= speed
        if self.rect.right < 0:
            self.kill()

player = Player()
orientadora = Orientadora(player)

player_group = pygame.sprite.GroupSingle(player)
orientadora_group = pygame.sprite.GroupSingle(orientadora)
obstaculos_group = pygame.sprite.Group()

run = True
game_active = True
base_obstacle_speed = 3
score = 0
spawn_timer = 0

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                player.jump()

    if game_active:
        player.update()
        orientadora.update()
        score += 1

        spawn_timer += 1
        if spawn_timer > 150:
            obstaculo = Obstaculo(WIDTH)
            obstaculos_group.add(obstaculo)
            spawn_timer = 0

        if player.at_limit:
            obstacle_speed = base_obstacle_speed + 2
        else:
            obstacle_speed = base_obstacle_speed

        obstaculos_group.update(obstacle_speed)

        # Colisão com máscara com Orientadora
        if pygame.sprite.spritecollide(player, orientadora_group, False, pygame.sprite.collide_mask):
            game_active = False

        # Colisão com máscara com Obstáculos
        if player.at_limit and pygame.sprite.spritecollide(player, obstaculos_group, False, pygame.sprite.collide_mask):
            player.knockback()

        screen.fill((255, 255, 255))
        player_group.draw(screen)
        orientadora_group.draw(screen)
        obstaculos_group.draw(screen)

        font = pygame.font.SysFont(None, 36)
        text_surface = font.render(f"Tempo: {score} e Spawn: {spawn_timer}", True, (0, 0, 0))
        screen.blit(text_surface, (10, 10))

    else:
        screen.fill((255, 255, 255))
        font = pygame.font.SysFont(None, 48)
        msg = font.render("Game Over! Pressione qualquer tecla para reiniciar", True, (0, 0, 0))
        screen.blit(msg, (50, HEIGHT // 2))

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