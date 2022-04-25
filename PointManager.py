import random
from tkinter import *
from GameFieldPoint import GameFieldPoint

class PointManager():
    
    def __init__(self, canvas):
        self.canvas = canvas

    def createPoints(self, pointCount):
        self.gamePoints = []
        for i in range(int(pointCount)):
            x = random.randint(5, self.canvas.winfo_width() - 5)
            y = random.randint(5, self.canvas.winfo_height() - 5)
            for point in self.gamePoints:
                if(x == point.getX()):
                    print("equal")
                    x = x + 1
            self.gamePoints.append(GameFieldPoint(x, y))
        self.availablePoints = self.gamePoints
        self.drawPoints()

    def drawPoints(self):
        for point in self.gamePoints:
            x1, y1 = (point.getX() - 3), (point.getY() - 3)
            x2, y2 = (point.getX() + 3), (point.getY() + 3)
            self.canvas.create_oval(x1, y1, x2, y2, fill="#476042")            
    
    def removeAvailablePoints(self, pointOne, pointTwo):
        self.availablePoints.remove(pointOne)
        self.availablePoints.remove(pointTwo)

    def addAvailablePoints(self, pointOne, pointTwo):
        self.availablePoints.append(pointOne)
        self.availablePoints.append(pointTwo)

    def getAvailablePoints(self):
        return self.availablePoints

    def getGamePoints(self):
        return self.gamePoints