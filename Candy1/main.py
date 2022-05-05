from module.Element import GrilleCandy
from PyQt5 import QtWidgets, QtGui


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
        self.click = []

    def isBtnClicked(self):
        sender = self.sender()
        index = sender.value
        sender.setText("*")
        self.setClick(index)

    def setClick(self, index):
        if len(self.click) == 0:
            self.click.append(index)
        elif len(self.click) == 1:
            self.click.append(index)
            print(self.click)
            self.game.move(self.click[0][0],self.click[0][1],self.click[1][0], self.click[1][1])
            self.resetGrille()
        else:
            self.click = []
            self.click.append(index)

    def resetGrille(self):
        for y in range(len(self.game.grille)):
            for i in range(len(self.game.grille)):
                self.btn[i][y].setText("")
                self.btn[i][y].setIcon(QtGui.QIcon(self.icons_dict[self.game.getItem(i, y)]))


    def setupUI(self):
        for i in range(len(self.game.grille)):
            for y in range(len(self.game.grille)):
                self.btn[i][y].setFixedSize(50, 50)
                self.btn[i][y].move(50 * (y + 1), 50 * (i + 1))
                self.btn[i][y].setIcon(QtGui.QIcon(self.icons_dict[self.game.getItem(i, y)]))
                self.btn[i][y].clicked.connect(self.isBtnClicked)
                self.btn[i][y].value = [i, y]
        self.setGeometry(700, 300, 500, 500)
        self.show()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    candy = Candy()
    candy.setupUI()
    sys.exit(app.exec_())
