import pygame
from puzzel_maker import puzzel_details

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Sudoku")


square_positions = [
    (50, 50), (175, 50), (300, 50), (425, 50),
    (50, 175), (175, 175), (300, 175), (425, 175),
    (50, 300), (175, 300), (300, 300), (425, 300),
    (50, 425), (175, 425), (300, 425), (425, 425),
]



border_color = (255, 0, 0)
selected = (252, 186, 3)
ball_color = (255, 255, 255)

white = (255, 255, 255)
blue = (0, 0, 128)

print(pygame.font.get_fonts())
font = pygame.font.SysFont('calisto', 80)
text = font.render('4', True, white)
textRect = text.get_rect()
textRect.center = 300, 300

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


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP and selected_square.y != 50:
                selected_square.move_ip((0, -125))
                # selected_y -= 50
            if event.key == pygame.K_DOWN and selected_square.y != 425:
                selected_square.move_ip((0, 125))
                # selected_y += 50
            if event.key == pygame.K_LEFT and selected_square.x != 50:
                selected_square.move_ip((-125, 0))
                # selected_x -= 50
            if event.key == pygame.K_RIGHT and selected_square.x != 425:
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
    screen.blit(text, textRect)

    
    pygame.display.flip()
pygame.quit()


