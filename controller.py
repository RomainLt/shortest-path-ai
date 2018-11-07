# -*- coding: utf-8 -*-
import time

from map import *
from ihm import *

def algoProfondeur():
    resetGraph()
    start = time.clock()

    notVisitedList = graph.nodeList()
    nodesToVisit = []
    nodesToVisit.append(graph.beginNode) # pile
    notVisitedList.remove(graph.beginNode)
    exitNode = graph.exitNode

    exitReached = False
    ind = 0
    while (len(nodesToVisit) != 0 and not exitReached):
        currentNode = nodesToVisit.pop()
        if (currentNode == exitNode):
            exitReached = True
        else:
            for node in graph.closeNodeList(currentNode):
                if (notVisitedList.__contains__(node)):
                    notVisitedList.remove(node)
                    node.precursor = currentNode
                    node.distanceFromBegin = currentNode.distanceFromBegin + graph.costBetweenNode(currentNode, node)
                    nodesToVisit.append(node)

                    if VISUHUMAN:
                        ihm.fen.after(ind * VISUTIME, ihm.drawElementText, node.distanceFromBegin, node.row, node.col, 'black')
                        ihm.fen.update()
                        ind+=1

    elapsedTime = (time.clock() - start) * 1000
    updateInformation("Finished {:.3f} ms ({})".format(elapsedTime, graph.exitNode.distanceFromBegin))

def algoLargeur():
    resetGraph()
    start = time.clock()

    notVisitedList = graph.nodeList() # noeuds non visités
    nodesToVisit = [] # noeuds à visiter
    nodesToVisit.append(graph.beginNode) # enfiler le noeud de départ
    notVisitedList.remove(graph.beginNode) # enlever le noeud de la liste des noeuds non visités
    exitNode = graph.exitNode # noeud de sortie

    exitReached = False # sortie trouvée
    ind = 0
    while (len(nodesToVisit) != 0 and not exitReached): # tant qu'il y a des noeuds et que la sortie n'est pas trouvée
        currentNode = nodesToVisit.pop(0) # pop(0) pour une file et pop() pour une pile, car la pile on prend le dernier élément
        if (currentNode == exitNode): # si le noeud courant est le noeud de sortie
            exitReached = True # sortie
        else: # sinon
            for node in graph.closeNodeList(currentNode): # pour chaque noeuds autour du noeud courant
                if (notVisitedList.__contains__(node)): # si la liste des noeuds non visités contient ce noeud
                    notVisitedList.remove(node) # enlever le noeud de la liste des noeuds non visités
                    node.precursor = currentNode # définir le précurseur de ce noeud avec le noeud courant
                    node.distanceFromBegin = currentNode.distanceFromBegin + graph.costBetweenNode(currentNode, node) # distance du noeud courant + coût et des adjacents
                    nodesToVisit.append(node) # enfiler ce noeud à la liste des noeuds à visiter

                    if VISUHUMAN:
                        ihm.fen.after(ind * VISUTIME, ihm.drawElementText, node.distanceFromBegin, node.row, node.col, 'black')
                        ihm.fen.update()
                        ind+=1

        elapsedTime = (time.clock() - start) * 1000
        updateInformation("Finished {:.3f} ms ({})".format(elapsedTime, graph.exitNode.distanceFromBegin))
    

def algoBellmanFord():
    resetGraph()
    nodes = graph.nodeList() # liste des noeuds    
    arcsList = graph.arcsList() # Liste des arcs
    distanceChanged = True
    nbLoopMax = len(nodes)-1 # Nombre de noeuds -1 à parcourir
    indice = 0

    start = time.clock()

    while (indice < nbLoopMax and distanceChanged):
        distanceChanged = False
        for arc in arcsList:
            if ((arc.fromNode.distanceFromBegin + arc.cost) < arc.toNode.distanceFromBegin):
                arc.toNode.distanceFromBegin = (arc.fromNode.distanceFromBegin + arc.cost)
                arc.toNode.precursor = arc.fromNode
                distanceChanged = True

            if VISUHUMAN:
                    ihm.fen.after(indice * VISUTIME, ihm.drawElementText, arc.fromNode.distanceFromBegin, arc.fromNode.row, arc.fromNode.col, 'black')
                    ihm.fen.update()
                    indice+=1
        indice+=1
        
    for arc in arcsList:
        if ((arc.fromNode.distanceFromBegin + arc.cost) < arc.toNode.distanceFromBegin):
            print('erreur')

    elapsedTime = (time.clock() - start) * 1000
    updateInformation("Finished {:.3f} ms ({})".format(elapsedTime, graph.exitNode.distanceFromBegin))

    

def algoDijkstra():
    resetGraph()
    nodesToVisit = graph.nodeList()
    exitReached = False
    exitNode = graph.exitNode

    indice = 0
    start = time.clock()

    while (len(nodesToVisit) != 0 and not exitReached):
        currentNode = nodesToVisit[0]
        for node in nodesToVisit:
            if node.distanceFromBegin < currentNode.distanceFromBegin:
                currentNode = node
        if currentNode == exitNode:
            exitReached = True
        else:
            adjacentArcs = graph.closeArcsList(currentNode) # *** voir fichier map et pas graph ***
            for arc in adjacentArcs:
                if ((arc.fromNode.distanceFromBegin + arc.cost) < arc.toNode.distanceFromBegin):
                    arc.toNode.distanceFromBegin = (arc.fromNode.distanceFromBegin + arc.cost)
                    arc.toNode.precursor = arc.fromNode

                if VISUHUMAN:
                    ihm.fen.after(indice * VISUTIME, ihm.drawElementText, arc.fromNode.distanceFromBegin, arc.fromNode.row, arc.fromNode.col, 'black')
                    ihm.fen.update()
                    indice+=1

            nodesToVisit.remove(currentNode)
    
    elapsedTime = (time.clock() - start) * 1000
    updateInformation("Finished {:.3f} ms ({})".format(elapsedTime, graph.exitNode.distanceFromBegin))

def algoAStar():
    resetGraph()
    graph.computeEstimatedDistanceToExit()
    nodesToVisit = graph.nodeList()
    exitReached = False
    exitNode = graph.exitNode

    indice = 0
    start = time.clock()
    while (len(nodesToVisit) != 0 and not exitReached):
        currentNode = nodesToVisit[0]
        for node in nodesToVisit:
            if ((node.estimatedDistance + node.distanceFromBegin) < ( currentNode.estimatedDistance + currentNode.distanceFromBegin)):
                currentNode = node
        if currentNode == exitNode:
            exitReached = True
        else:
            adjacentArcs = graph.closeArcsList(currentNode)
            for arc in adjacentArcs:
                if ((arc.fromNode.distanceFromBegin + arc.cost) < arc.toNode.distanceFromBegin):
                    arc.toNode.distanceFromBegin = (arc.fromNode.distanceFromBegin + arc.cost)
                    arc.toNode.precursor = arc.fromNode

            if VISUHUMAN:
                ihm.fen.after(indice * VISUTIME, ihm.drawElementText, arc.fromNode.distanceFromBegin, arc.fromNode.row, arc.fromNode.col, 'black')
                ihm.fen.update()
                indice+=1

            nodesToVisit.remove(currentNode)

def algoSolution():
    print(graph.reconstructPath())
    row, col = 0, 0

    if VISUHUMAN:
        graph.initReconstructPathByStepInit()
        ind = 0
        while(row!=-1 and col!=-1):
            row, col = graph.reconstructPathByStep()

            ihm.fen.after(ind * VISUTIME, ihm.drawElement, row, col, 'red')
            ihm.fen.update()
            ind += 1
    # print(graph.exitNode().distanceFromBegin)

mapStr  = "..  XX   .\n"
mapStr += "*.  *X  *.\n"
mapStr += " .  XX ...\n"
mapStr += " .* X *.* \n"
mapStr += " ...=...  \n"
mapStr += " .* X     \n"
mapStr += " .  XXX*  \n"
mapStr += " .  * =   \n"
mapStr += " .... XX  \n"
mapStr += "   *.  X* "
#print(mapStr)
'''
mapStr  = ".   \n"
mapStr += ".X. \n"
mapStr += ".XX.\n"
mapStr += ". X "
'''

VISUTIME = 50
VISUHUMAN = True
graph = None
ihm = None
label = None

def updateInformation(_text):
    label.config(text=_text)
    label.update()

def resetGraph():
    global graph
    # graph = Map(mapStr, 0, 0, 9, 9)
    # graph = Map(mapStr, 0, 0, 3, 9)
    graph = Map(mapStr, 0, 0, 9, 9)
    print(graph)

    global ihm
    if (not ihm):
        ihm = Ihm(graph)

        b1A = Button(ihm.fen, text='Profondeur', command=algoProfondeur)
        b1A.pack(side=LEFT, padx=3, pady=3)

        b2A = Button(ihm.fen, text='Largeur', command=algoLargeur)
        b2A.pack(side=LEFT, padx=3, pady=3)

        b3A = Button(ihm.fen, text='Bellman-Ford', command=algoBellmanFord)
        b3A.pack(side=LEFT, padx=3, pady=3)

        b3A = Button(ihm.fen, text='Dijkstra', command=algoDijkstra)
        b3A.pack(side=LEFT, padx=3, pady=3)

        b3A = Button(ihm.fen, text='A*', command=algoAStar)
        b3A.pack(side=LEFT, padx=3, pady=3)

        b3S = Button(ihm.fen, text='Solution', command=algoSolution)
        b3S.pack(side=LEFT, padx=3, pady=3)

        global label
        label = Label(ihm.fen, text="Informations")
        label.pack(side=LEFT, padx=3, pady=3)
    ihm.drawEnv()

resetGraph()
ihm.fenLaunch()