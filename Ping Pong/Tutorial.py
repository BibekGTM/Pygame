import pygame, sys, random

pygame.init()
clock = pygame.time.Clock()

# Display
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("pong")

# Rectangles
#variable = pygame.Rect(x, y, width, height)

ball  = pygame.Rect(640/2 - 7.5, 460/2 - 7.5, 15, 15) 
player = pygame.Rect(640 - 10, 480/2 - 35, 5, 75)
opponent = pygame.Rect(5, 480/2 - 35, 5, 75)

# Color
bg_color = pygame.Color("grey12")
light_grey = (200, 200, 200)

# Game variables
ball_speed_x = 3.5 * random.choice((1, -1))
ball_speed_y = 3.5 * random.choice((1, -1))
player_speed = 0
opponent_speed = 7

# Score
player_score = 0 
opponent_score = 0


def ball_animation():
	global ball_speed_x, ball_speed_y
	ball.x += ball_speed_x
	ball.y += ball_speed_y

	if ball.top <= 0 or ball.bottom >= 480:
		ball_speed_y *= -1
	if ball.left <= 0 or ball.right >= 640:
		ball_restart()
	if ball.colliderect(player) or ball.colliderect(opponent):
		ball_speed_x *= -1

def player_border():
	if player.top <= 0:
		player.top = 0
	if player.bottom >= 480:
		player.bottom = 480

	

def opponent_ai():
	if opponent.top < ball.y:
		opponent.top += opponent_speed
	if opponent.bottom > ball.y:
		opponent.bottom -= opponent_speed
	if opponent.top <= 0:
		opponent.top = 0
	if opponent.bottom >= 480:
		opponent.bottom = 480

def ball_restart():
	global ball_speed_x, ball_speed_y
	ball.center = (640/2, 480/2)
	ball_speed_x *= random.choice((1, -1))
	ball_speed_y *= random.choice((1, -1))
	
# Main loop
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:	
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_s:
				player_speed += 3.5
			if event.key == pygame.K_w:
				player_speed -= 3.5
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_s:
				player_speed -= 3.5
			if event.key == pygame.K_w:
				player_speed += 3.5
	player.y += player_speed
	ball_animation()
	player_border()
	opponent_ai()

	# Visual
	screen.fill(bg_color)

	pygame.draw.rect(screen, light_grey, player)
	pygame.draw.rect(screen, light_grey, opponent)
	pygame.draw.ellipse(screen, light_grey, ball)
	pygame.draw.aaline(screen, light_grey, (640/2, 0), (640/2, 480))

	pygame.display.update()
	clock.tick(60)
	



	