from Element import *
from PyQt5 import QtWidgets, QtGui

ICONS_DICT = {
    1: 'icones/1.png',
    2: 'icones/2.png',
    3: 'icones/3.png',
    4: 'icones/4.png',
    5: 'icones/5.png',
    6: 'icones/6.png',
}


class Candy(QtWidgets.QMainWindow):
    def __init__(self):
        super(Candy, self).__init__()
        # QtWidgets.QMainWindow.__init__(self)
        self.icons_dict = {
            1: 'icones/1.png',
            2: 'icones/2.png',
            3: 'icones/3.png',
            4: 'icones/4.png',
            5: 'icones/5.png',
            6: 'icones/6.png',
        }
        self.game = GrilleCandy()
        self.btn = [[QtWidgets.QPushButton("", self)
                     for _ in range(len(self.game.grille))] for _ in range(len(self.game.grille))]

    def setIconButton(self, i, y):
        print(self.icons_dict[self.game.getItem(i, y)])
        self.btn[i][y].setIcon(QtGui.QIcon(self.icons_dict[self.game.getItem(i, y)]))

    def setupUI(self):
        for i in range(len(self.game.grille)):
            for y in range(len(self.game.grille)):
                self.btn[i][y].setFixedSize(50, 50)
                self.btn[i][y].move(50 * (y + 1), 50 * (i + 1))
                self.btn[i][y].setIcon(QtGui.QIcon(self.icons_dict[self.game.getItem(i, y)]))
                # self.setIconButton(i, y)
        self.setGeometry(700, 300, 500, 500)
        self.show()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    candy = Candy()
    candy.setupUI()
    sys.exit(app.exec_())
