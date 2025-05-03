class RaceCar:
    def __init__(self, win, x, y, sprite):
        self.win = win
        self.x = x
        self.y = y
        self.sprite = sprite

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
