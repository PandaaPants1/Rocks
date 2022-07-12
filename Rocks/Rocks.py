#imports
import pygame
from sys import exit
pygame.init()

#display settings
h = 800
w = 800
screen = pygame.display.set_mode((h,w), pygame.NOFRAME)
clock = pygame.time.Clock()
fps = 60

#crosshair
crosshair = pygame.image.load("crosshair.png").convert_alpha()

#exit button
exitbutton = pygame.image.load("exit.png").convert_alpha()
exitbutton_pos = (400 - (exitbutton.get_width()/2), 550 - (exitbutton.get_height()/2))
mask = pygame.mask.from_surface(exitbutton)

#back button
backbutton = pygame.image.load("back.png").convert_alpha()
backbutton_pos = (400 - (backbutton.get_width()/2), 250 - (backbutton.get_height()/2))
mask = pygame.mask.from_surface(backbutton)

#menu
menu = False

#main loop
while True:

    #sets mouse invisible when in game
    pygame.mouse.set_visible(False)

    #events
    for e in pygame.event.get():
        if e.type == pygame.KEYDOWN:

            #detects escape key for menu
            if e.key == pygame.K_ESCAPE:

                #begins seperate game loop for menu
                menu = True
                while menu:
                    for e in pygame.event.get():

                        #detects click
                        if e.type == pygame.MOUSEBUTTONDOWN:

                            #exit button
                            try:
                                if mask.get_at((e.pos[0] - int(exitbutton_pos[0]), e.pos[1] - int(exitbutton_pos[1]))):
                                    pygame.quit()
                                    exit()
                            except IndexError:
                                pass

                            #back button
                            try:
                                if mask.get_at((e.pos[0] - int(backbutton_pos[0]), e.pos[1] - int(backbutton_pos[1]))):
                                    menu = False
                                    break
                            except IndexError:
                                pass

                    #set mouse visiblie when in menu
                    pygame.mouse.set_visible(True)

                    #bg and border
                    screen.fill((100, 100,100))
                    pygame.draw.rect(screen, ("Black"), (0, 0, h, w), 10)

                    #buttons
                    screen.blit(exitbutton, exitbutton_pos)
                    screen.blit(backbutton, backbutton_pos)

                    #clock
                    pygame.display.update()
                    clock.tick(fps)

    #bg and border
    screen.fill((100, 100,100))
    pygame.draw.rect(screen, ("Black"), (0, 0, h, w), 10)

    #sets crosshair to mouse location
    mx, my = pygame.mouse.get_pos()
    screen.blit(crosshair, (mx - (crosshair.get_width() / 2), my - (crosshair.get_height() / 2)))

    #clock
    pygame.display.update()
    clock.tick(fps)
