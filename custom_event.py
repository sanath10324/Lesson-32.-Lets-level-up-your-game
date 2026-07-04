import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Two Sprites with Custom Event")

CHANGE_COLOR = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOR, 1000)  

class Sprite(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface((80, 80))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(x, y))

    def change_color(self):
        new_color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )
        self.image.fill(new_color)

sprite1 = Sprite(200, 200, (255, 0, 0))   
sprite2 = Sprite(400, 200, (0, 0, 255))   

all_sprites = pygame.sprite.Group()
all_sprites.add(sprite1, sprite2)

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == CHANGE_COLOR:
            sprite1.change_color()
            sprite2.change_color()

    screen.fill((200, 200, 200))  
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()