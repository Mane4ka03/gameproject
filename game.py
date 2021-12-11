import pygame
from pygame.locals import *

pygame.init()

screen_w = 595    #параметры окна
screen_h = 1000
                  # тут так же можно было вызвать специальную функцию, которая форматирует дисплей под фон, но я вписала сама.
screen = pygame.display.set_mode((screen_w,screen_h)) #работаем через библиотеку с окном
pygame.display.set_caption('игра ') #название игры(название в разработке, пока так)

#Загружу необходимые изображения для игры:

background = pygame.image.load('background.png')






#цикл работы игры (включение и выключение окна)
run = True
while run:

    screen.blit(background,(0,0)) #откуда нужно ставить фон

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()