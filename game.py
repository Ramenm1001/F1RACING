import pygame

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

        self.win.blit(self.background, (0-self.player.x, 0-self.player.y))
        self.player.update()
        pygame.display.update()
