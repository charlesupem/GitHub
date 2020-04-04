import pygame
from game import Game

pygame.init()

# Setup
screen = pygame.display.set_mode((800, 600))

background = pygame.image.load('assets/bg1.jpg')
icon = pygame.image.load('assets/ufo.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('Space Invader')

shoot_sound = pygame.mixer.Sound('assets/sounds/tir.ogg')
shoot_sound.set_volume(0.2)


game = Game()

loop = game.player.stop

while not loop:

    screen.blit(background, (0, 0))
    screen.blit(game.font.render("Score : " + str(game.score), True, (156, 232, 255)), (0, 0))
    screen.blit(game.player.image, game.player.rect)

    for bullet in game.player.allBullet:
        bullet.move()

    for ufo in game.allUfo:
        ufo.move()

    game.player.allBullet.draw(screen)
    game.allUfo.draw(screen)

    if game.pressed.get(pygame.K_d) and game.player.rect.x + game.player.image.get_width() < 800:
        game.player.move_right()
    elif game.pressed.get(pygame.K_a) and game.player.rect.x > 0:
        game.player.move_left()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False

        if event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            game.player.launchBullet()
            shoot_sound.play()

    game.player.checkgame()
    loop = game.player.stop
    pygame.display.update()

