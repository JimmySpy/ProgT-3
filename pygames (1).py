import pygame
import sys
pygame.init()

# värvid
lGreen = [153, 255, 153]

# ekraani seaded
screen = pygame.display.set_mode([640, 480])
pygame.display.set_caption("Harjutamine")
screen.fill(lGreen)

gameover = False

while not gameover:
    # Lisame pildid
    youWin = pygame.image.load("img/youwin.png")
    youWin = pygame.transform.scale(youWin, [300, 120])
    screen.blit(youWin, [180, 100])

    pygame.display.flip()

    # mängu sulgemine ristist
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

pygame.quit()
