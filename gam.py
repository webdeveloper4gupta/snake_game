import pygame 
import random
pygame.init()

white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
snake_x=45
snake_y=55
init_velocity=5
snake_size=10
fps=30
screen_width=1200
screen_height=600
velocity_x=0
velocity_y=0
score=0
food_x=random.randint(20,screen_width/2)
food_y=random.randint(20,screen_height/2)
clock=pygame.time.Clock()
font=pygame.font.SysFont(None,55)





def text_screen(text,color,x,y):
          screen_text=font.render(text,True,color)
          gameWindow.blit(screen_text,[x,y])
# creating window 
gameWindow=pygame.display.set_mode((screen_width,screen_height))


pygame.display.set_caption("snake game develop by sukritan gupta")
# to see the change that happened
pygame.display.update()


exit_game=False 
game_over=False 

snk_list=[]
snk_length=1
def plot_snake(gameWindow,color,snk_list,snake_size):
          for x,y in snk_list:
                    
                    pygame.draw.rect(gameWindow,color,[x,y,snake_size,snake_size])
          
          pass
# game loop 

while not exit_game:
          if game_over:
                    gameWindow.fill(white)
                    text_screen("game over",red,screen_width/2,screen_height/2)
                    
          else:
                    
                    for event in pygame.event.get():
                              # print(event)
                              if event.type==pygame.QUIT:
                                        exit_game=True
                              if event.type==pygame.KEYDOWN:
                                        if event.key==pygame.K_RIGHT:
                                                  # snake_x=snake_x+10
                                                  velocity_x=init_velocity
                                                  velocity_y=0
                                        if event.key==pygame.K_LEFT:
                                                  # snake_x=snake_x-10
                                                  velocity_x=-init_velocity
                                                  velocity_y=0
                                        if event.key==pygame.K_UP:
                                                  # snake_y=snake_y-10
                                                  velocity_y=-init_velocity
                                                  velocity_x=0
                                        if event.key==pygame.K_DOWN:
                                                  # snake_y=snake_y+10
                                                  velocity_y=init_velocity
                                                  velocity_x=0
          
          
                              snake_x=snake_x+velocity_x
                              snake_y=snake_y+velocity_y
                              if abs(snake_x-food_x)<6 and abs(snake_y-food_y)<6:
                                        score+=1
                   
                    
                                        food_x=random.randint(20,screen_width/2)
                                        food_y=random.randint(20,screen_height/2)
                                        snk_length=snk_length+5
                                        if score>int(hiscore):
                                                  hiscore=score
                              gameWindow.fill(white)
                              text_screen("score"+str(score*10)+"Hiscore"+str(hiscore),red,5,5)
          
                              head=[]
                              head.append(snake_x)
                              head.append(snake_y)
                              snk_list.append(head)
                              if len(snk_list)>snk_length:
                                        del snk_list[0]
          
          
                              if snake_x<0 or snake_x>screen_width or  snake_y<0 or snake_y>screen_height:
                                        game_over=True
                    
                              pygame.draw.rect(gameWindow,red,[food_x,food_y,snake_size,snake_size])
          
                              plot_snake(gameWindow,black,snk_list,snake_size)
          # pygame.draw.rect(gameWindow,black,[snake_x,snake_y,snake_size,snake_size])
          pygame.display.update()
          clock.tick(fps)


pygame.quit()
quit()