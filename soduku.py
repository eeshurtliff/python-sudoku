import pygame
from puzzel_maker import Puzzel

def position_outer_borders():
    border = pygame.Rect(50, 50, 500, 500)
    left_top = pygame.Rect(50, 50, 250, 250)
    right_top = pygame.Rect(300, 50, 250, 250)
    left_bottom = pygame.Rect(50, 300, 250, 250)
    right_bottom = pygame.Rect(300, 300, 250, 250)

    borders = [border, left_top, right_top, left_bottom, right_bottom]
    return borders


def position_inner_borders():
    
    line = pygame.Rect(50, 175, 500, 1)
    line2 = pygame.Rect(50, 425, 500, 1)
    line3 = pygame.Rect(175, 50, 1, 500)
    line4 = pygame.Rect(425, 50, 1, 500)
   
    borders = [line,line2, line3, line4 ]
    return borders

def setup_start_text(puzzel, font, color, sq_positions):
    start_text = []
    for i in range(len(sq_positions)):
        num = puzzel.start_puzzel[i]
        if num != 0:
            text = font.render(str(num), True, color)
            textRect = text.get_rect()
            x, y = sq_positions[i]
            textRect.center = x+60, y+60
            start_text.append((text, textRect))
    return start_text

def check_empty(puzzel, square_positions, x, y):
    selected = (x, y)
    spot_index = square_positions.index(selected)
    if puzzel.start_puzzel[spot_index] == 0:
        return True
    return False

def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("4x4 Sudoku")


    square_positions = [
        (50, 50), (175, 50), (300, 50), (425, 50),
        (50, 175), (175, 175), (300, 175), (425, 175),
        (50, 300), (175, 300), (300, 300), (425, 300),
        (50, 425), (175, 425), (300, 425), (425, 425),
    ]


    puzzel = Puzzel(square_positions)
    print(puzzel.start_puzzel)
    print(len(square_positions))



    border_color = (255, 0, 0)
    selected = (252, 186, 3)
    ball_color = (255, 255, 255)

    white = (255, 255, 255)
    blue = (0, 0, 128)

    
    font = pygame.font.SysFont('calisto', 80)
    # text = font.render('4', True, white)
    # textRect = text.get_rect()
    # textRect.center = 300, 300

    start_text = setup_start_text(puzzel, font, white, square_positions)

    min_limit = 50
    max_limit = 425

    
    selected_square = pygame.Rect(50, 50, 125, 125)
    outer_borders = position_outer_borders()
    inner_borders = position_inner_borders()
    



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
                if event.key == pygame.K_1:
                    x = selected_square.x
                    y = selected_square.y
                    print("pushed 1")
                    print(check_empty(puzzel, square_positions, x, y))

        screen.fill((0, 0, 0))

        
        for o_border in outer_borders:
            pygame.draw.rect(screen, border_color, o_border, 1)
        for border in inner_borders:
            pygame.draw.rect(screen, border_color, border)
        for element in start_text:
            num, space = element
            screen.blit(num, space)
        pygame.draw.rect(screen, selected, selected_square, 2)
        # screen.blit(text, textRect)

        
        pygame.display.flip()
    pygame.quit()


main()