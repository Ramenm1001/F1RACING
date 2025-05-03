class RaceCar:
    def __init__(self):
        pass

    def draw(self):
        pass

    def update(self):
        pass


if __name__ == "__main__":
    import pygame

    win = pygame.display.set_mode((500, 500))
    car = RaceCar()  # машина
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
