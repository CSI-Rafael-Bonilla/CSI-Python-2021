import pygame
import time
import random

#Initializes all of the imported Pygame modules.
pygame.init()

#Updates the display
#pygame.display.update()

#black, red, white, and are in the parameter "0, 0, 0", "255,0,0", "255, 255, 255", and "0,0,225" respectively
black=(0,0,0)
red=(255,0,0)
white = (255, 255, 255)
blue = (0,0,225)

#Sets the display paramaters
dis_width = 800
dis_height = 600
dis=pygame.display.set_mode((dis_width,dis_height))

#Names the display after the set caption
pygame.display.set_caption('Snake game by Edureka')

#Adds a clock
clock = pygame.time.Clock()

snake_block = 10
#It is the snake's speed
snake_speed = 30

#Establishes the font
font_style = pygame.font.SysFont(None, 30)

#It establishes the font of the message
def message(msg,color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/3, dis_height/3])

#It makes it when game_over is false it prints out all the actions that take place on the screen. 
def gameLoop():
    game_over=False
    game_close=False

#parameters of x and y
    x1 = dis_width/2
    y1 = dis_height/2

#The change made in x and y
    x1_change = 0       
    y1_change = 0

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0


    while not game_over:
        #When game close is true, then it prints You lost
        while game_close == True:
            dis.fill(white)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()
 
            for event in pygame.event.get():
                #When pressed q then game_over is true and it closes the tab
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    #When the key c is pressed, then the game starts over
                    if event.key == pygame.K_c:
                        gameLoop()
 
        for event in pygame.event.get():
            #When the X is pressed then game_over is true and the code ends
            if event.type == pygame.QUIT:
                game_over = True
            
            #When an arrow key is pressed then it moves according to the key pressed
            if event.type == pygame.KEYDOWN:

                #When the arrow key left is pressed then the snake goes to the left
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                
                #When the arrow key right is pressed then the snake goes to the right
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                #When the arrow key up is pressed then the snake goes up
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                #When the arrow key down is pressed then the snake goes down
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
 
        #When x is greater or equal than the width of the screen or less than zero or y is greater than the height of the screen or is less than zero, then it is game over
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        #When x1 is increased, x1_change is increased
        x1 += x1_change
        #When x1 is increased, x1_change is increased
        y1 += y1_change
        dis.fill(white)

        #It draws a blue rectangle with the parameters of foodx, food,y, snake_block and snake_block
        pygame.draw.rect(dis, blue, [foodx, foody, snake_block, snake_block])
        #It draws a black rectangle with the parameters of x1, y1, snake_block and snake_block
        pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block])
        pygame.display.update()
 
        #When the snake is in the same x and y axis of the food, then it prints "Yummy!!!"
        if x1 == foodx and y1 == foody:
            print("Yummy!!")
        clock.tick(snake_speed)
 
 #Used to unitialize everything
    pygame.quit()
    quit()
 
 
gameLoop()




