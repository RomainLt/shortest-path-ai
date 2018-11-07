from tkinter import *

from tile import *


class Ihm:
    tileSize = 50

    def __init__(self, graph):
        fen = Tk()
        self.graph = graph
        self.canvasSizeWidth = self.graph.nbCols * Ihm.tileSize
        self.canvasSizeHeight = self.graph.nbRows * Ihm.tileSize
        canvas = Canvas(fen, width=self.canvasSizeWidth, height=self.canvasSizeHeight, bg='white', bd=0)
        canvas.pack()
        self.fen = fen
        self.canvas = canvas;
        #self.canvasSize = canvasSize

    def fenLaunch(self):
        """ This is bloquant """
        self.fen.mainloop()

    def drawEnv(self):
        self.canvas.delete(ALL)
        xWidth = self.canvasSizeWidth / self.graph.nbCols
        yHeight = self.canvasSizeHeight / self.graph.nbRows

        for irow in range(0, self.graph.nbRows):
            for icol in range(0, self.graph.nbCols):
                x = icol * xWidth
                y = irow * yHeight

                x1 = ((icol + 1) * xWidth) - 1
                y1 = ((irow + 1) * yHeight) - 1

                colorId = self.graph.tiles[irow][icol].tileType
                if colorId.value == TileType.PATH.value:
                    color = "#7F7D7D"
                elif colorId.value == TileType.GRASS.value:
                    color = "#04B431"
                elif colorId.value == TileType.WATER.value:
                    color = "#A9D0F5"
                elif colorId.value == TileType.BRIDGE.value:
                    color = "#8B4513"
                elif colorId.value == TileType.TREE.value:
                    color = "#800000"
                else:
                    color = 'black'

                #print(x, y, x1, y1, color)
                self.canvas.create_rectangle(x, y, x1, y1, fill=color)

        self.drawElement(self.graph.beginNode.row, self.graph.beginNode.col, 'pink')
        self.drawElement(self.graph.exitNode.row, self.graph.exitNode.col, 'red')

    def drawElement(self, irow, icol, color='black'):
        xWidth = self.canvasSizeWidth / self.graph.nbCols
        yHeight = self.canvasSizeHeight / self.graph.nbRows
        x = icol * xWidth
        y = irow * yHeight
        x1 = ((icol + 1) * xWidth) - 1
        y1 = ((irow + 1) * yHeight) - 1
        self.canvas.create_oval(x+10, y+10, x1-10, y1-10, fill=color)

    def drawElementText(self, chaine, irow, icol, color='black'):
        xWidth = self.canvasSizeWidth / self.graph.nbCols
        yHeight = self.canvasSizeHeight / self.graph.nbRows
        x = icol * xWidth
        y = irow * yHeight
        x1 = ((icol + 1) * xWidth) - 1
        y1 = ((irow + 1) * yHeight) - 1
        self.canvas.create_oval(x+10, y+10, x1-10, y1-10, fill=color)
        self.canvas.create_text(x+(x1-x)/2, y+(y1-y)/2, fill='white', text=chaine)