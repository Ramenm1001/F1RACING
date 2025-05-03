import pygame
from game import Game
from race_car import RaceCar

START_POS = (50, 50)

win = pygame.display.set_mode((750, 500))

# загрузка ресурсов
car = pygame.image.load("sprites/yellow_car.png").convert_alpha()
car = pygame.transform.scale(car, (50, 25))
background = pygame.image.load("sprites/track_background.png").convert_alpha()

player = RaceCar(win, *START_POS, car)

game = Game(win, player, background)
run = True
while run:
    pygame.time.delay(50)
    for eve in pygame.event.get():
        if eve.type == pygame.QUIT:
            run = False

    game.update_loop()
    pygame.display.update()
pygame.quit()
