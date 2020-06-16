import pygame
import random
from snake import Snake
from apple import Apple
from gui import Gui
from pygame.locals import *

SCREEN_SIZE = (600, 600)
COLOR_WHITE = (255, 255, 255)
COLOR_RED = (255, 0, 0)
INITIAL_LEGTH = 3
LEGTH_INCREMENT = 3
BLOCK_SIZE = 10
APPLE_SPAWN_PERIOD = 100
BASE_SPEED = 15
SPEED_INCREMENT = 0.15

pygame.init()
pygame.display.set_caption('Snake')

def handle_events(snake, gui):
    for event in pygame.event.get():
        gui.handle_event(event)
        if (gui.paused):
            return
        snake.handle_event(event)

def tick(clock, apples):
    factor = SPEED_INCREMENT * float(apples//2) + 1
    new_clock_tick = BASE_SPEED * factor
    clock.tick(new_clock_tick)

def play():
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    snake = Snake(BLOCK_SIZE, COLOR_WHITE, INITIAL_LEGTH, LEGTH_INCREMENT)
    gui = Gui(COLOR_WHITE)
    game_over = False

    while not game_over:
        tick(clock, snake.apples)
        handle_events(snake, gui)
        if (gui.paused):
            continue
        snake.update()
        screen.fill((0,0,0))
        snake.render(screen)
        Apple.spawn(BLOCK_SIZE, COLOR_RED, APPLE_SPAWN_PERIOD)
        snake.got_an_apple(Apple.apples)
        if (snake.self_collided() or snake.wall_collided()):
            game_over = True
        Apple.render_all(screen)
        gui.render_score(snake.apples, screen)
        pygame.display.update()
    print('Score:', gui.get_score(snake.apples))

play()
exit(0)
