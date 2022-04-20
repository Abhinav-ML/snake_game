import pygame

pygame.init()

# Colors
white = (255, 255, 255)
green = (255, 0, 0)
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
fps = 30

velocity_x = 1
velocity_y = 1


# Game Loop
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
        # Event handling
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake_x = snake_x + 10
            if event.key == pygame.K_LEFT:
                snake_x = snake_x - 10
            if event.key == pygame.K_UP:
                snake_y = snake_y - 10
            if event.key == pygame.K_DOWN:
                snake_y = snake_y + 10

    snake_x += velocity_x
    snake_y += velocity_y

    gameWindow.fill(white)
    pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])
    pygame.display.update()
    clock.tick(fps)
