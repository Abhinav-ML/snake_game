import pygame

pygame.init()
# a = pygame.init()
# print(a)

# Creating Display/window
pygame.display.set_mode((500, 300))
# Creating Title/Name/Captions
pygame.display.set_caption("The Danger Cobra")

######   Creating some useful variable
exit_game = False  # by-default false (we are going to make it True when someone wants to close the pygame)
game_over = False

########   Creating Game Loop

while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:  
            if event.key == pygame.K_RIGHT:
                print("You have enter Right arrow  key")

pygame.quit()
quit()
