import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from setup import Grille, ElementGrille


class CandyCrush(QtWidgets.QMainWindow):
    def __init__(self):
        super(CandyCrush, self).__init__()
        self.iconDict = {
            1: 'CandyCrushImages/1.png',
            2: 'CandyCrushImages/2.png',
            3: 'CandyCrushImages/3.png',
            4: 'CandyCrushImages/4.png',
            5: 'CandyCrushImages/5.png',
            6: 'CandyCrushImages/6.png',
            7: 'CandyCrushImages/7.png',
            8: 'CandyCrushImages/8.png',
        }
        self.grille = [[ElementGrille() for y in range(1, 8)] for i in range(1, 8)]
        # for i in range(len(self.grille)):
        #     for y in range(len(self.grille)):
        #         print(self.grille[i][y],sep=' ', end= ' ')
        #     print()
        self.button = [[QtWidgets.QPushButton('', self) for y in range(len(self.grille))] for i in
                       range(len(self.grille))]
        self.setupUI()
        self.click = []
    def setupUI(self):
        self.buttonConnect()
        self.statusBar()
        self.afficheGrille()
        self.setGeometry(220, 200, 590, 500)
        self.setWindowTitle('Candy Crush Saga')
        self.show()
    def setIcon(self, i, y):
        self.button[i][y].setIcon(QtGui.QIcon(self.iconDict[self.getItem(i, y)]))

    def getItem(self, i, y):
        if (0 <= i and i < len(self.grille) and 0 <= y and y < len(self.grille)):
            return self.grille[i][y].type

    def afficheGrille(self):
        for i in range(len(self.grille)):
            for y in range(len(self.grille)):
                self.button[i][y].setFixedSize(50, 50)
                self.button[i][y].move(50 * (y + 1), 50 * (i + 1))
                self.setIcon(i, y)

    def buttonConnect(self):
        for i in range(len(self.grille)):
            for y in range(len(self.grille)):
                self.button[i][y].clicked.connect(self.buttonClicked)
                self.button[i][y].value = [i,y]

    def buttonClicked(self):
        sender = self.sender()
        index = sender.value
        # print(index)
        sender.setText("*")
        self.setClick(index)
    def setClick(self,index):
        if len(self.click) == 0:
            self.click.append(index)
        elif len(self.click) == 1:
            self.click.append(index)
            self.refreshGrille()
        else:
            self.click = []
            self.click.append(index)
    def refreshGrille(self):
        for i in range(len(self.grille)):
            for y in range(len(self.grille)):
                self.button[i][y].setText("")
                self.setIcon(i,y)
def main():
    app = QtWidgets.QApplication(sys.argv)
    ex = CandyCrush()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
