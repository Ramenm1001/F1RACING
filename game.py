class Game:
    def __init__(self, win,  player=1, background=1):
        self.win = win
        self.player = player
        self.background = background

    def update_loop(self):
        self.win.blit(self.background, (0,0))
        self.player.update()
