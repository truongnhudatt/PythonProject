import random
from random import randint


class Element(object):
    def __init__(self):
        self.type = randint(1, 6)

    def __str__(self):
        return self.type

    def __repr__(self):
        return f"{self.type}"


class GrilleCandy(object):
    def __init__(self):
        self.scores = 0
        flag = True
        while flag:
            self.grille = [[Element() for _ in range(8)] for _x in range(8)]
            self.visited = [[0 for _ in range(len(self.grille))]
                            for _x in range(len(self.grille))]
            flag = self.setupGrille()

    def setupGrille(self):
        for i in range(len(self.grille)):
            for y in range(len(self.grille)):
                self.resetVisited()
                self.getPosRemove(i, y, self.getItem(i, y))
                if self.crush(i, y):
                    return True

    def getItem(self, i, y):
        if 0 <= i < len(self.grille) and 0 <= y < len(self.grille):
            return self.grille[i][y].type

    def move(self, i, y, k, l):
        self.swap(i, y, k, l)
        self.scores += self.action(i,y)
        self.scores += self.action(k,l)
        if not self.crush(i,y) and not self.crush(k,l):
            self.swap(i,y,k,l)
        self.scores += self.comboCrush()
        print(self.scores)
    def swap(self, i, y, k, l):
        if abs(i - k) + abs(y - l) == 1:
            tmp = self.getItem(i, y)
            self.setItem(i, y, self.getItem(k, l))
            self.setItem(k, l, tmp)

    def resetVisited(self):
        self.visited = [[0 for _ in range(len(self.grille))] for _x in range(len(self.grille))]

    def getPosRemove(self, x, y, value):
        if 0 <= x < 9 and 0 <= y < 9:
            if self.getItem(x, y) == value and self.visited[x][y] == 0:
                self.visited[x][y] = 1
                self.getPosRemove(x + 1, y, value)
                self.getPosRemove(x - 1, y, value)
                self.getPosRemove(x, y + 1, value)
                self.getPosRemove(x, y - 1, value)

    def action(self, i, y):
        self.resetVisited()
        score = 0
        self.getPosRemove(i, y, self.getItem(i, y))
        if self.crush(i, y):
            for _ in range(len(self.visited)):
                if self.detectItem(_):
                    print("_ la: ", _, self.visited[_])
                    count = self.getAllItemRemove(_)
                    if count[1] > 0:
                        for it in reversed(range(count[1])):
                            self.setItem(it + count[0], _, randint(1, 6))
                            self.setItem(it, _, randint(1, 6))
                            score += 1
                    else:
                        for it in range(count[0]):
                            self.setItem(it, _, randint(1, 6))
                            score += 1
        return score

    def crush(self, x, y):
        sumX, sumY = 0, 0
        for _ in range(len(self.visited)):
            sumX += self.visited[x][_]
            sumY += self.visited[_][y]
        return sumX > 2 or sumY > 2

    def detectItem(self, x):
        for _ in range(len(self.visited)):
            if self.visited[_][x] == 1:
                return True
        return False

    def getAllItemRemove(self, x):
        count = [0, 8]
        for _ in range(len(self.visited)):
            if self.visited[_][x] == 1:
                count = [count[0] + 1, min(count[1], _)]
                print(count)
        return count

    def comboCrush(self):
        flag = self.setupGrille()
        count, score = 0,0
        while flag:
            for i in range(len(self.grille)):
                for y in range(len(self.grille)):
                    k = self.action(i,y)
                    if k > 0:
                        count += 1
                        k *= count
                        score += k
            flag = self.setupGrille()
        return score

    def setItem(self, i, y, value):
        self.grille[i][y].type = value


if __name__ == "__main__":
    grid = GrilleCandy()
    print(grid.grille)
    print(grid.visited)
