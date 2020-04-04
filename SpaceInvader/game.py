import pygame
import random

from player import Player
from ufo import Ufo


class Game():

    def __init__(self):
        self.player = Player(self)
        self.pressed = {}
        self.allUfo = pygame.sprite.Group()
        self.spawn_ufo()
        self.score = 0
        self.font = pygame.font.Font('assets/font/game_over.ttf', 64)

    def spawn_ufo(self):
        for i in range(2, random.randint(0, 50)):
            ufo = Ufo()
            self.allUfo.add(ufo)

    def respawn(self):
        self.allUfo.add(Ufo())

    def checkCollision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, True, pygame.sprite.collide_mask)

