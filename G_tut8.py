import pygame
pygame.init()

white = (255,255,255)
green = (255,0,0)
black = (0,0,0 )

pygame.display.set_caption(("The Snake Game"))
window_width = 500
window_height = 300
gameWindow = pygame.display.set_mode((window_width,window_height))

pygame.display.update()
######## Creating important Variables
exit_game = False
exit_over = False
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

    gameWindow.fill(white)
    pygame.display.update()