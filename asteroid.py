from circleshape import CircleShape
import pygame
import random
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(x, y, radius)
        else:
            super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 0)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), int(self.radius), 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        v1 = self.velocity.rotate(random_angle) * 1.2
        v2 = self.velocity.rotate(-random_angle) * 1.2
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        from asteroid import Asteroid  # avoid circular import issues
        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a1.velocity = v1
        a2 = Asteroid(self.position.x, self.position.y, new_radius)
        a2.velocity = v2
