from GameFieldLine import GameFieldLine
from AI import AI

class GameManager:
    def __init__(self, pointManager, lineManager, gameCanvas):
        self.playerOne = 'MAXIMIZER'
        self.playerTwo = 'MINIMIZER'
        self.gameCanvas = gameCanvas
        self.isGameInProgress = False
        self.lineManager = lineManager
        self.pointManager = pointManager
        self.currentPlayer = self.playerOne

    def setUI(self, UI):
        self.UI = UI

    def startGame(self, AIType, pointCount):
        self.isGameInProgress = True
        self.UI.setLabelValue("GAME IN PROGRESS")
        self.currentPlayer = self.playerOne
        self.ai = AI(AIType, self.lineManager, self.pointManager, self)
        if(not self.isGameInProgress):
            self.pointManager.createPoints(pointCount)
            self.handleAIStart()
        else:
            self.gameCanvas.delete("all")
            self.lineManager.resetLines()
            self.pointManager.createPoints(pointCount)
            self.handleAIStart()

    def handleAIStart(self):
        if(self.ai.getPlayerType() == self.currentPlayer):
            self.ai.makeTurn()
            self.handleMove()

    def getCurrentPlayer(self):
        return self.currentPlayer
    
    def checkState(self):
        for firstPoint in self.pointManager.getAvailablePoints(): 
            for secondPoint in self.pointManager.getAvailablePoints():
                if(firstPoint != secondPoint): 
                    if(self.lineManager.canExist(GameFieldLine(firstPoint, secondPoint))):
                        return 'STILL ARE MOVES'
        return self.currentPlayer

    def handleMove(self):
        state = self.checkState()
        if(state == 'STILL ARE MOVES'):
            if(self.currentPlayer == self.playerOne):
                self.currentPlayer = self.playerTwo
            else:
                self.currentPlayer = self.playerOne

            if(self.currentPlayer == self.ai.getPlayerType()):
                self.ai.makeTurn()
                self.handleMove()
        else:
            if(state == 'MAXIMIZER' and self.ai.getPlayerType() == 'MAXIMIZER'):
                winner = 'COMPUTER'
            elif(state == 'MINIMIZER' and self.ai.getPlayerType() == 'MINIMIZER'):
                winner = 'COMPUTER'
            else:
                winner = 'PLAYER'
            self.UI.setLabelValue(str(winner) + " WON!")
