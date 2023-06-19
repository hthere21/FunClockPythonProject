import pygame
import time
import math
from pygame import mixer

pygame.init()

mixer.init()

mixer.music.load("mixkit-alarm-tone-996.wav")
mixer.music.set_volume(0.2)

screen = pygame.display.set_mode((500,600))

GREY = (150,150,150)
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (250,0,0)

running = True
total_secs = 0
display_min=0
display_sec=0
start = False
total =0

font = pygame.font.SysFont('sans',50) 
text_1 = font.render('+',True, BLACK)
text_2 = font.render('+',True, BLACK)
text_3 = font.render('-',True, BLACK)
text_4 = font.render('-',True, BLACK)
text_5 = font.render('START',True, BLACK)
text_6 = font.render('RESET',True, BLACK)
while running:
	screen.fill(GREY)

	mouse_x, mouse_y = pygame.mouse.get_pos()
	
	pygame.draw.rect(screen, WHITE, (100,50,50,50))
	pygame.draw.rect(screen, WHITE, (100,200,50,50))
	pygame.draw.rect(screen, WHITE, (200,200,50,50))
	pygame.draw.rect(screen, WHITE, (200,50,50,50))
	pygame.draw.rect(screen, WHITE, (300,50,150,50))
	pygame.draw.rect(screen, WHITE, (300,150,150,50))

	screen.blit(text_1, (100,50))
	screen.blit(text_2, (100,200))
	screen.blit(text_3, (200,50))
	screen.blit(text_4, (200,200))
	screen.blit(text_5, (300,50))
	screen.blit(text_6, (300,150))

	pygame.draw.rect(screen, BLACK, (50,520,400,50))
	pygame.draw.rect(screen, WHITE, (60,530,380,30))

	pygame.draw.circle(screen, BLACK, (250,400), 100)
	pygame.draw.circle(screen, WHITE, (250,400), 95)
	pygame.draw.circle(screen, BLACK, (250,400), 5)

	

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False 
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				if(100 < mouse_x < 150) and (50 < mouse_y < 100):
					total_secs +=60
					total = total_secs;
					print("press + min")
				if(100 < mouse_x < 150) and (200 < mouse_y < 250):
					total_secs +=1
					total = total_secs;
					print("press +sec")
				if(200 < mouse_x < 250) and (50 < mouse_y < 100):
					total_secs -=60
					total = total_secs;
					print("press  - min")
				if(200 < mouse_x < 250) and (200 < mouse_y < 250):
					total_secs -=1
					total = total_secs;
					print("press - sec")
				if(300 < mouse_x < 450) and (50 < mouse_y < 100):
					start = True
					total = total_secs;
					print("press Start")
				if(300 < mouse_x < 400) and (150 < mouse_y < 200):
					total_secs = 0
					print("press Reset")
				mixer.music.stop()
				break

	if start:
		total_secs -=1
		if total_secs == -1:
			start = False
			pygame.mixer.music.play(-1)
		time.sleep(1)


	display_min = int(total_secs/60)
	display_sec = total_secs - display_min*60

	if(display_min < 0 or display_sec < 0):
		total_secs = 0

	time_now = str(display_min) + ":" + str(display_sec)
	text_time = font.render(time_now, True, BLACK)
	screen.blit(text_time, (120,120))

	x_sec = 250 + 90* math.sin(6*display_sec*math.pi/180)
	y_sec = 400 - 90* math.cos(6*display_sec*math.pi/180)
	pygame.draw.line(screen, BLACK, (250,400), (x_sec, y_sec))

	x_min = 250 + 40*math.sin(6*display_min*math.pi/180)
	y_min = 400 - 40*math.cos(6*display_min*math.pi/180)
	pygame.draw.line(screen, RED, (250,400), (x_min, y_min))


	if total != 0:
		pygame.draw.rect(screen, RED, (60,530, int(380 * (total_secs/ total)),30))
	

	pygame.display.flip()

pygame.quit()