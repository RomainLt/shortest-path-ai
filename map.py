# -*- coding: utf-8 -*-
from graph import *
from tile import *

from arc import *


class Map(Graph):
    def __init__(self, _mapstr, _beginRow, _beginColumn, _exitRow, _exitColumn):
        mapRows = _mapstr.split('\n')
        self.nbRows = len(mapRows)
        self.nbCols = len(mapRows[0])
        self.tiles = self.createEmpty2dList(self.nbRows, self.nbCols)

        for irow in range(0, self.nbRows):
            for icol in range(0, self.nbCols):
                self.tiles[irow][icol] = Tile(irow, icol, TileConverter.typeFromChar(mapRows[irow][icol]))
                # print("{} {} {}".format(irow, icol, self.tiles[irow][icol]))

        self.beginNode = self.tiles[_beginRow][_beginColumn]
        self.beginNode.distanceFromBegin = 0 #self.beginNode.cost()
        self.exitNode = self.tiles[_exitRow][_exitColumn]

        self.nodeList()
        self.arcsList()

    def __repr__(self):
        line = ''
        for irow in range(0, self.nbRows):
            for icol in range(0, self.nbCols):
                line += "{}".format(self.tiles[irow][icol].tileType.value)
            line += '\n'
        return line

    def createEmpty2dList(self, row, col):
            return [[None] * col for i in range(row)]

    def nodeList(self):
        self.nList = []
        for irow in range(0, self.nbRows):
            for icol in range(0, self.nbCols):
                self.nList.append(self.tiles[irow][icol])
        return self.nList

    def closeNodeList(self, currentNode):
        currentRow = currentNode.row
        currentCol = currentNode.col
        tempNodeList = []

        if (currentRow - 1 >= 0 and self.tiles[currentRow - 1][currentCol].isValidPath()):
            tempNodeList.append(self.tiles[currentRow - 1][currentCol])
        if (currentCol - 1 >= 0 and self.tiles[currentRow][currentCol - 1].isValidPath()):
            tempNodeList.append(self.tiles[currentRow][currentCol - 1])
        if (currentRow + 1 < self.nbRows and self.tiles[currentRow + 1][currentCol].isValidPath()):
            tempNodeList.append(self.tiles[currentRow + 1][currentCol])
        if (currentCol + 1 < self.nbCols and self.tiles[currentRow][currentCol + 1].isValidPath()):
            tempNodeList.append(self.tiles[currentRow][currentCol + 1])

        return tempNodeList

    def arcsList(self):
        self.aList = []
        for irow in range(0, self.nbRows):
            for icol in range(0, self.nbCols):
                if (self.tiles[irow][icol].isValidPath()):
                    #haut
                    if (irow - 1 >= 0 and self.tiles[irow - 1][icol].isValidPath()):
                        self.aList.append(Arc(self.tiles[irow][icol], self.tiles[irow - 1][icol], self.tiles[irow - 1][icol].cost()))
                    #gauche
                    if (icol - 1 >= 0 and self.tiles[irow][icol - 1].isValidPath()):
                        self.aList.append(Arc(self.tiles[irow][icol], self.tiles[irow][icol - 1], self.tiles[irow][icol - 1].cost()))
                    #bas
                    if (irow + 1 < self.nbRows and self.tiles[irow + 1][icol].isValidPath()):
                        self.aList.append(Arc(self.tiles[irow][icol], self.tiles[irow + 1][icol],  self.tiles[irow + 1][icol].cost()))
                    #droite
                    if (icol + 1 < self.nbCols and self.tiles[irow][icol + 1].isValidPath()):
                        self.aList.append(Arc(self.tiles[irow][icol], self.tiles[irow][icol + 1], self.tiles[irow][icol + 1].cost()))

        return self.aList

    def closeArcsList(self, currentNode):
        currentRow = currentNode.row
        currentCol = currentNode.col
        tempArcList = []

        if (currentRow - 1 >= 0 and self.tiles[currentRow - 1][currentCol].isValidPath()):
            tempArcList.append(Arc(currentNode, self.tiles[currentRow - 1][currentCol], self.tiles[currentRow - 1][currentCol].cost()))
        if (currentCol - 1 >= 0 and self.tiles[currentRow][currentCol - 1].isValidPath()):
            tempArcList.append(Arc(currentNode, self.tiles[currentRow][currentCol - 1], self.tiles[currentRow][currentCol - 1].cost()))
        if (currentRow + 1 < self.nbRows and self.tiles[currentRow + 1][currentCol].isValidPath()):
            tempArcList.append(Arc(currentNode, self.tiles[currentRow + 1][currentCol], self.tiles[currentRow + 1][currentCol].cost()))
        if (currentCol + 1 < self.nbCols and self.tiles[currentRow][currentCol + 1].isValidPath()):
            tempArcList.append(Arc(currentNode, self.tiles[currentRow][currentCol + 1], self.tiles[currentRow][currentCol + 1].cost()))

        return tempArcList

    def nodeCount(self):
        return self.nbRows * self.nbCols

    def costBetweenNode(self, fromNode, toNode):
        return toNode.cost()

    def reconstructPath(self):
        resPath = ""
        currentNode = self.exitNode
        prevNode = currentNode.precursor

        while (hasattr(prevNode, 'precursor')):
            resPath += "{}".format(currentNode)
            currentNode = prevNode
            prevNode = prevNode.precursor

        return "@>{} {}".format(resPath, currentNode)

    def initReconstructPathByStepInit(self):
        self.rpCurrentNode = self.exitNode
        self.rpPrevNode = self.rpCurrentNode.precursor

    def reconstructPathByStep(self):
        if hasattr(self.rpPrevNode, 'precursor'):
            self.rpCurrentNode = self.rpPrevNode
            self.rpPrevNode = self.rpPrevNode.precursor
            return self.rpCurrentNode.row, self.rpCurrentNode.col
        else:
            return -1, -1

    def computeEstimatedDistanceToExit(self):
        for irow in range(0, self.nbRows):
            for icol in range(0, self.nbCols):
                self.tiles[irow][icol].estimatedDistance = abs(self.exitNode.row - self.tiles[irow][icol].row) + abs(self.exitNode.col - self.tiles[irow][icol].col)
                #print(self.tiles[irow][icol].estimatedDistance)

    def clear(self):
        self.nList = []
        self.aList = []

        for irow in range(0, self.nbRows):
            for icol in range(0, self.nbCols):
                self.tiles[irow][icol].distanceFromBegin = float('inf')
                self.tiles[irow][icol].precursor = None

        self.beginNode.distanceFromBegin = self.beginNode.cost()
