import pygame
from .enemy import Enemy

imgs = []
for x in range(4):
    add_str = str(x)
    if x < 4:
        add_str = "0" + add_str
    imgs.append(pygame.transform.scale(pygame.image.load(r'D:\Projects\game-cad\game_assets\enemies_images\zombie\character_zombie_attack0.png'),(64, 64)))

class Zombie(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "zombie"
        self.money = 1
        self.max_health = 1
        self.health = self.max_health
        self.imgs = imgs[:]