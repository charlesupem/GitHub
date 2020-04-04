import pygame
from bullet import Bullet


class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 370
        self.rect.y = 530
        self.velocity = 2
        self.attack = 100

        self.allBullet = pygame.sprite.Group()
        self.stop = False

    def checkgame(self):
        if self.game.checkCollision(self, self.game.allUfo):
            self.stop = True
            print('GAME OVER !')
        elif len(self.game.allUfo) == 0:
            print('Fin du niveau.')
            self.stop = True

    def launchBullet(self):
        self.allBullet.add(Bullet(self, self.game))

    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity
