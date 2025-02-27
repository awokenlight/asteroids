from constants import *
import sys
import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from asteroid import Shot
def main():
    print(f"Starting Asteroids! Screen width: {SCREEN_WIDTH} Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Create the shared groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullet = pygame.sprite.Group()

    Player.containers = [updatable, drawable]
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (bullet, updatable, drawable)
    # Now create the player instance!
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    
    # Create the asteroid field
    AsteroidField()
    while True:
        screen.fill((0, 0, 0))  
        # Game loop
        updatable.update(dt)
        for element in drawable:
            element.draw(screen)
        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game over!")  
                sys.exit()
        for shot in bullet:
            for asteroid in asteroids:
                if shot.collision(asteroid):
                    asteroid.split()
                    shot.kill()        

        pygame.display.flip()
        dt = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

main()
