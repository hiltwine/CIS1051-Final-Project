import pygame
import time
import random
 
pygame.init()
 
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 200, 0)
blue = (50, 153, 213)
gold = (204 , 204 , 0)
 
dis_width = 600
dis_height = 400
 
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('War Snake by Hiltwine & Hughes')
 
clock = pygame.time.Clock()
 
snake_block = 10
snake_speed = 15
 
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.Font("Margarine-Regular.ttf", 20)
 
 
def Your_score(score):
    value = score_font.render("Eat the Black Food, Avoid the Red Mines! Your Score: " + str(score), True, white)
    dis.blit(value, [0, 0])
 
 
 
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
 
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])
 
 
def gameLoop():
    game_over = False
    game_close = False
 
    x1 = dis_width / 2
    y1 = dis_height / 2
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    Length_of_snake = 1
 
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    minex = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    miney = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    
    minex2 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    miney2 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    minex3 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    miney3 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    minex4 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    miney4 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    minex5 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    miney5 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    minex6 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    miney6 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    
    minex7 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    miney7 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    minex8 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    miney8 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    minex9 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    miney9 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    minex10 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    miney10 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    minex11 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    miney11 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    
    minex12 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    miney12 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    minex13 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    miney13 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    minex14 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    miney14 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    minex15 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    miney15 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    minex16 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    miney16 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    
    minex17 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    miney17 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    minex18 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    miney18 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    minex19 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    miney19 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    minex20 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    miney20 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    
    while not game_over:
 
        while game_close == True:
            dis.fill(red)
            message("Get Better! Press C-Play Again or Q-Quit" , black)
            Your_score(Length_of_snake - 1)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
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
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(green)

        if Length_of_snake <= 5:
            pygame.draw.rect(dis, gold, [foodx, foody, snake_block, snake_block])
            pygame.draw.rect(dis, red, [minex, miney, snake_block, snake_block])
            
            snake_Head = []
            snake_Head.append(x1)
            snake_Head.append(y1)
            snake_List.append(snake_Head)

            if len(snake_List) > Length_of_snake:
                del snake_List[0]
     
            for x in snake_List[:-1]:
                if x == snake_Head:
                    game_close = True
     
            our_snake(snake_block, snake_List)
            Your_score(Length_of_snake - 1)
     
            pygame.display.update()
     
            if x1 == foodx and y1 == foody:
                foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                minex = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                miney = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                Length_of_snake += 1

            if (x1 == minex and y1 == miney):
                foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                minex = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                miney = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                
                snake_Head.remove(x1)
                snake_Head.remove(y1)
                snake_List.remove(snake_Head)
                Length_of_snake -= 1

                if Length_of_snake < 1:
                    game_close = True

        elif Length_of_snake <= 10:
            pygame.draw.rect(dis, gold, [foodx, foody, snake_block, snake_block])
            pygame.draw.rect(dis, red, [minex, miney, snake_block, snake_block])
            pygame.draw.rect(dis, red, [minex2, miney2, snake_block, snake_block])
            pygame.draw.rect(dis, red, [minex3, miney3, snake_block, snake_block])
            pygame.draw.rect(dis, red, [minex4, miney4, snake_block, snake_block])
            pygame.draw.rect(dis, red, [minex5, miney5, snake_block, snake_block])
            
            snake_Head = []
            snake_Head.append(x1)
            snake_Head.append(y1)
            snake_List.append(snake_Head)

            if len(snake_List) > Length_of_snake:
                del snake_List[0]
     
            for x in snake_List[:-1]:
                if x == snake_Head:
                    game_close = True
     
            our_snake(snake_block, snake_List)
            Your_score(Length_of_snake - 1)
     
            pygame.display.update()
     
            if x1 == foodx and y1 == foody:
                foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                minex = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                miney = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                minex = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                miney = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                minex2 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                miney2 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                minex3 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                miney3 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                minex4 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                miney4 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                minex5 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                miney5 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                snake_Head.append(x1)
                snake_Head.append(y1)
                snake_List.append(snake_Head)
                Length_of_snake += 1

            if (x1 == minex and y1 == miney) or (x1 == minex2 and y1 == miney2) or (x1 == minex3 and y1 == miney3) or (x1 == minex4 and y1 == miney4) or (x1 == minex5 and y1 == miney5):
                foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                minex = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                miney = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                minex = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                miney = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                minex2 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                miney2 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                minex3 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                miney3 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                minex4 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                miney4 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                minex5 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                miney5 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                snake_Head.remove(x1)
                snake_Head.remove(y1)
                snake_List.remove(snake_Head)
                Length_of_snake -= 1

                if Length_of_snake < 1:
                    game_close = True

        elif Length_of_snake <= 20:
            pygame.draw.rect(dis, gold, [foodx, foody, snake_block, snake_block])
            pygame.draw.rect(dis, red, [minex, miney, snake_block, snake_block])
            pygame.draw.rect(dis, red, [minex2, miney2, snake_block, snake_block])
            pygame.draw.rect(dis, red, [minex3, miney3, snake_block, snake_block])
            pygame.draw.rect(dis, red, [minex4, miney4, snake_block, snake_block])
            pygame.draw.rect(dis, red, [minex5, miney5, snake_block, snake_block])
            pygame.draw.rect(dis, red, [minex6, miney6, snake_block, snake_block])
            pygame.draw.rect(dis, red, [minex7, miney7, snake_block, snake_block])
            pygame.draw.rect(dis, red, [minex8, miney8, snake_block, snake_block])
            pygame.draw.rect(dis, red, [minex9, miney9, snake_block, snake_block])
            
            snake_Head = []
            snake_Head.append(x1)
            snake_Head.append(y1)
            snake_List.append(snake_Head)

            if len(snake_List) > Length_of_snake:
                del snake_List[0]
     
            for x in snake_List[:-1]:
                if x == snake_Head:
                    game_close = True
     
            our_snake(snake_block, snake_List)
            Your_score(Length_of_snake - 1)
     
            pygame.display.update()
     
            if x1 == foodx and y1 == foody:
                foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                minex = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                miney = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                minex = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                miney = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                minex2 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                miney2 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                minex3 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                miney3 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                minex4 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                miney4 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                minex5 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                miney5 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                minex6 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                miney6 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0         
                minex7 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                miney7 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                minex8 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                miney8 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                minex9 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                miney9 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                minex10 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                miney10 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                snake_Head.append(x1)
                snake_Head.append(y1)
                snake_List.append(snake_Head)
                Length_of_snake += 1

            if (x1 == minex and y1 == miney) or (x1 == minex2 and y1 == miney2) or (x1 == minex3 and y1 == miney3) or (x1 == minex4 and y1 == miney4) or (x1 == minex5 and y1 == miney5) or (x1 == minex6 and y1 == miney6) or (x1 == minex7 and y1 == miney7) or (x1 == minex8 and y1 == miney8) or (x1 == minex9 and y1 == miney9) or (x1 == minex10 and y1 == miney10):
                foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                minex = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                miney = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                minex = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                miney = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                minex2 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                miney2 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                minex3 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                miney3 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                minex4 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                miney4 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                minex5 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                miney5 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                minex6 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                miney6 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0         
                minex7 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                miney7 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                minex8 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                miney8 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                minex9 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                miney9 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                minex10 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                miney10 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                snake_Head.remove(x1)
                snake_Head.remove(y1)
                snake_List.remove(snake_Head)
                Length_of_snake -= 1

                if Length_of_snake < 1:
                    game_close = True

        else:
            pygame.draw.rect(dis, gold, [foodx, foody, snake_block, snake_block])
            pygame.draw.rect(dis, red, [minex, miney, snake_block, snake_block])
            pygame.draw.rect(dis, red, [minex2, miney2, snake_block, snake_block])
            pygame.draw.rect(dis, red, [minex3, miney3, snake_block, snake_block])
            pygame.draw.rect(dis, red, [minex4, miney4, snake_block, snake_block])
            pygame.draw.rect(dis, red, [minex5, miney5, snake_block, snake_block])
            pygame.draw.rect(dis, red, [minex6, miney6, snake_block, snake_block])
            pygame.draw.rect(dis, red, [minex7, miney7, snake_block, snake_block])
            pygame.draw.rect(dis, red, [minex8, miney8, snake_block, snake_block])
            pygame.draw.rect(dis, red, [minex9, miney9, snake_block, snake_block])
            pygame.draw.rect(dis, red, [minex10, miney10, snake_block, snake_block])
            pygame.draw.rect(dis, red, [minex11, miney11, snake_block, snake_block])
            pygame.draw.rect(dis, red, [minex12, miney12, snake_block, snake_block])
            pygame.draw.rect(dis, red, [minex13, miney13, snake_block, snake_block])
            pygame.draw.rect(dis, red, [minex14, miney14, snake_block, snake_block])
            pygame.draw.rect(dis, red, [minex15, miney15, snake_block, snake_block])
            pygame.draw.rect(dis, red, [minex16, miney6, snake_block, snake_block])
            pygame.draw.rect(dis, red, [minex17, miney7, snake_block, snake_block])
            pygame.draw.rect(dis, red, [minex18, miney8, snake_block, snake_block])
            pygame.draw.rect(dis, red, [minex19, miney9, snake_block, snake_block])
            pygame.draw.rect(dis, red, [minex20, miney10, snake_block, snake_block])
            
            snake_Head = []
            snake_Head.append(x1)
            snake_Head.append(y1)
            snake_List.append(snake_Head)

            if len(snake_List) > Length_of_snake:
                del snake_List[0]
     
            for x in snake_List[:-1]:
                if x == snake_Head:
                    game_close = True
     
            our_snake(snake_block, snake_List)
            Your_score(Length_of_snake - 1)
     
            pygame.display.update()
     
            if x1 == foodx and y1 == foody:
                foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                minex = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                miney = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                minex = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                miney = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                minex2 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                miney2 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                minex3 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                miney3 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                minex4 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                miney4 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                minex5 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                miney5 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                minex6 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                miney6 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0         
                minex7 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                miney7 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                minex8 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                miney8 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                minex9 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                miney9 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                minex10 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                miney10 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                minex11 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                miney11 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                minex12 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                miney12 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                minex13 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                miney13 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                minex14 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                miney14 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                minex15 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                miney15 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                minex16 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                miney16 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                minex17 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                miney17 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                minex18 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                miney18 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                minex19 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                miney19 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                minex20 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                miney20 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                
                snake_Head.append(x1)
                snake_Head.append(y1)
                snake_List.append(snake_Head)
                Length_of_snake += 1

            if (x1 == minex and y1 == miney) or (x1 == minex2 and y1 == miney2) or (x1 == minex3 and y1 == miney3) or (x1 == minex4 and y1 == miney4) or (x1 == minex5 and y1 == miney5) or (x1 == minex6 and y1 == miney6) or (x1 == minex7 and y1 == miney7) or (x1 == minex8 and y1 == miney8) or (x1 == minex9 and y1 == miney9) or (x1 == minex10 and y1 == miney10) or (x1 == minex11 and y1 == miney11) or (x1 == minex12 and y1 == miney12) or (x1 == minex13 and y1 == miney13) or (x1 == minex14 and y1 == miney14) or (x1 == minex15 and y1 == miney15) or (x1 == minex16 and y1 == miney16) or (x1 == minex17 and y1 == miney17) or (x1 == minex18 and y1 == miney18) or (x1 == minex19 and y1 == miney19) or (x1 == minex20 and y1 == miney20):
                foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                minex = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                miney = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                minex = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                miney = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                minex2 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                miney2 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                minex3 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                miney3 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                minex4 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                miney4 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                minex5 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                miney5 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                minex6 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                miney6 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0         
                minex7 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                miney7 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                minex8 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                miney8 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                minex9 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                miney9 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                minex10 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                miney10 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                minex11 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                miney11 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                minex12 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                miney12 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                minex13 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                miney13 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                minex14 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                miney14 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                minex15 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                miney15 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                minex16 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                miney16 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                minex17 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                miney17 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                minex18 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                miney18 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                minex19 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                miney19 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                minex20 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                miney20 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                
                snake_Head.remove(x1)
                snake_Head.remove(y1)
                snake_List.remove(snake_Head)
                Length_of_snake -= 1

                if Length_of_snake < 1:
                    game_close = True
            
              

            
                

            
 
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 
 
gameLoop()
