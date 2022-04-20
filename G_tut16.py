import pygame
import random

pygame.init()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# Game Window
window_width = 500
window_height = 300
gameWindow = pygame.display.set_mode((window_width, window_height))

# Game Title
pygame.display.set_caption(("The Snake Game"))
pygame.display.update()

# Game specific variables
exit_game = False
exit_over = False
snake_x = 50  # initial position  of snake along x axis
snake_y = 70  # initial position  of snake along y axis
snake_size = 10  # size of head(square)

clock = pygame.time.Clock()
fps = 60

velocity_x = 0
velocity_y = 0
init_velocity = 3

food_x = random.randint(0, window_width / 2)
food_y = random.randint(0, window_height / 2)

score = 0

# Game Loop
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
        # Event handling
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                velocity_x = init_velocity
                velocity_y = 0
            if event.key == pygame.K_LEFT:
                velocity_x = - init_velocity
                velocity_y = 0
            if event.key == pygame.K_UP:
                velocity_y = - init_velocity
                velocity_x = 0
            if event.key == pygame.K_DOWN:
                velocity_y = init_velocity
                velocity_x = 0

    snake_x += velocity_x
    snake_y += velocity_y
    if abs(snake_x - food_x) < 6 and abs(snake_y - food_y) < 6:
        score += 1
        print("Score :", score * 10)
        food_x = random.randint(0, window_width / 2)
        food_y = random.randint(0, window_height / 2)

    gameWindow.fill(white)
    pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])
    pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])
    pygame.display.update()
    clock.tick(fps)
