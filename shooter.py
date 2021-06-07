# подключаем модули
import pygame
import sys
# из модуля const берём всё
# ВНИМАНИЕ! НЕБЕЗОПАСНО! ТАК МОЖНО ИМПОРТИРОВАТЬ ТОЛЬКО СВОИ МОДУЛИ!

from const import *
from player import *
from meteor import *
from bullet import *

#НАСТРОЙКА ИГРЫ (ИНИЦИАЛИЗАЦИЯ)
#инициализация библиотеки
pygame.init()
#создание экрана, указываем ширину и высоту в кортеже
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
# создаем часы для отслеживания FPS
clock = pygame.time.Clock()
#=====СОЗДАНИЕ ГРУПП=====
# создаем группу для всех спрайтов
all_sprites = pygame.sprite.Group()
meteors = pygame.sprite.Group()
bullets = pygame.sprite.Group()
#=====CОЗДАНИЕ ОБЪЕКТОВ=====
# создаем объект для игрока
player = Player()
# добавляем player в группу all_sprites
all_sprites.add(player)

for i in range(10):
    meteor = Meteor()
    all_sprites.add(meteor)
    meteors.add(meteor)



# переменная для управления циклом
run = True
# основной игровой цикл
while run:
    #0 задержка для фиксированного FPS
    clock.tick(FPS)
    #1 ==========обработка событий==========
    for event in pygame.event.get():
        # если тип события - закрытие окна программы
        if event.type == pygame.QUIT:
            # выйти из программы
            run = False
        # если нажата клавиша и эта клваиша - пробел, то
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            #===ИГРОК СТРЕЛЯЕТ===
            #создаем пулю
            bullet = Bullet(player.rect.centerx, player.rect.top)
            #добавлям пулю в группу всех спрайтов
            all_sprites.add(bullet)
            #добавляем пулю в группу пуль
            bullets.add(bullet)
            
    #2 ===========действия и взаимодействия==========
    all_sprites.update()
    #=====ПРОВЕРКА СТОЛКНОВЕНИЙ=====
    #столкновение игрока с метеоритами
    player_hit = pygame.sprite.spritecollide(player, meteors, False)
    if player_hit:
        run = False
    #столкновения пуль с метеоритами
    meteor_hits = pygame.sprite.groupcollide(meteors, bullets, True, True)
    #на каждый сбитый метеор создаем новый метеор
    for hit in meteor_hits:
        meteor = Meteor()
        all_sprites.add(meteor)
        meteors.add(meteor)
    
    #3 ==========отрисовка==========
    #заливаем экран черным цветом
    screen.fill(BLACK)
    # рисуем все спрайты (в памяти)
    all_sprites.draw(screen)
    # обновляем экран (выводим фон и спрайты на экран)
    pygame.display.update()

#здесь основной цикл игры закончился
# завершить pygame
pygame.quit()
# выйти
sys.exit()
