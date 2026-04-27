import pygame
import random

SIZE = 20
W, H = 600, 600


class SnakeGame:
    def __init__(self):
        self.snake = [(100, 100)]
        self.dx, self.dy = SIZE, 0

        self.food = self.spawn()
        self.poison = self.spawn()

        self.score = 0
        self.level = 1

        self.speed = 8

        # POWERUPS
        self.powerup = None
        self.power_timer = 0

        self.speed_boost = False
        self.slow = False
        self.shield = False

        # OBSTACLES
        self.obstacles = []

    def spawn(self):
        return (random.randrange(0, W, SIZE),
                random.randrange(0, H, SIZE))

    def move(self):
        x, y = self.snake[0]
        self.snake.insert(0, (x + self.dx, y + self.dy))

    def update(self):
        self.move()

        head = self.snake[0]

        # self collision
        if head in self.snake[1:]:
            if not self.shield:
                return False
            self.shield = False

        # walls
        x, y = head
        if x < 0 or x >= W or y < 0 or y >= H:
            if not self.shield:
                return False
            self.shield = False

        # food
        if head == self.food:
            self.score += 1
            self.food = self.spawn()
        else:
            self.snake.pop()

        # poison
        if head == self.poison:
            self.snake.pop()
            self.snake.pop()
            self.poison = self.spawn()
            if len(self.snake) <= 1:
                return False

        # LEVEL
        self.level = self.score // 5 + 1

        # LEVEL 3 obstacles
        if self.level >= 3 and len(self.obstacles) < 10:
            self.obstacles.append(self.spawn())

        if head in self.obstacles:
            return False

        # POWER TIMER
        if self.power_timer > 0:
            self.power_timer -= 1
        else:
            self.speed_boost = False
            self.slow = False

        return True

    def draw(self, screen):
        for s in self.snake:
            pygame.draw.rect(screen, (0,255,0), (*s, SIZE, SIZE))

        pygame.draw.rect(screen, (255,0,0), (*self.food, SIZE, SIZE))
        pygame.draw.rect(screen, (120,0,0), (*self.poison, SIZE, SIZE))

        for o in self.obstacles:
            pygame.draw.rect(screen, (80,80,80), (*o, SIZE, SIZE))