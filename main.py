# Python Arcade Shooting Game
import pygame
import math

pygame.init()
fps = 60
timer = pygame.time.Clock()
font = pygame.font.Font('./assets/font/myFont.ttf', 32)
WIDTH = 900
HEIGHT = 800
screen = pygame.display.set_mode([WIDTH, HEIGHT])