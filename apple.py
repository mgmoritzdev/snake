import pygame
from pygame.locals import *
import random
import math

class Apple:
    apples = []
    spawn_count = 0
    spawn_period = 0
    def __init__(self, block_size, color):
        self.skin = pygame.Surface((block_size, block_size))
        self.color = color
        self.block_size = block_size
        self.skin.fill(color)
        self.position = (10 * math.floor(random.randint(0, 590) / 10), 10 * math.floor(random.randint(0, 590) / 10))

    def render(self, screen):
        screen.blit(self.skin, self.position)

    @staticmethod
    def spawn(block_size, color, spawn_period):
        Apple.spawn_count += 1
        if (Apple.spawn_count >= Apple.spawn_period):
            apple = Apple(block_size, color)
            Apple.apples.append(apple)
            Apple.spawn_count = 0
        Apple.spawn_period = spawn_period

    @staticmethod
    def render_all(screen):
        for apple in Apple.apples:
             apple.render(screen)
