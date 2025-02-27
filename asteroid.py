from circle_shape import CircleShape
import pygame
from constants import SHOT_RADIUS 
import random
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)
    def update(self, dt):
        self.position += self.velocity * dt
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
         # Generate random angle and create new velocities
        random_angle = random.uniform(20, 50)
        new_velocity1 = self.velocity.rotate(random_angle)
        new_velocity2 = self.velocity.rotate(-random_angle)
    
    # Calculate new radius
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        # Create two new asteroids
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = new_velocity1 * 1.2  # Scale up velocity by 1.2
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = new_velocity2 * 1.2  # Scale up velocity by 1.2
    
   
        



class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = pygame.math.Vector2(0, 0)  # Velocity must be set by the Player
        print(f"Shot created at position: ({x}, {y})")  # Debugging!
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, SHOT_RADIUS, 2)

    def update(self, dt):
        self.position += self.velocity * dt  # Move the shot based on velocity and time step
        # Add additional logic to handle when the shot goes out-of-bounds (optional)

