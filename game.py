import pygame
import math
pygame.init()

font = pygame.font.Font(None, 32)

debug = True
class Game:
    def __init__(self, win,  player, background: pygame.Surface):
        self.win = win
        self.player = player
        self.background = background
        self.run = True

    def update_loop(self):
        pygame.time.delay(50)
        for eve in pygame.event.get():
            if eve.type == pygame.QUIT:
                self.run = False
            if eve.type == pygame.KEYDOWN:
                if eve.key == pygame.K_a:
                    self.player.left()
                if eve.key == pygame.K_d:
                    self.player.right()
                if eve.key == pygame.K_w:
                    self.player.gas()
                if eve.key == pygame.K_s:
                    self.player.stop()


        self.win.blit(self.background, (0-self.player.x_camera, 0-self.player.y))
        self.player.update()

        if debug:
            txt = font.render(math.cos(self.player.napravlenie) * self.player.speed)
            self.win.blit(txt, (0, 0))
        pygame.display.update()
