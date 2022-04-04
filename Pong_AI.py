import pygame
from pong import Game

width, height = 700, 500
window = pygame.display.set_mode((width, height))

game = Game(window, width, height)

run = True
clock = pygame.time.Clock()
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

    game.loop()
    game.draw()
    pygame.display.update()

pygame.quit()