from constants import *
import pygame
def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	while True:
                   screen.fill((0, 0, 0))
                   pygame.display.flip()
                   for event in pygame.event.get():
                       if event.type == pygame.QUIT:
                          return

print (f"Starting Asteroids! Screen width: {SCREEN_WIDTH} Screen height: {SCREEN_HEIGHT}")
if __name__ == "__main__":
    main()
