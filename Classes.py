import pygame
import sys
from pygame.locals import *
import random
import time
screen = pygame.display.set_mode((800, 600))


def timer():
    now = time.localtime(time.time())
    return now[5]


class Aliens(pygame.sprite.Sprite):
    initial_time = 0
    time = 0

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Alien.png")
        self.img_height = self.image.get_height()
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 800, self.img_height)
        self.rect.y = random.randrange(0, (self.img_height+1), self.img_height)
        self.flag = 0

    def blit(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        self.image = pygame.image.load("Alien1.png")
        self.initial_time = timer() - 3
        self.flag = 1


class Shoot(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Shooter.png")
        self.rect = self.image.get_rect()
        self.rect.y = screen.get_height() - self.image.get_height()
        self.x_velocity = 0
        self.rect.x = screen.get_width()/2 - self.image.get_width()/2


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.y -= 3


class Faltu_Bullet(Bullet):
    def __init__(self, x, y):
        self.image = pygame.image.load("FBullet.png")
        super().__init__(x, y)

    def update(self):
        self.rect.y -= 6


class Asli_Bullet(Bullet):
    def __init__(self, x, y):
        self.image = pygame.image.load("Bullet.png")
        super().__init__(x, y)
