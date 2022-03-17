import pygame
import time

#Initializes all of the imported Pygame modules.
pygame.init()

#Updates the display
#pygame.display.update()

#red, blue, and white are in the parameter "0, 0, 0", "255,0,0", "255, 255, 255" respectively
black=(0,0,0)
red=(255,0,0)
white = (255, 255, 255)

#Sets the display paramaters
dis_width = 800
dis_height = 600
dis=pygame.display.set_mode((dis_width,dis_height))

#Names the display after the set caption
pygame.display.set_caption('Snake game by Edureka')

#It makes a look in which it when game_over is false it prints out all the actions that take place on the screen. 
game_over=False

#parameters of x and y
x1 = dis_width/2
y1 = dis_height/2

snake_block = 10

#The change made in x and y
x1_change = 0       
y1_change = 0

#Adds a clock
clock = pygame.time.Clock()

#It is the snake's speed
snake_speed = 30

#Establishes the font
font_style = pygame.font.SysFont(None, 50)

#It establishes the font of the message
def message(msg,color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/2, dis_height/2])

while not game_over:
    for event in pygame.event.get():
#When the X is pressed on the tab of the game, the code is terminated.
        if event.type==pygame.QUIT:
            game_over=True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -snake_block
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = snake_block
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -snake_block
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = snake_block
                x1_change = 0
    
#If the x1 or y1 is greater than dis_width or dis_height, then it is game over. 
    if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
        game_over = True
 

#x1 adds to x1_change and y1 adds to y1_change    
    x1 += x1_change
    y1 += y1_change
    dis.fill(white) 
    #Updates the display and draws blue       
    pygame.draw.rect(dis,black,[x1,y1,10,10])
    pygame.display.update()
    clock.tick(snake_speed)

#When one losses, the message "You lost" is displayed
message("You lost",red)
pygame.display.update()
time.sleep(2)

#Used to uninitialize everything
pygame.quit()
quit()



