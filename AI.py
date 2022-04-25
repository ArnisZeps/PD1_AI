from audioop import minmax
import math
from GameFieldLine import GameFieldLine

class AI():
    def __init__(self, playerType, lineManager, pointManager, gameManager):
        self.playerType = playerType
        self.lineManager = lineManager
        self.pointManager = pointManager
        self.gameManager = gameManager

    def getPlayerType(self):
        return self.playerType
        
    def getHeuristicEvaluation(self):
        eval = 0
        for pointOne in self.pointManager.getAvailablePoints():
            for pointTwo in self.pointManager.getAvailablePoints():
                if(pointOne != pointTwo):
                    if (not (self.lineManager.canExist(GameFieldLine(pointOne, pointTwo)))):
                        eval = eval + 1
        return eval/2

    def miniMax(self, depth, player, alpha, beta):
        otherPlayer = 'MINIMIZER' if player == 'MAXIMIZER' else 'MAXIMIZER'
        bestMove = None
        if(self.gameManager.checkState() != 'STILL ARE MOVES'):
            if(player == 'MAXIMIZER'):
                return -math.inf
            elif(player == 'MINIMIZER'):
                return math.inf
        if(depth == 1):
            return self.getHeuristicEvaluation()
        if(player == 'MAXIMIZER'):
            bestScore = -math.inf
        else:
            bestScore = math.inf
        for pointOne in self.pointManager.getAvailablePoints():
            for pointTwo in self.pointManager.getAvailablePoints():
                if(pointOne != pointTwo):
                    if (self.lineManager.canExist(GameFieldLine(pointOne, pointTwo))):
                        tmpLine = GameFieldLine(pointOne, pointTwo)
                        self.lineManager.addLine(tmpLine)
                        self.pointManager.removeAvailablePoints(pointOne, pointTwo)
                        option = self.miniMax(depth + 1, otherPlayer, alpha, beta)
                        self.lineManager.removeLine(tmpLine)
                        self.pointManager.addAvailablePoints(pointOne, pointTwo)
                        if(player == 'MAXIMIZER'):
                            if(option>bestScore):
                                bestScore = option      
                                bestMove = [pointOne, pointTwo]
                        else:
                            if(option<bestScore):
                                bestScore = option      
                                bestMove = [pointOne, pointTwo]
                        if (player == 'MINIMIZER'):
                            alpha = max(alpha, option)
                        else:
                            beta = min(beta, option)
                        if (beta < alpha):
                            break
        if(bestMove is None ):
            for pointOne in self.pointManager.getAvailablePoints():
                for pointTwo in self.pointManager.getAvailablePoints():
                    if(pointOne != pointTwo):
                        if (self.lineManager.canExist(GameFieldLine(pointOne, pointTwo))):
                            bestMove = [pointOne, pointTwo]

        if(depth == 0):
            self.lineManager.drawLine(bestMove[0], bestMove[1])
            self.pointManager.removeAvailablePoints(bestMove[0], bestMove[1])
        else:
            return bestScore

    def makeTurn(self):
        self.miniMax(0, self.playerType, -math.inf, math.inf)
