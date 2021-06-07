import pygame
import random
from const import *

class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((60,60))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        
        self.rect.centerx = random.randint(0, SCREEN_WIDTH)
        self.rect.centery = random.randint(-120, -60)
        self.speedx = random.randint(-2,2)
        self.speedy = random.randint(1,5)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > SCREEN_HEIGHT or self.rect.right < 0 or self.rect.left > SCREEN_WIDTH:
            self.rect.centerx = random.randint(0, SCREEN_WIDTH)
            self.rect.centery = random.randint(-120, -60)
            self.speedx = random.randint(-2,2)
            self.speedy = random.randint(1,5)
        
