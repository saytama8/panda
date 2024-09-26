from direct.showbase.ShowBase import ShowBase
from mapoanda3d import Mapnamager
class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.model = self.loader.loadModel('toris.egg')
        self.model.reparentTo(self.render)
        self.model.setScale(0.1)#розмір
        self.model.setPos(-2, 40,-3)#спавн
        base.camLens.setFov(90)


game = Game()
game.run()