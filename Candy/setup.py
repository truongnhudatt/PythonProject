from random import randint

class ElementGrille:
    def __init__(self):
        self.type = randint(1,7)
    def __str__(self):
        return  str(self.type)
    def __repr__(self):
        return '{}'.format(self.type)
    def __eq__(self, other):
        return (self.type == other)

class Grille:
    def __init__(self):
        grid_bool = True
        while grid_bool:
            self.grille = [[ElementGrille() for y in range(1,9)] for i in range(1,9)]
            self.visited = [[0 for j in range(len(self.grille))] for i in range(len(self.grille))]
    def initGrille(self):
        for i in range(len(self.grille)):
            for y in range(len(self.grille)):
                self.resetVisited()
    def resetVisited(self):
        self.visited = [[0 for j in range(len(self.visited))] for i in range(len(self.visited))]
    def isSame(self,i,y):
        sumI, sumY = 0,0
        for index in range(len(self.visited)):
            sumI = sumI + self.visited[i][index]
            sumY = sumY + self.visited[index][y]
        return (sumI > 2 or sumY > 2)
    def setItemForGrid(self,i,y,x):
        self.grille[i][y].type = x
    def getItem(self,i,y):
        if (0 <= i and i < len(self.grille) and 0 <= y and y < len(self.grille)):
            return self.grille[i][y].type