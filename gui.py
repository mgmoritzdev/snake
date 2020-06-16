import pygame
from pygame.locals import *
import random
import math

class Gui:
    def __init__(self, color):
        self.paused = False
        self.font_color = color
        self.font_name = pygame.font.get_default_font()
        self.font_size = 28
        self.font = pygame.font.Font(self.font_name, 28)

    def get_score(self, apples):
        return apples * 100

    def render_score(self, apples, screen):
        score = self.font.render('Score: ' + str(self.get_score(apples)), True, self.font_color)
        score_rect = score.get_rect()
        score_rect.midtop = (300, 10)
        screen.blit(score, score_rect)

    def handle_event(self, event):
        if event.type == QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if (event.key == K_p):
                self.paused = not self.paused
