from tkinter import *
from turtle import left

class UIFrame(Frame):
    def __init__(self, window, gameManager):
        self.gameManager = gameManager
        self.gameManager.setUI(self)
        Frame.__init__(self,window, bg = '#355C7D', pady=10)
        self.initRightPane()
        self.initLeftPane()
        self.initCentralPane()

    def initRightPane(self):
        self.startButtonPane = Frame(self)
        self.startButtonPane.pack(side=RIGHT, expand=True)
        self.button = Button(self.startButtonPane, text='Play', command=self.playPressed)
        self.button.pack()

    def initCentralPane(self):
        self.centralPane = Frame(self)
        self.centralPane.pack(side=LEFT, expand=True)
        self.playerSelect = StringVar(None, "MAXIMIZER")
        self.R1 = Radiobutton(self.centralPane, text="COMPUTER", variable=self.playerSelect, value="MAXIMIZER")
        self.R1.pack()
        self.R2 = Radiobutton(self.centralPane, text="PLAYER", variable=self.playerSelect, value="MINIMIZER")
        self.R2.pack()
        self.labelValue = StringVar()
        self.label = Label( self.centralPane, textvariable=self.labelValue)
        self.label.pack(side=LEFT)        
        self.labelValue.set("SELECT WHO GOES FIRST")

    def initLeftPane(self):
        self.leftPane = Frame(self)
        self.leftPane.pack(side=LEFT, expand=True)
        self.leftLabelValue = StringVar()
        self.leftLabel = Label(self.leftPane, textvariable=self.leftLabelValue)
        self.leftLabel.pack(side=BOTTOM)        
        self.leftLabelValue.set("SELECT POINT COUNT")
        self.pointSelect = StringVar(None, 8)
        self.R3 = Radiobutton(self.leftPane, text="8", variable=self.pointSelect, value=8)
        self.R4 = Radiobutton(self.leftPane, text="9", variable=self.pointSelect, value=9)
        self.R5 = Radiobutton(self.leftPane, text="10", variable=self.pointSelect, value=10)
        self.R6 = Radiobutton(self.leftPane, text="11", variable=self.pointSelect, value=11)
        self.R7 = Radiobutton(self.leftPane, text="12", variable=self.pointSelect, value=12)
        self.R3.pack(side=LEFT)
        self.R4.pack(side=LEFT)
        self.R5.pack(side=LEFT)
        self.R6.pack(side=LEFT)
        self.R7.pack(side=LEFT)


    def setLabelValue(self, value):
        self.labelValue.set(value)
        pass

    def playPressed(self):
        self.button.config(text = "Restart")
        self.gameManager.startGame(self.playerSelect.get(), self.pointSelect.get())
        
    def getPlayerSelect(self):
        return self.playerSelect