import pygame
import time
import random
#initializing pygame
pygame.init()

#white, black and red are in the parameter "255, 255, 255",  "0, 0, 0" and "255,0,0" respectively
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)


#sets up a display mode that is on the parameter of width, 800, and height, 600
dis_width = 800
dis_height  = 600
dis = pygame.display.set_mode((dis_width, dis_width))

#it prints the caption that says 'Snake game by Edureka'
pygame.display.set_caption('Snake game by Edureka')

#adds a clock to the snake game
clock = pygame.time.Clock()
 
snake_block = 10
#adds the speed of the snake
snake_speed = 30

#establishes a font style for the game
font_style = pygame.font.SysFont(None, 30)

def message(msg,color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/2, dis_height/2])

def gameloop():
    game_over = False
    game_close = False
    
    #parameters of x and y
    x1 = dis_width / 2
    y1 = dis_height / 2
 
    x1_change = 0
    y1_change = 0

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0

    while not game_over:
        while game_close == True:
            dis.fill(white)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()
    for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameloop()
    for event in pygame.event.get():
        #if pygame quits, then it is a game over
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

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_over = True
    #changes the parameters of x1 and y1 to those of x1_change and y1_change
    x1 += x1_change
    y1 += y1_change
    dis.fill(white)
    #draws a black square in the display
    pygame.draw.rect(dis,black,[x1,y1,10,10])
    #updates the screen display
    pygame.display.update()

    if x1 == foodx and y1 == foody:
            print("Yummy!!")
    clock.tick(snake_speed)

#tells the player it lost 
message("You lost", red)
pygame.display.update()
time.sleep(2)

#uninitializes everything
pygame.quit()
quit()
