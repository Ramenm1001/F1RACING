import pygame.transform


class RaceCar:
    def __init__(self, win, x, y, sprite, napravlenie=0):
        self.win = win
        self.x = x
        self.y = y
        self.sprite = sprite
        self.napravlenie = napravlenie

        self.spritelist = [self.sprite]
        for i in range(3):
            sprite = pygame.transform.rotate(sprite, 90)
            self.spritelist.append(sprite)

    def right(self):
        self.napravlenie += 1
        if self.napravlenie == 4:
            self.napravlenie = 0

    def left(self):
        self.napravlenie -= 1
        if self.napravlenie == 0:
            self.napravlenie = 4
        

    def draw(self):
        self.win.blit(self.sprite, (self.x, self.y))

    def update(self):
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
