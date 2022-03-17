import pygame

#Initializes all of the imported Pygame modules.
pygame.init()

#Updates the display
#pygame.display.update()

#red, blue, and white are in the parameter "0, 0, 255", "255,0,0", "255, 255, 255" respectively
blue=(0,0,255)
red=(255,0,0)
white = (255, 255, 255)

#Sets the display paramaters
dis=pygame.display.set_mode((800,600))

#Names the display after the set caption
pygame.display.set_caption('Snake game by Edureka')

#It makes a look in which it when game_over is false it prints out all the actions that take place on the screen. 
game_over=False

#parameters of x and y
x1 = 300
y1 = 300
x1_change = 0       
y1_change = 0

#Adds a clock
clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
#When the X is pressed on the tab of the game, the code is terminated.
        if event.type==pygame.QUIT:
            game_over=True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -10
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = 10
                x1_change = 0

#x1 adds to x1_change and y1 adds to y1_change    
    x1 += x1_change
    y1 += y1_change
    dis.fill(white) 
    #Updates the display and draws blue       
    pygame.draw.rect(dis,blue,[x1,y1,10,10])
    pygame.display.update()
    clock.tick(30)
#Used to uninitialize everything
pygame.quit()
quit()



