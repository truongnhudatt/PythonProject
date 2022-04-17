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
        }
        self.grille = [[ElementGrille() for y in range(1, 7)] for i in range(1, 7)]
        # for i in range(len(self.grille)):
        #     for y in range(len(self.grille)):
        #         print(self.grille[i][y],sep=' ', end= ' ')
        #     print()
        self.button = [[QtWidgets.QPushButton('', self) for y in range(len(self.grille))] for i in
                       range(len(self.grille))]
        self.visited = [[0 for y in range(len(self.grille))] for i in range(len(self.grille))]
        print(self.visited)
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
            self.moveButton(self.click[0][0],self.click[0][1],self.click[1][0],self.click[1][1])
            self.refreshGrille()
        else:
            self.click = []
            self.click.append(index)
    def refreshGrille(self):
        for i in range(len(self.grille)):
            for y in range(len(self.grille)):
                self.button[i][y].setText("")
                self.setIcon(i,y)

    def refreshVisited(self):
        self.visited = [[0 for y in range(len(self.grille))] for i in range(len(self.grille))]
    def moveButton(self,i,j,k,l):
        self.invert(i,j,k,l)
        index = [i,j,k,l]
        self.action(index[0],index[1])
        print(self.visited)
    def invert(self,i,j,k,l):
        if abs(i-k) + abs(j - l) == 1:
            tmp = self.getItem(i,j)
            self.setItem(i,j, self.getItem(k,l))
            self.setItem(k,l,tmp)
    def setItem(self,i,j,value):
        self.grille[i][j].type = value
    def flood(self,i,j,value):
        if 0 <= i and i < 7 and 0 <= j and j < 7:
            if self.getItem(i,j) == value and self.visited[i][j] == 0:
                self.visited[i][j] = 1
                self.flood(i+1,j,value)
                self.flood(i-1,j,value)
                self.flood(i,j+1,value)
                self.flood(i,j-1,value)

    def action(self,i,j):
        self.refreshVisited()
        self.flood(i,j,self.getItem(i,j))
    def match3(self,i,j):
        sumI, sumY = 0,0
        for p in range(len(self.visited)):
            sumI += self.visited[i][p]
            sumY += self.visited[p][j]
        return sumI > 2 or sumY > 2
def main():
    app = QtWidgets.QApplication(sys.argv)
    ex = CandyCrush()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
