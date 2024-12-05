import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pong")

paddle_color = (255, 0, 0)

ball_color = (255, 255, 255)

paddle1 = pygame.Rect(50, 250, 10, 100)
paddle2 = pygame.Rect(740, 250, 10, 100)
ball = pygame.Rect(390, 290, 20, 20)



ball_velocity = [5, 5]
if ball.colliderect(paddle1) or ball.colliderect(paddle2):
    ball_velocity[0] = -ball_velocity[0]
if ball.top <= 0 or ball.bottom >=600:
    ball_velocity[1] = -ball_velocity[1]


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.draw.rect(screen, paddle_color, paddle1)
    pygame.draw.rect(screen, paddle_color, paddle2)
    pygame.draw.rect(screen, ball_color, ball)
    pygame.display.flip()
pygame.quit()
