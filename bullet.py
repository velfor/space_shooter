import pygame
from const import *

class Bullet(pygame.sprite.Sprite):
    def __init__(self, shipx, shipy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10,20))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.centerx = shipx
        self.rect.bottom = shipy
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        #удалить, если вышла за верхний край экрана
        if self.rect.bottom < 0:
            self.kill()
        
