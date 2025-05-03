import pygame


win = pygame.display.set_mode((750, 500))

car = pygame.image.load("sprites/yellow_car.png").convert_alpha()
car = pygame.transform.scale(car, (50, 25))

run = True
while run:
    pygame.time.delay(50)
    for eve in pygame.event.get():
        if eve.type == pygame.QUIT:
            run = False

    win.fill((0, 0, 77))
    win.blit(car, (50, 50))
    # for some in island:
    #    some.update()
    pygame.display.update()
pygame.quit()
