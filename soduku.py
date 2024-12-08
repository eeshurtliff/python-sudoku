import pygame

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Soduku")

border_color = (255, 0, 0)
selected = (252, 186, 3)
ball_color = (255, 255, 255)

min_limit = 50
max_limit = 425

border = pygame.Rect(50, 50, 500, 500)
left_square = pygame.Rect(50, 50, 250, 250)
right_square = pygame.Rect(300, 50, 250, 250)
lb_square = pygame.Rect(50, 300, 250, 250)
line = pygame.Rect(50, 175, 500, 1)
line2 = pygame.Rect(50, 425, 500, 1)
line3 = pygame.Rect(175, 50, 1, 500)
line4 = pygame.Rect(425, 50, 1, 500)
selected_square = pygame.Rect(50, 50, 125, 125)
rb_square = pygame.Rect(300, 300, 250, 250)

COMPLETE = [
    
]

# some soduku options to start with:



# edge = True

# ball_velocity = [5, 5]
# if selected_square.colliderect(border):
#     ball_velocity[0] = -ball_velocity[0]
    
# if ball.top <= 0 or ball.bottom >=600:
#     ball_velocity[1] = -ball_velocity[1]


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP and selected_square.y != 50:
                print("up arrow pressed")
                selected_square.move_ip((0, -125))
                # selected_y -= 50
            if event.key == pygame.K_DOWN and selected_square.y != 425:
                print("down arrow pressed")
                selected_square.move_ip((0, 125))
                # selected_y += 50
            if event.key == pygame.K_LEFT and selected_square.x != 50:
                print("left arrow pressed")
                selected_square.move_ip((-125, 0))
                # selected_x -= 50
            if event.key == pygame.K_RIGHT and selected_square.x != 425:
                print("right arrow pressed")
                selected_square.move_ip((125, 0))
                # selected_x += 50

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, border_color, border, 2)
    pygame.draw.rect(screen, border_color, left_square, 1)
    pygame.draw.rect(screen, border_color, right_square, 1)
    pygame.draw.rect(screen, border_color, rb_square, 1)
    pygame.draw.rect(screen, border_color, lb_square, 1)
    pygame.draw.rect(screen, border_color, line)
    pygame.draw.rect(screen, border_color, line2)
    pygame.draw.rect(screen, border_color, line3)
    pygame.draw.rect(screen, border_color, line4)
    pygame.draw.rect(screen, selected, selected_square, 2)
    
    pygame.display.flip()
pygame.quit()


