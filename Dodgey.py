import pygame
import random
import sys
import os
import time
from pygame.locals import *


        
pygame.init()
pygame.mixer.music.load("C:/Users/ayaan2/Music/Free Background Music For Gaming Videos - No Copyright.mp3")
WIDTH = 1920
HEIGHT = 1080

RED = (255,0,0)
BLUE = (34,255,255)
YELLOW = (255,255,0)
BACKGROUND_COLOR = (0,196,255)


player_size = 50
player_pos = [WIDTH/2, HEIGHT-2*player_size]

enemy_size = 50
enemy_pos = [random.randint(0,WIDTH-enemy_size), 0]
enemy_list = [enemy_pos]

speed = 10
score = 0
high_score = 0
white = (255, 255, 255) 
green = (0, 255, 0) 
blue = (0, 0, 128)
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

font = pygame.font.Font('freesansbold.ttf', 40)
font2 = pygame.font.Font('freesansbold.ttf', 30) 

for n in range(0, 4):  
    # create a text suface object, 
    # on which text is drawn on it. 
    text = font.render('Dodgey', True, green, blue)
    text2 = font2.render('Dodge The Blocks!!! ', True, green, blue)
    text3 = font.render(str(4-n), True, green, blue)
    
    X = 1920
    Y = 1080
    display_surface = pygame.display.set_mode((X, Y )) 

    # create a rectangular object for the 
    # text surface object 
    textRect = text.get_rect()
    textRect.center = (X // 2, Y // 2)
    display_surface.fill(white) 
    display_surface.blit(text, textRect)

    text2Rect = text2.get_rect()
    text2Rect.center = (X //2 + 10, Y // 2 + 50)
    display_surface.blit(text2, text2Rect)

    text3Rect = text3.get_rect()
    text3Rect.center = (X //2 + 10, Y // 2 + 90)
    display_surface.blit(text3, text3Rect)

    pygame.display.update() 
    time.sleep(1)



def write_score(score):
    f = open("score.txt","w")
    f.write(str(score))
    print ("file path"+os.path.abspath(os.getcwd()))
    f.close()

def read_score():
    try:
        f = open("score.txt","r")
        score = f.read()
        return int(score) 
    except FileNotFoundError:
        return 0
            
    

screen = pygame.display.set_mode((WIDTH, HEIGHT))
game_over = False

clock = pygame.time.Clock()
pygame.mixer.music.play(-1)

myFont = pygame.font.SysFont("monospace", 35)


def wait_for_key():
    print("WAITING")
    while True:
        print("waiting for key")
        time.sleep(1)
        for event in pygame.event.get():
            if event.type == QUIT:
                game_over = True
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                print("Key pressed")
                print(event.key)
                
                if (event.key == K_f):
                    game_over = False
                elif (event.key == K_q):
                    game_over = True
                    pygame.quit()
                    sys.exit()
                return
        

def set_level(score, speed):
    while score >= 0:
        speed = score * 0.5 + 10
        return speed
	# speed = score/5 + 1

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()



def drop_enemies(enemy_list):
	delay = random.random()
	if len(enemy_list) < 10 and delay < 0.1:
		x_pos = random.randint(0.0,WIDTH-enemy_size)
		y_pos = 0.0
		enemy_list.append([x_pos, y_pos])

def draw_enemies(enemy_list):
	for enemy_pos in enemy_list:
		pygame.draw.rect(screen, BLUE, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))

def update_enemy_positions(enemy_list, score, speed):
	for idx, enemy_pos in enumerate(enemy_list):
		if enemy_pos[1] >= 0 and enemy_pos[1] < HEIGHT:
			enemy_pos[1] += speed
		else:
			enemy_list.pop(idx)
			score += 1
	return score

def collision_check(enemy_list, player_pos):
	for enemy_pos in enemy_list:
		if detect_collision(enemy_pos, player_pos):
			return True
	return False

            
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((WIDTH/2),(HEIGHT/2))
    screen.blit(TextSurf, TextRect)
    pygame.display.update()
    
def small_text(message):
    text2 = font2.render(message, True, green, blue)
    text2Rect = text2.get_rect()
    text2Rect.center = (X //2 + 200, Y // 2 + 200)
    screen.blit(text2, text2Rect)
    pygame.display.update()
    
    
def detect_collision(player_pos, enemy_pos):
    p_x = player_pos[0]
    p_y = player_pos[1]

    e_x = enemy_pos[0]
    e_y = enemy_pos[1]

    if (e_x >= p_x and e_x < (p_x + player_size)) or (p_x >= e_x and p_x < (e_x+enemy_size)):
        if (e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= e_y and p_y < (e_y+enemy_size)):
            return True
    return False

def show_score(message, score):
    text = message + str(score)
    label = myFont.render(text, 1, YELLOW)
    screen.fill(BACKGROUND_COLOR)
    screen.blit(label, (WIDTH-300, HEIGHT-40))

def game_start():
    score = 0
    high_score = read_score()
    speed = 10
    player_size = 50
    player_pos = [WIDTH/2, HEIGHT-2*player_size]
    enemy_size = 50
    enemy_pos = [random.randint(0,WIDTH-enemy_size), 0]
    enemy_list = [enemy_pos]

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                x = player_pos[0]
                y = player_pos[1]
                print ("x="+ str(x) + " y="+str(y))
                print ("Speed=" + str(speed))
                
                if event.key == pygame.K_LEFT and x > 0:
                    x -= player_size
                elif event.key == pygame.K_RIGHT and x < (WIDTH -50) :
                    x += player_size
                player_pos = [x,y]
            
        screen.fill(BACKGROUND_COLOR)
        drop_enemies(enemy_list)
        score = update_enemy_positions(enemy_list, score, speed)
        speed = set_level(score, speed)
            
        
        show_score("Score ", score)
        if collision_check(enemy_list, player_pos):
            if (score > high_score):
                high_score = score
                write_score(score)
            show_score("High Score ", high_score)
            message_display("Game Over!!!")
            small_text("Press F to restart. Q to quit...")
            break;
        
        draw_enemies(enemy_list)
        pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], player_size, player_size))
        clock.tick(30)
        pygame.display.update()

while True:
    game_start()
    wait_for_key()




	
  






 
