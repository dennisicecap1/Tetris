import pygame
import random

# creating the data structure for pieces
# setting up global vars
# functions
# - create_grid
# - draw_grid
# - draw_window
# - rotating shape in main
# - setting up the main

"""
10 x 20 square grid
shapes: S, Z, I, O, J, L, T
represented in order by 0 - 6
"""

pygame.font.init ()

# GLOBALS VARS
s_width = 800
s_height = 700
play_width = 300  # meaning 300 // 10 = 30 width per block
play_height = 600  # meaning 600 // 20 = 20 height per block
block_size = 30

screen = pygame.display.set_mode((s_width, s_height))


top_left_x = (s_width - play_width) // 2
top_left_y = s_height - play_height

font = pygame.font.SysFont ('Calibri', 40)

# SHAPE FORMATS

S = [['....',
      '.....',
      '..00.',
      '.00..',
      '....'],
     ['....',
      '.0..',
      '.00.',
      '..0.',
      '....']]

Z = [['....',
      '....',
      '.00.',
      '..00',
      '....'],
     ['....',
      '..0.',
      '.00.',
      '.0..',
      '....']]

I = [['..0.',
      '..0.',
      '..0.',
      '..0.',
      '....'],
     ['....',
      '0000',
      '....',
      '....',
      '....']]

O = [['....',
      '....',
      '.00.',
      '.00.',
      '....']]

J = [['....',
      '.0..',
      '.000',
      '....',
      '....'],
     ['....',
      '..00',
      '..0.',
      '..0.',
      '....'],
     ['....',
      '....',
      '.000',
      '...0',
      '....'],
     ['....',
      '..0.',
      '..0.',
      '.00.',
      '....']]

L = [['....',
      '...0',
      '.000',
      '....',
      '....'],
     ['....',
      '..0.',
      '..0.',
      '..00',
      '....'],
     ['....',
      '....',
      '.000',
      '.0..',
      '....'],
     ['....',
      '.00.',
      '..0.',
      '..0.',
      '....']]

T = [['....',
      '..0.',
      '.000',
      '....',
      '....'],
     ['....',
      '..0.',
      '..00',
      '..0.',
      '....'],
     ['....',
      '....',
      '.000',
      '..0.',
      '....'],
     ['....',
      '..0.',
      '.00.',
      '..0.',
      '....']]

shapes = [S, Z, I, O, J, L, T]
# shapes = [O]
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (50, 50, 255), (255, 0, 255)]


# index 0 - 6 represent shape

def game_over(score):
    black = (0, 0, 0)

    font = pygame.font.SysFont('Calibri', 100)
    restart_font = pygame.font.SysFont('Calibri', 40)

    over_text = font.render("GAME OVER!", True, (255, 0, 0))
    final_score = font.render ('Score: ' + str (score), True, (255, 255, 0))
    restart = restart_font.render ('Press Y to restart and N to quit', True, (0, 255, 0))

    while True:
        screen.fill(black)
        screen.blit (over_text, (100, 200))
        screen.blit (final_score, (100, 300))
        screen.blit (restart, (100, 400))
        pygame.display.update()

        for x in pygame.event.get ():
            if x.type == pygame.QUIT:
                pygame.quit ()
                quit ()
            if x.type == pygame.KEYDOWN:
                if pygame.K_q == x.key:
                    pygame.quit()
                    quit ()
                if pygame.K_n == x.key:
                    pygame.quit ()
                    quit ()
                if pygame.K_y == x.key:
                    main_menu ()

def choose_random(new_shape):
    if new_shape == True:
        chosen_shape = random.choice(shapes)
    else:
        chosen_shape = chosen_shape

def draw_old(positions, positions_colours):
    for y, x in enumerate(positions):
        pygame.draw.rect (screen, (positions_colours[y]), (x[0], x[1], 30, 30))

def small_shape(next_shape_type):
    shape = next_shape_type[0]

    new_shape = []
    row = 0
    for x in shape:
        row += 1
        column = 0
        for y in x:
            column += 1
            if y == "0":
                row_column = [row * 15, column * 15]
                new_shape.append (row_column)

    shape_colour = shape_colors[shapes.index (next_shape_type)]

    for x in new_shape:
        pygame.draw.rect (screen, (255, 255, 255), (620 + x[0], 300 + x[1], 15, 15))



# def convert_shape_format(shape, rotations, rotate, z, location_x, location_y, corner):
#     placement = []
#
#     row = 0
#     for x in z[rotations]:
#         column = 0
#         for y in x:
#             if y == 1:
#                 xy = []
#                 x_place = row * 40
#                 y_place = column * 40
#
#                 if len(location_x) > 0:
#                     x_place += corner[0][0]
#                     y_place += corner[0][1]
#
#                 xy = [x_place, y_place]
#
#                 placement.append (xy)
#             if y == 2:
#                 x_corner = row * 40
#                 y_corner = column * 40
#                 xy_corner = [x_corner, y_corner]
#                 corner.append(xy_corner)
#                 if len(corner) > 1:
#                     del corner[-1]
#             column += 1
#         row += 1
#
#     return placement, corner


def get_shape(current_shape_type, rotate_shape, shape_type, rotations, rotate_xy):
    if rotate_shape == False:
        shape_type = current_shape_type
        shape = shape_type[0]
        new_shape = []

        row = 0
        for x in shape:
            row += 1
            column = 0
            for y in x:
                column += 1
                if y == "0":
                    row_column = [row * 30, column * 30]
                    new_shape.append (row_column)


    elif rotate_shape == True:
        shape = shape_type[rotations]
        new_shape = []

        row = 0
        for x in shape:
            row += 1
            column = 0
            for y in x:
                column += 1
                if y == "0":
                    row_column = [row * 30 + int(rotate_xy[0]), column * 30 + int(rotate_xy[1])]
                    new_shape.append (row_column)

    return(new_shape, shape_type)

def draw_grid(surface):
    for i in range (11):
        x_line = i * 30
        pygame.draw.line (screen, (255, 255, 255), (x_line + 250, 100), (x_line + 250, 700))
    for i in range (21):
        y_line = i * 30
        pygame.draw.line (screen, (255, 255, 255), (250, y_line + 100), (550, y_line + 100))


def clear_rows(positions, positions_colours, removal_locations):
    new_list = []
    new_colours = []
    for q, p in enumerate (positions):
        if int (p[1]) != int (removal_locations):
            new_list.append (p)
            new_colours.append (positions_colours[q])

    for z, y in enumerate (new_list):
        if y[1] < removal_locations:
            new_list[z][1] = int (new_list[z][1] + 30)

    return new_list, new_colours

def check_rows(positions, positions_colours, score):
    check_clear_row = []
    row_delete = []
    new_list = []
    removal_locations = 0

    for c in positions:
        check_clear_row.append (c[1])
        if check_clear_row.count (c[1]) == 10:
            row_delete.append(c[1])

    if len(row_delete) == 1:
        score += 40
    if len(row_delete) == 2:
        score += 100
    if len(row_delete) == 3:
        score += 300
    if len(row_delete) == 4:
        score += 1200


    if len(row_delete) == 0:
        new_list = positions
        new_colours = positions_colours
    else:
        for x in range(len(row_delete)):
            removal_locations = row_delete[x]
            stuff = clear_rows (positions, positions_colours, removal_locations)
            new_list = stuff[0]
            new_colours = stuff[1]

            positions_colours = new_colours
            positions = new_list

    newer_list = []
    newer_colour = []
    for j, i in enumerate(positions):
        if i not in newer_list:
            newer_list.append(i)
            newer_colour.append(positions_colours[j])

    positions = newer_list
    positions_colours = newer_colour




    return positions, positions_colours, score

def main():
    location_x = [400]
    location_y = [100]

    positions = []
    positions_colours = []
    corner = []
    finished_shapes = []

    game = True

    surface = None

    rotations = 0
    time_down = 0
    time = 0
    rotate = False
    go_down = False
    call_rotate = False
    stop_move = False
    right = None
    left = None

    black = (0, 0, 0)

    require_shape = True
    next_shape_type = random.choice(shapes)

    rotation_x = 0
    rotation_y = 0

    rotate_shape = False
    shape_type = None
    rotations = 0
    rotate_xy = ()

    down = False

    y_values = []

    score = 0

    while True:
        if 100 in y_values:
            game_over(score)

        current_x = 0
        current_y = 0

        removal = False

        screen.fill (black)

        for x in pygame.event.get ():
            if x.type == pygame.QUIT:
                pygame.quit ()
                quit ()
            if x.type == pygame.KEYDOWN:
                if pygame.K_q == x.key:
                    end = False
                    pygame.quit ()
                    quit ()
                if pygame.K_UP == x.key:
                    rotate = True
                if pygame.K_LEFT == x.key:
                    left = True
                if pygame.K_RIGHT == x.key:
                    right = True
                if pygame.K_DOWN == x.key:
                    down = True
            if x.type == pygame.KEYUP:
                if pygame.K_DOWN == x.key:
                    down = False

        if require_shape:
            current_shape_type = next_shape_type
            no_rotate = 0
            test_current = None
            rotate_shape = False
            recieve_shape = get_shape(current_shape_type, rotate_shape, shape_type, rotations, rotate_xy)
            current_shape = recieve_shape[0]
            shape_type = recieve_shape[1]
            next_shape_type = random.choice(shapes)


            current_x += 310
            current_y += -50
            require_shape = False

            small_shape(next_shape_type)

        if rotate == True:
            no_rotate = 0
            rotations -= 1
            if rotations < -(int(len(shape_type)) - 1):
                rotations = 0

            rotate_xy = [rotation_x, rotation_y]

            rotate_shape = True
            recieve_shape = get_shape (current_shape_type, rotate_shape, shape_type, rotations, rotate_xy)
            test_current = recieve_shape[0]
            for x in test_current:
                if x in positions:
                    no_rotate += 1
                if x[0] <= 220:
                    no_rotate += 1
                if x[0] >= 550:
                    no_rotate += 1

            if no_rotate == 0:
                current_shape = recieve_shape[0]
                shape_type = recieve_shape[1]

            rotate = False
            rotate_shape = False

        if right == True:
            go_right = 0
            before_wall = 0
            for s in current_shape:
                location_x = s[0]
                location_y = s[1]
                location = [location_x + 30, location_y]
                if location in positions:
                    go_right += 1
                if (s[0] + 30) >= 550:
                    before_wall += 1
            if go_right == 0 and before_wall == 0:
                current_x += 30
                right = None
            else:
                right == None
                pass

        if left == True:
            go_left = 0
            before_wall = 0
            for s in current_shape:
                location_x = s[0]
                location_y = s[1]
                location = [location_x - 30, location_y]
                if location in positions:
                    go_left += 1
                if (s[0] - 30) <= 220:
                    before_wall += 1
            if go_left == 0 and before_wall == 0:
                current_x -= 30
                left = None
            else:
                left == None
                pass

        time_down += 1
        if down == True:
            time_down += 5
        if time_down >= 250:
            skip_down = False
            for s in current_shape:
                location_y = s[1]
                if [s[0], s[1] + 30] in positions:
                    rotation_x = 0
                    rotation_y = 0
                    for x in current_shape:
                        xy = [x[0], x[1]]
                        if xy not in positions:
                            positions.append (xy)
                            positions_colours.append (shape_colour)
                            y_values.append (x[1])
                    require_shape = True
                    time_down = 0
                    skip_down = True
                    down = False
                    removal = True

                    break

                if location_y + 30 >= 700:
                    rotation_x = 0
                    rotation_y = 0
                    for x in current_shape:
                        xy = [x[0], x[1]]
                        if xy not in positions:
                            positions.append (xy)
                            positions_colours.append(shape_colour)
                            y_values.append(x[1])
                    require_shape = True
                    time_down = 0
                    skip_down = True
                    down = False

                    removal = True

                    break
            if skip_down == False:
                current_y += 30
                time_down = 0

        if removal == True:
            for x in range(2):
                after_remove = check_rows (positions, positions_colours, score)
                positions = after_remove[0]
                positions_colours = after_remove[1]
                score = after_remove[2]
            removal = False

        shape_number = shapes.index(shape_type)
        shape_colour = shape_colors[shape_number]
        shape_squares = len (current_shape)
        for z in range (shape_squares):
            current_shape[z][0] += current_x
            current_shape[z][1] += current_y
            pygame.draw.rect (screen, (shape_colour), (current_shape[z][0], current_shape[z][1], 30, 30))
        rotation_x += current_x
        rotation_y += current_y

        screen_score = font.render ('Score: ' + str(score), True, (150, 150, 150))
        screen.blit(screen_score, (50, 300))

        next_shape_text = font.render ('Next Shape:', True, (255, 255, 255))
        screen.blit (next_shape_text, (580, 250))

        draw_old (positions, positions_colours)
        draw_grid(surface)
        pygame.draw.rect (screen, (0, 0, 0), (0, 0, 800, 100))
        small_shape (next_shape_type)
        pygame.display.update ()


def main_menu():
    black = (0, 0, 0)

    font = pygame.font.SysFont('Calibri', 100)
    start_font = pygame.font.SysFont('Calibri', 40)


    start_text = font.render("Welcome to Tetris!", True, (0, 255, 255))
    start = start_font.render ('Press Y to start and N to quit', True, (0, 255, 0))

    while True:
        screen.fill(black)
        screen.blit (start_text, (30, 200))
        screen.blit (start, (30, 300))

        for x in pygame.event.get ():
            if x.type == pygame.QUIT:
                pygame.quit ()
                quit ()
            if x.type == pygame.KEYDOWN:
                if pygame.K_q == x.key:
                    pygame.quit()
                    quit ()
                if pygame.K_n == x.key:
                    pygame.quit ()
                    quit ()
                if pygame.K_y == x.key:
                    main()

        pygame.display.update()


main_menu ()  # start game