import pygame

#Initializes all of the imported Pygame modules.
pygame.init()

#Sets the display paramaters
dis=pygame.display.set_mode((400,300))

#Updates the display
pygame.display.update()

#Names the display after the set caption
pygame.display.set_caption('Snake game by Edureka')

#It makes a look in which it when game_over is false it prints out all the actions that take place on the screen. 
game_over=False
while not game_over:
    for event in pygame.event.get():
        print(event)   
 
#Used to uninitialize everything
pygame.quit()
quit()



