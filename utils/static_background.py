import pygame
import random

class Background:
    def __init__(self, screen_width, screen_height):
        """Inicializa o fundo com nuvens em posições aleatórias."""
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.clouds = []
        self.cloud_speed = 2  # Velocidade de movimento das nuvens
        self.cloud_images = [
            pygame.image.load("assets/nuvem.png").convert_alpha(),
            pygame.image.load("assets/nuvem.png").convert_alpha(),
        ]
        # Escala as imagens das nuvens para um tamanho adequado
        self.cloud_images = [pygame.transform.scale(img, (150, 100)) for img in self.cloud_images]
        self.initialize_clouds()

    def initialize_clouds(self):
        """Cria nuvens iniciais espalhadas pela tela."""
        for _ in range(5):  # Número de nuvens
            x = random.randint(0, self.screen_width)
            y = random.randint(50, self.screen_height // 2)
            cloud_img = random.choice(self.cloud_images)
            self.clouds.append({"image": cloud_img, "x": x, "y": y})

    def update(self):
        """Atualiza a posição das nuvens, movendo-as para a esquerda."""
        for cloud in self.clouds:
            cloud["x"] -= self.cloud_speed
            # Se a nuvem sair da tela pela esquerda, reposiciona à direita
            if cloud["x"] < -150:  # Considera a largura da nuvem
                cloud["x"] = self.screen_width
                cloud["y"] = random.randint(50, self.screen_height // 2)
                cloud["image"] = random.choice(self.cloud_images)

    def draw(self, screen):
        """Desenha as nuvens na tela."""
        for cloud in self.clouds:
            screen.blit(cloud["image"], (cloud["x"], cloud["y"]))