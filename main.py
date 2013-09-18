import pygame
pygame.init()

size = width, height = 640, 480
speed = [5, 5]
color = 0, 0, 1
screen = pygame.display.set_mode(size)

ball = pygame.image.load("ball.png")
ballAction = ball.get_rect()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

	ballAction = ballAction.move(speed)
	if ballAction.left < 0 or ballAction.right > width:
		speed[0] = -speed[0]
	if ballAction.top < 0 or ballAction.bottom > height:
		speed[1] = -speed[1]

	screen.fill(color)
	screen.blit(ball, ballAction)
	pygame.display.flip()