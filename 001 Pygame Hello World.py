import pygame, sys, os
from pygame.locals import*
red=[250,0,0]

pygame.init() #intialize

#set up window
window=pygame.display.set_mode((1000,600))
pygame.display.set_caption('Slither.eat- The Snake Game')

#set up drawing surface
screen = pygame.display.get_surface()
screen.fill(red)
pygame.display.set_caption("Snake")
pygame.display.flip()

while True:
	for event in pygame.event.get():
		print(event)
		if event.type==QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()