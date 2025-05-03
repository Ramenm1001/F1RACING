import pygame

from negr import Negr
from palma import Palma
from housefornigga import HouseNigga
from background import draw_background
from sun import Sun
from campfire import Fire
from oblaka import draw_oblaka

win = pygame.display.set_mode((500, 500))
negr = Negr(win, 200, 400, 50)
palma = Palma(win, 250, 444, 55 )
house = HouseNigga(win, 290, 460, 90)
sun = Sun(win, 400, 50, 50)

fire = Fire(win, 200, 460)


island = [negr, palma, house]
island.append(sun)
island.append(fire)


run = True
while run:
    pygame.time.delay(50)
    for eve in pygame.event.get():
        if eve.type == pygame.QUIT:
            run = False

    win.fill((0, 0, 0))
    draw_background(win)
    draw_oblaka(win)
    for some in island:
        some.update()
    pygame.display.update()
pygame.quit()
