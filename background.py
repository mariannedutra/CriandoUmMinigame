# background.py
import pygame, random, os
from pathlib import Path
from typing import Sequence

class Background:
    """
    Controla o cenário de fundo + nuvens + rochas.
    Todas as imagens em assets/backgrounds/ (*.png, *.jpg, *.jpeg)
    são carregadas e alternadas a cada BG_CHANGE_INTERVAL milissegundos.
    """

    # ---------------- configuração visual ----------------
    CLOUD_SPEED   = 120          # px/s
    NUM_CLOUDS    = 5
    NUM_ROCKS     = 5
    BG_CHANGE_INTERVAL = 3_000  # ms (12 s)

    # ------------------------------------------------------
    def __init__(self,
                 screen_width: int,
                 screen_height: int,
                 bg_dir: str | Path = "assets/backgrounds") -> None:

        self.w, self.h = screen_width, screen_height
        self.clock = pygame.time.get_ticks  # atalho

        # 1. carregar TODOS os arquivos de imagem na pasta
        self.bg_images = self._load_backgrounds(bg_dir)
        if not self.bg_images:
            raise FileNotFoundError(
                f"Nenhuma imagem .png/.jpg encontrada em {bg_dir}"
            )

        self.bg_index = 0
        self.next_bg_switch = self.clock() + self.BG_CHANGE_INTERVAL

        # 2. nuvens
        cloud_raw = pygame.image.load("assets/nuvem.png").convert_alpha()
        cloud_raw = pygame.transform.scale(cloud_raw, (150, 100))
        self.cloud_images = [cloud_raw]
        self.clouds: list[dict] = []
        self._init_clouds()

        # 3. rochas
        rock_raw = pygame.image.load("assets/pedra.png").convert_alpha()
        rock_raw = pygame.transform.scale(rock_raw, (80, 100))
        self.rock_images = [rock_raw]
        self.rocks: list[dict] = []
        # self._init_rocks()

    # ------------------------------------------------------
    #   utilitário: varrer diretório de fundos
    # ------------------------------------------------------
    def _load_backgrounds(self, bg_dir: str | Path) -> list[pygame.Surface]:
        """Lê todas as imagens .png/.jpg/.jpeg do diretório informado."""
        bg_dir = Path(bg_dir)
        valid_ext = {".png", ".jpg", ".jpeg"}
        surfaces: list[pygame.Surface] = []

        if not bg_dir.exists():
            print(f"[Background] pasta {bg_dir} não encontrada.")
            return surfaces

        for file in sorted(bg_dir.iterdir()):
            if file.suffix.lower() in valid_ext:
                img = pygame.image.load(file).convert()
                img = pygame.transform.scale(img, (self.w, self.h))
                surfaces.append(img)

        return surfaces

    # ------------------------------------------------------
    #   inicialização de nuvens e rochas
    # ------------------------------------------------------
    def _init_clouds(self) -> None:
        for _ in range(self.NUM_CLOUDS):
            x = random.randint(0, self.w)
            y = random.randint(50, self.h // 2)
            self.clouds.append({"image": random.choice(self.cloud_images),
                                "x": x, "y": y})

    def _init_rocks(self) -> None:
        ground = self.h - 90
        for _ in range(self.NUM_ROCKS):
            x = random.randint(0, self.w)
            y = ground + random.randint(-10, 10)
            self.rocks.append({"image": random.choice(self.rock_images),
                               "x": x, "y": y})

    # ------------------------------------------------------
    #   atualização (troca de fundo + parallax)
    # ------------------------------------------------------
    def update(self, dt: float) -> None:
        # troca automática de fundo
        if self.clock() >= self.next_bg_switch:
            self.bg_index = (self.bg_index + 1) % len(self.bg_images)
            self.next_bg_switch = self.clock() + self.BG_CHANGE_INTERVAL

        # deslocamento lateral
        dx = self.CLOUD_SPEED * dt
        for cloud in self.clouds:
            cloud["x"] -= dx
            if cloud["x"] < -150:
                cloud["x"] = self.w
                cloud["y"] = random.randint(50, self.h // 2)

        for rock in self.rocks:
            rock["x"] -= dx
            if rock["x"] < -80:
                rock["x"] = self.w
                ground = self.h - 90
                rock["y"] = ground + random.randint(-10, 10)

    # ------------------------------------------------------
    #   renderização
    # ------------------------------------------------------
    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.bg_images[self.bg_index], (0, 0))

        for cloud in self.clouds:
            screen.blit(cloud["image"], (cloud["x"], cloud["y"]))

        for rock in self.rocks:
            screen.blit(rock["image"], (rock["x"], rock["y"]))
