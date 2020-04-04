import pygame
import random


class Ufo(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.velocity = 3

        self.image = pygame.image.load('assets/ufo.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 800)
        self.rect.y = random.randint(0, 100)

        self.dir = 'right'

    def right(self):
        self.rect.x += self.velocity

    def left(self):
        self.rect.x -= self.velocity

    def down(self):
        self.rect.y += 100

    def detection(self):

        if self.dir == 'right' and self.rect.x >= 800 - self.image.get_width():
            self.down()
            self.dir = 'left'

        if self.dir == 'left' and self.rect.x <= 0:
            self.down()
            self.dir = 'right'

    def move(self):

        self.detection()

        if self.dir == 'right':
            self.right()

        elif self.dir == 'left':
            self.left()