import pygame
from puzzel_maker import Puzzel
from time import sleep

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

def check_input(puzzel, x, y, font, inputs, blue, gray, num):
    index = puzzel.check_spot_empty(x, y)
    if index:
        if index == 17:
            index = 0
        if puzzel.check_guess(num, index):
            print('correct!')
            new = font.render(f'{num}', True, blue)
            newRect = new.get_rect()
            newRect.center = x + 60, y + 60
        else:
            new = font.render(f'{num}', True, gray)
            newRect = new.get_rect()
            newRect.center = x + 60, y + 60
        inputs[index] = (new, newRect)
    print(inputs)

        

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
    print(puzzel.game_board)
    print(len(square_positions))



    border_color = (255, 0, 0)
    selected = (252, 186, 3)

    gray = (165, 166, 181)
    white = (255, 255, 255)
    blue = (86, 181, 240)

    
    font = pygame.font.SysFont('calisto', 80)
    # text = font.render('4', True, white)
    # textRect = text.get_rect()
    # textRect.center = 300, 300

    start_text = setup_start_text(puzzel, font, white, square_positions)

    exit = font.render('Great Job!', True, selected)
    exitRect = exit.get_rect()
    exitRect.center = 300, 300

    min_limit = 50
    max_limit = 425

    
    selected_square = pygame.Rect(50, 50, 125, 125)
    outer_borders = position_outer_borders()
    inner_borders = position_inner_borders()
    
    inputs = {}


    running = True
    solved = False
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:

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
                    check_input(puzzel, x, y, font, inputs, blue, gray, 1)
                    
                if event.key == pygame.K_2:
                    x = selected_square.x
                    y = selected_square.y
                    print("pushed 2")
                    check_input(puzzel, x, y, font, inputs, blue, gray, 2)

                if event.key == pygame.K_3:
                    x = selected_square.x
                    y = selected_square.y
                    print("pushed 3")
                    check_input(puzzel, x, y, font, inputs, blue, gray, 3)

                if event.key == pygame.K_4:
                    x = selected_square.x
                    y = selected_square.y
                    print("pushed 4")
                    check_input(puzzel, x, y, font, inputs, blue, gray, 4)

            if puzzel.check_solved() == True:
                running = False
                solved = True


        screen.fill((0, 0, 0))
        
        for o_border in outer_borders:
            pygame.draw.rect(screen, border_color, o_border, 1)
        for border in inner_borders:
            pygame.draw.rect(screen, border_color, border)
        for element in start_text:
            num, space = element
            screen.blit(num, space)
        for element in inputs.values():
            num, space = element
            screen.blit(num, space)
        pygame.draw.rect(screen, selected, selected_square, 2)
        if solved:
            screen.blit(exit, exitRect)

        pygame.display.flip()
        
        if solved:
            pygame.time.delay(1000)
        

    pygame.quit()


main()