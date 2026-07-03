import pygame
import random

Screen_width, Screen_height = 500, 400
Movement_speed = 5
Font_size = 72

pygame.init()

background_image = pygame.transform.scale("Background.avif"), ((Screen_width, Screen_height))

font = pygame.font.SysFont('Times New Roman', Font_size)

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.Surface((height, width))
        self.image.fill(pygame.color("dodgerblue"))