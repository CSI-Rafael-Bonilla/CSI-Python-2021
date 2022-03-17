import pygame

#Initializes all of the imported Pygame modules.
pygame.init()

#Sets the display paramaters
dis=pygame.display.set_mode((400,300))

#Updates the display
#pygame.display.update()

#Names the display after the set caption
pygame.display.set_caption('Snake game by Edureka')

#red, and blue are in the parameter "0, 0, 255", and "255,0,0" respectively
blue=(0,0,255)
red=(255,0,0)

#It makes a look in which it when game_over is false it prints out all the actions that take place on the screen. 
game_over=False
while not game_over:
    for event in pygame.event.get():
#When the X is pressed on the tab of the game, the code is terminated.
        if event.type==pygame.QUIT:
            game_over=True

    #Updates the display and draws blue        
    pygame.draw.rect(dis,blue,[200,150,10,10])
    pygame.display.update()

#Used to uninitialize everything
pygame.quit()
quit()



