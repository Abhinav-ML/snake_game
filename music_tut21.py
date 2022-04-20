import pygame
import random
import os
pygame.mixer.init()

pygame.init()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# Game Window
window_width = 900
window_height = 400
gameWindow = pygame.display.set_mode((window_width, window_height))

# Background Image lodaing
bgimg = pygame.image.load('bgimg.jpg')
bgimg = pygame.transform.scale(bgimg,(window_width,window_height)).convert_alpha()
wc = pygame.image.load('welcome.jpg')
wc = pygame.transform.scale(wc,(window_width,window_height)).convert_alpha()
# Game Title
pygame.display.set_caption(("The Snake Game"))
pygame.display.update()

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])


def plot_snake(gameWindow, color, snk_list, snake_size):
    for x, y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])
def welcome():
    exit_game = False
    while not exit_game:
        # gameWindow.fill((200,50,100))
        gameWindow.blit(wc, (0, 0))
        text_screen("Welcome to Snake Game",black,200,120)
        text_screen("  Press SpaceBar to play", (255,100,50), 200, 180)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('back.mp3')
                    pygame.mixer.music.play()
                    global snake_x

                    # if abs(snake_x - food_x) < 6 and abs(snake_y - food_y) < 6:
                    #     pygame.mixer.music.load('eat.wav')
                    #     pygame.mixer.music.play()
                    gameloop()

        pygame.display.update()
        clock.tick(60)
# Game Loop
def gameloop():
    # Game specific variables
    exit_game = False
    game_over = False
    snake_x = 50  # initial position  of snake along x axis
    snake_y = 70  # initial position  of snake along y axis
    velocity_x = 0
    velocity_y = 0
    snk_length = 1
    snk_list = []
    # Checking if highscore file exist or not
    if(not os.path.exists("highscore.txt")):
        with open("highscore.txt","w") as f:
            f.write("0")
    with open("highscore.txt", "r") as f:
        highscore = f.read()

    food_x = random.randint(0, window_width / 2)
    food_y = random.randint(0, window_height / 2)
    score = 0
    init_velocity = 3
    snake_size = 15  # size of head(square)
    fps = 60

    while not exit_game:
        if game_over:
            with open("highscore.txt", "w") as f:
                f.write(str(highscore))
            gameWindow.fill(white)
            text_screen("Game Over! Press enter to continue.", red, 100, 150)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
        else:
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
                    if event.key == pygame.K_q:
                        score += 10

            snake_x += velocity_x
            snake_y += velocity_y
            if abs(snake_x - food_x) < 6 and abs(snake_y - food_y) < 6:
                # pygame.mixer.music.load('eat.wav')
                # pygame.mixer.music.play()
                score += 10
                # print("Score :", score * 10)

                food_x = random.randint(0, window_width / 2)
                food_y = random.randint(0, window_height / 2)

                snk_length += 5
                if score > int(highscore):
                    highscore = score

            gameWindow.fill(white)
            gameWindow.blit(bgimg, (0,0))
            text_screen("Score :" + str(score) + "  HighScore: " + str(highscore), red, 5, 5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list) > snk_length:
                del snk_list[0]

            if snake_x < 0 or snake_x > window_width or snake_y < 0 or snake_y > window_height:
                game_over = True
                pygame.mixer.music.load('gameover.wav')
                pygame.mixer.music.play()
                # print("Game Over")

            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load('gameover.wav')
                pygame.mixer.music.play()
            # pygame.draw.rect(gameWindow, black, snake_x, snake_y, snake_size)
            plot_snake(gameWindow, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()


# gameloop()
welcome()