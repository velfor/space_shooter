import pygame
from const import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        # создаем спрайт
        pygame.sprite.Sprite.__init__(self)
        # рисуем квадрат
        self.image = pygame.Surface((50,50))
        # закрашиваем зеленым цветом
        self.image.fill(GREEN)
        # создаем прямоугольник - рамку для определения столкновений
        self.rect = self.image.get_rect()
        # задаём координаты игрока на экране
        self.rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT - 30)
        self.speedx = 0
        self.speedy = 0

    def update(self):
        self.speedx = 0
        key_state = pygame.key.get_pressed()
        if key_state[pygame.K_LEFT]:
            self.speedx = -5
        if key_state[pygame.K_RIGHT]:
            self.speedx = 5
        self.rect.x = self.rect.x + self.speedx
        #проверка выхода за границы
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
