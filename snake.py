import pygame
from pygame.locals import *

SPEED_UP = (0, -1)
SPEED_DOWN = (0, 1)
SPEED_LEFT = (-1, 0)
SPEED_RIGHT = (1, 0)

class Snake:
    def __init__(self, block_size, color, length, increment_length):
        self.skin = pygame.Surface((block_size,block_size))
        self.skin.fill(color)
        self.apples = 0
        self.block_size = block_size
        self.increment_length = increment_length
        self.blocks = []
        start_pos = (200, 200)
        increment = 0
        for block in range(length):
            self.blocks += [(start_pos[0] + increment, start_pos[1])]
            increment += block_size
        self.growing = 0
        self.speed = SPEED_LEFT

    def head(self):
        return self.blocks[0]

    def update(self):
        next_pos = (self.blocks[0][0] + self.speed[0] * self.block_size,
                    self.blocks[0][1] + self.speed[1] * self.block_size)
        if (self.growing > 0):
            self.growing -= 1;
            self.blocks = [(next_pos)] + self.blocks
        else:
            self.blocks = [(next_pos)] + self.blocks[:-1]

    def render(self, screen):
        for pos in self.blocks:
            screen.blit(self.skin, pos)

    def handle_event(self, event):
        if event.type == KEYDOWN:
            if (event.key == K_UP and
                (self.speed == SPEED_LEFT or self.speed == SPEED_RIGHT)):
                self.speed = SPEED_UP
            if (event.key == K_DOWN and
                (self.speed == SPEED_LEFT or self.speed == SPEED_RIGHT)):
                self.speed = SPEED_DOWN
            if (event.key == K_LEFT
                and (self.speed == SPEED_UP or self.speed == SPEED_DOWN)):
                self.speed = SPEED_LEFT
            if (event.key == K_RIGHT
                and (self.speed == SPEED_UP or self.speed == SPEED_DOWN)):
                self.speed = SPEED_RIGHT

    def got_an_apple(self, apples):
        head = self.head()
        for apple in apples:
            if (apple.position[0] == head[0] and apple.position[1] == head[1]):
                apples.remove(apple)
                self.growing += self.increment_length
                self.apples += 1

    def self_collided(self):
        head = self.head()
        for tail in self.blocks[1:]:
            if (head[0] == tail[0] and head[1] == tail[1]):
                return True
        return False

    def wall_collided(self):
        head = self.head()
        if ((head[0] < 0 or head[0] > 590) or
            (head[1] < 0 or head[1] > 590)):
            return True
        return False
