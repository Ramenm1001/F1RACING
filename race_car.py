import math

import pygame.transform

class RaceCar:
    def __init__(self, win, x, y, sprite, napravlenie=0):
        self.win = win
        self.x = x
        self.y = y
        self.napravlenie = 0

        self.sprite = sprite
        self.napravlenie = napravlenie
        self.speed = 0
        self.x_camera = 0
        self.X_RAMKA = 150
        self.Y_RAMKA = 150

        self.spritelist = []
        for i in range(36):
            sprite_add = pygame.transform.rotate(sprite, -10 * i)
            self.spritelist.append(sprite_add)

    def right(self):
        self.napravlenie += 10
        if self.napravlenie == 360:
            self.napravlenie = 0

    def left(self):
        self.napravlenie -= 10
        if self.napravlenie == -10:
            self.napravlenie = 350

    def gas(self):
        self.speed += 1

    def stop(self):
        self.speed -= 1

    def draw(self):
        xoffset, yoffset= self.spritelist[self.napravlenie//10].get_size()
        xoffset, yoffset = xoffset//2, yoffset//2
        self.win.blit(self.spritelist[self.napravlenie//10], (self.x-xoffset, self.y-yoffset))
        # self.win.blit(self.spritelist[self.napravlenie], (50-xoffset, 50-yoffset))

    def update(self):
        x_speed = math.cos(self.napravlenie/57.2958) * self.speed
        y_speed = math.sin(self.napravlenie/57.2958) * self.speed
        self.y += y_speed
        if self.x + x_speed > 750 - self.X_RAMKA:
            self.x_camera += x_speed
        elif self.x + x_speed < 0 + self.X_RAMKA:
            self.x_camera += x_speed
        else:
            self.x += x_speed
        self.draw()


if __name__ == "__main__":
    import pygame
    win = pygame.display.set_mode((500, 500))
    car_sprite = pygame.image.load("sprites/yellow_car.png").convert_alpha()
    car_sprite = pygame.transform.scale(car_sprite, (50, 25))
    car = RaceCar(win, 50, 50, car_sprite)  # машина
    run = True
    while run:
        pygame.time.delay(50)
        for eve in pygame.event.get():
            if eve.type == pygame.QUIT:
                run = False

        win.fill((0, 0, 0))
        car.update()
        # for some in island:
        #    some.update()
        pygame.display.update()
    pygame.quit()
