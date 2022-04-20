import pygame
import random

pygame.init()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# Game Window
window_width = 900
window_height = 400
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

font = pygame.font.SysFont(None, 55)


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text,[x,y])

def plot_snake(gameWindow,color,snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size,snake_size])



snk_length = 1
snk_list = []
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
        # print("Score :", score * 10)

        food_x = random.randint(0, window_width / 2)
        food_y = random.randint(0, window_height / 2)
        snk_length += 5

    gameWindow.fill(white)
    text_screen("Score :" + str(score * 10), red, 5, 5)
    pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])


    head = []
    head.append(snake_x)
    head.append(snake_y)
    snk_list.append(head)

    if len(snk_list)>snk_length:
        del snk_list[0]

    # pygame.draw.rect(gameWindow, black, snake_x, snake_y, snake_size)
    plot_snake(gameWindow, black,snk_list,snake_size)
    pygame.display.update()
    clock.tick(fps)


pygame.quit()
quit()
