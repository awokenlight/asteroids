from circle_shape import CircleShape
from constants import PLAYER_RADIUS
from constants import PLAYER_TURN_SPEED
from constants import PLAYER_SPEED
from constants import PLAYER_SHOT_SPEED  
from asteroid import Shot
from constants import PLAYER_SHOOT_COOLDOWN
import pygame
class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
        # Automatically add self to predefined groups
        if hasattr(self.__class__, "containers"):
            for group in self.__class__.containers:  # Loop through the groups
                group.add(self)  # Add this instance to each group
# in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(),2)
    def rotate(self,dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    def update(self, dt):
         # Decrease the timer by dt
        self.timer -= dt
    
    # Optional: prevent timer from going below 0
        if self.timer < 0:
            self.timer = 0

        
        
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)   
        if keys[pygame.K_s]:
            self.move(-dt)  
        if keys[pygame.K_SPACE]:
            if self.timer <= 0:
                self.shoot()
                self.timer = PLAYER_SHOOT_COOLDOWN
    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt        
    def shoot(self):
    # Create the shot at the player's current position
        shot = Shot(self.position.x, self.position.y)
    
    # Set its velocity to move in the direction the player is facing
        direction = pygame.math.Vector2(0, 1)  # Default direction for "up"
        shot.velocity = direction.rotate(self.rotation) * PLAYER_SHOT_SPEED

        