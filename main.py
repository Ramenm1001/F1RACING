import pygame


win = pygame.display.set_mode((500, 500))


run = True
while run:
    pygame.time.delay(50)
    for eve in pygame.event.get():
        if eve.type == pygame.QUIT:
            run = False

    win.fill((0, 0, 0))

    #for some in island:
    #    some.update()
    pygame.display.update()
pygame.quit()
