# main.py
import pygame
import sys

# Importa variáveis e tela de config.py
from utils.config import (
    screen, clock, WIDTH, HEIGHT, WHITE, BLACK,
    BASE_OBSTACLE_SPEED, SPAWN_INTERVAL, FONT, FONT_LARGE
)
from player import Player
from orientadora import Orientadora
from obstaculo import Obstaculo

def main():
    player = Player()
    orientadora = Orientadora(player)

    player_group = pygame.sprite.GroupSingle(player)
    orientadora_group = pygame.sprite.GroupSingle(orientadora)
    obstaculos_group = pygame.sprite.Group()

    run = True
    game_active = True
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
            if spawn_timer > SPAWN_INTERVAL:
                obstaculo = Obstaculo(WIDTH)
                obstaculos_group.add(obstaculo)
                spawn_timer = 0

            # Aumenta velocidade se player estiver parado no centro
            if player.at_limit:
                obstacle_speed = BASE_OBSTACLE_SPEED + 2
            else:
                obstacle_speed = BASE_OBSTACLE_SPEED

            obstaculos_group.update(obstacle_speed)

            # Colisão com Orientadora (com máscara)
            if pygame.sprite.spritecollide(player, orientadora_group, False, pygame.sprite.collide_mask):
                game_active = False

            # Colisão com Obstáculos (somente se chegou ao centro)
            if player.at_limit:
                # Aqui, 'True' faz com que o obstáculo seja removido do grupo ao colidir
                collisions = pygame.sprite.spritecollide(player, obstaculos_group, True, pygame.sprite.collide_mask)
                if collisions:
                    # Se houve colisão, aplicamos o knockback
                    player.knockback()

            # Desenho na tela
            screen.fill(WHITE)
            player_group.draw(screen)
            orientadora_group.draw(screen)
            obstaculos_group.draw(screen)

            # Exibir pontuação e debug de spawn
            text_surface = FONT.render(f"Tempo: {score} | Spawn: {spawn_timer}", True, BLACK)
            screen.blit(text_surface, (10, 10))

        else:
            # Tela de Game Over
            screen.fill(WHITE)
            msg = FONT_LARGE.render("Game Over! Pressione qualquer tecla para reiniciar", True, BLACK)
            screen.blit(msg, (50, HEIGHT // 2))

            keys = pygame.key.get_pressed()
            if any(keys):
                # Reinicia o jogo
                game_active = True
                score = 0
                spawn_timer = 0
                obstaculos_group.empty()
                player.rect.midbottom = (200, HEIGHT)
                orientadora.rect.midbottom = (50, HEIGHT)
                # Velocidade inicial do player
                player.speed_x = 2
                player.at_limit = False

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
