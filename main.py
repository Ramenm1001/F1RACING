import pygame
from game import Game
from race_car import RaceCar

START_POS = (150, 150)

win = pygame.display.set_mode((750, 500))

# загрузка ресурсов
car = pygame.image.load("sprites/yellow_car.png").convert_alpha()
car = pygame.transform.scale(car, (50, 25))
background = pygame.image.load("sprites/track_background.png").convert_alpha()

# Создание игрока
player = RaceCar(win, *START_POS, car)

# класс игры
game = Game(win, player, background)

# запуск приложения
while game.run:
    game.update_loop()
pygame.quit()
