import pygame
import time

BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)

pygame.init()

screen = pygame.display.set_mode((640, 480))

pygame.display.set_caption('Simple Movement')

position_x = 0

velocity_x = 100

ti = time.time()

while True:

    tf = time.time()

    dt = (tf - ti)

    ti = tf



    event = pygame.event.poll()

    if event.type == pygame.QUIT:
        break


    position_x += velocity_x * dt

    if position_x >= 640:
        position_x = 0

    screen.fill(BLACK)

    pygame.draw.rect(screen, WHITE, [position_x, 230, 20, 20])

    pygame.display.flip()