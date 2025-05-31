import pygame.transform

class RaceCar:
    def __init__(self, win, x, y, sprite, napravlenie=0):
        self.win = win
        self.x = x
        self.y = y



        self.sprite = sprite
        self.napravlenie = napravlenie
        self.speed = 0
        self.x_camera = 0

        self.spritelist = [self.sprite]
        for i in range(3):
            sprite = pygame.transform.rotate(sprite, -90)
            self.spritelist.append(sprite)

    def right(self):
        self.napravlenie += 1
        if self.napravlenie == 4:
            self.napravlenie = 0

    def left(self):
        self.napravlenie -= 1
        if self.napravlenie == -1:
            self.napravlenie = 3
    def gas(self):
        self.speed += 1

    def stop(self):
        self.speed -= 1

    def draw(self):
        xoffset, yoffset= self.spritelist[self.napravlenie].get_size()
        xoffset, yoffset = xoffset//2, yoffset//2
        self.win.blit(self.spritelist[self.napravlenie], (self.x-xoffset, self.y-yoffset))
        # self.win.blit(self.spritelist[self.napravlenie], (50-xoffset, 50-yoffset))

    def update(self):


        if self.x + self.speed > 750:
            self.x_camera += self.speed
        else:
            self.x += self.speed
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
