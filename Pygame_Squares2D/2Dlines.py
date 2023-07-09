import pygame
import math
from random import randrange

#Lattice setup
X_squares = 33
Y_squares = 33

square_size = 30
border_width = 3

X_screen_size = X_squares*(square_size+border_width)
Y_screen_size = Y_squares*(square_size+border_width)

X_middle = math.floor(X_squares/2)
Y_middle = math.floor(Y_squares/2)

square_start_color = pygame.Color(100,100,100,255)

def draw_square(X,Y,color):
    X_cord = X*(square_size+border_width)+border_width
    Y_cord = Y*(square_size+border_width)+border_width
    pygame.draw.rect(screen, color, pygame.Rect(X_cord, Y_cord, square_size, square_size))

def recurent_maze(prev_X, prev_Y,X,Y,color,depth):
    draw_square(X,Y,color)
    if depth >= 15:
        return
    X_vect = X - prev_X
    Y_vect = Y - prev_Y
    print(X_vect, Y_vect)
    rand = randrange(0,100,1)
    color = fade_color(color)
    if (0 <= rand < 80):
        recurent_maze(X, Y, X+X_vect, Y+Y_vect, color ,depth+1)
    if ((80 <= rand < 90) or (0<= rand <= 5)):
        recurent_maze(X, Y, X+Y_vect, Y+X_vect, color,depth+1)
    if ((90 <= rand <= 100) or (5<= rand <= 10)):
        recurent_maze(X, Y, X-Y_vect, Y-X_vect, color,depth+1)
    if (999 <= rand <= 999):
        recurent_maze(X, Y, X-X_vect, Y-Y_vect, color,depth+1)

def fade_color(color):
    max_change = 20

    r = color.r
    g = color.g
    b = color.b
    diff = randrange(-max_change,max_change,1)
    r += diff
    if r > 255:
        r = 255
    if r < 0:
        r = 0
    diff = randrange(-max_change,max_change,1)
    g += diff
    if g > 255:
        g = 255
    if g < 0:
        g = 0
    diff = randrange(-max_change,max_change,1)
    b += diff
    if b > 255:
        b = 255
    if b < 0:
        b = 0
    #print(r, g, b)
    new_color = pygame.Color(r,g,b)
    return new_color

# pygame setup
pygame.init()
screen = pygame.display.set_mode((X_screen_size, Y_screen_size))
clock = pygame.time.Clock()
running = True
dt = 0

start_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    #Draw background lattice
    for i in range(X_squares):
        for j in range(Y_squares):
            draw_square(i,j, pygame.Color(30,30,30))

    #Draw start square
    draw_square(X_middle, Y_middle,square_start_color)
    recurent_maze(X_middle, Y_middle,X_middle+1,Y_middle, square_start_color,1)
    recurent_maze(X_middle, Y_middle,X_middle-1,Y_middle, square_start_color,1)
    recurent_maze(X_middle, Y_middle,X_middle,Y_middle+1, square_start_color,1)
    recurent_maze(X_middle, Y_middle,X_middle,Y_middle-1, square_start_color,1)
      

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(1) / 1000

pygame.quit()