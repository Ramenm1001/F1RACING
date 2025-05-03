class Game:
    def __init__(self, win,  player=1, background=1):
        self.win = win
        self.player = player
        self.background = background

    def update_loop(self):

        self.background.draw()
        self.player.update()