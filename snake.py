import pygame
import time
import math
import random

pygame.init()

GREY = (150,150,150)
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)

screen_with = 600
screen_height = 1000
screen = pygame.display.set_mode((screen_height,screen_with))
pygame.display.set_caption("Snake")

snake_block = 20
snake_speed = 10

clock = pygame.time.Clock()

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, GREY)
    screen.blit(value, [0, 0])

def our_snake(snake_block, snake_list):
	for x in snake_list:
		pygame.draw.rect(screen, WHITE, (x[0], x[1], snake_block, snake_block))

def message(msg,color):
	mesg = font_style.render(msg, True, color)
	screen.blit(mesg, (screen_height/4,screen_height/5))

def gameLoop():
	game_over = True
	game_close = True

	x1 = screen_height/2
	y1 = screen_with/2

	x1_change = 0
	y1_change = 0

	# pygame.draw.rect(screen, WHITE, (200,200,50,50))
	# time.sleep(3)
	screen.fill(GREY)
	pygame.display.update()
	time.sleep(1)

	snake_List = []
	lenght_of_snake = 1

	foodx = round(random.randrange(0, screen_height - snake_block) / 20.0) * 20.0
	foody = round(random.randrange(0, screen_with - snake_block) / 20.0) * 20.0

	while game_over:

		while game_close == False:
			screen.fill(GREY)
			message("You lose! Press Q-Quit or C-Play Again", RED)
			Your_score(lenght_of_snake - 1)
			pygame.display.update()
			# time.sleep(3)

			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						game_over = False
						game_close = True
					if event.key == pygame.K_c:
						gameLoop()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game_over = False
			if event.type == pygame.KEYDOWN:
				
					if event.key == pygame.K_LEFT:
						x1_change = -snake_block
						y1_change = 0
					elif event.key == pygame.K_RIGHT:
						x1_change = snake_block
						y1_change = 0
					elif event.key == pygame.K_UP:
						x1_change = 0
						y1_change = -snake_block
					elif event.key == pygame.K_DOWN:
						x1_change = 0
						y1_change = snake_block
				
		if x1 >= screen_height or x1 < 0 or y1 >= screen_with or y1 < 0:
				game_close = False

		x1 += x1_change
		y1 += y1_change

		screen.fill(BLACK)
		pygame.draw.rect(screen, RED, (foodx,foody,snake_block,snake_block))
		pygame.draw.rect(screen, WHITE, (x1,y1,snake_block,snake_block))
		snake_Head = []
		snake_Head.append(x1)
		snake_Head.append(y1)
		snake_List.append(snake_Head)
		if len(snake_List) > lenght_of_snake:
			del snake_List[0]

		for x in snake_List[:-1]:
			if x == snake_Head:
				game_close = False

		our_snake(snake_block, snake_List)
		Your_score(lenght_of_snake - 1)

		pygame.display.update()

		if x1 == foodx and y1 == foody:
			foodx = round(random.randrange(0, screen_height - snake_block) / 20.0) * 20.0
			foody = round(random.randrange(0, screen_with - snake_block) / 20.0) * 20.0
			lenght_of_snake += 1

		clock.tick(snake_speed)

		pygame.display.update()

	pygame.quit()

gameLoop()
