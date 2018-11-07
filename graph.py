# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod

class Graph:
    __metaclass__ = ABCMeta

    @abstractmethod
    def beginNode(self):
        """ Noeud de départ du graphe """
        pass

    @abstractmethod
    def exitNode(self):
        """ Noeud d'arrivée du graphe """
        pass

    @abstractmethod
    def nodeList(self):
        """ Liste de tous les noeuds du graphe """
        pass

    @abstractmethod
    def nodeList(self, currentNode):
        """ Liste de tous les noeuds adjacent au noeud currentNode """
        pass

    @abstractmethod
    def arcsList(self):
        """ Liste de tous les arcs du graphe """
        pass

    @abstractmethod
    def arcsList(self, currentNode):
        """ Liste de tous les arcs du noeud currentNode """
        pass

    @abstractmethod
    def nodeCount(self):
        """ Nombre total de noeuds """
        pass

    @abstractmethod
    def costBetweenNode(self, fromNode, toNode):
        """ Cout entre 2 noeuds adjacent """
        pass

    @abstractmethod
    def reconstructPath(self):
        """ Méthode de reconstitution du chemin optimal en remontant les prececesseurs """
        pass

    @abstractmethod
    def computeEstimatedDistanceToExit(self):
        """ Distance estimée à la sortie selon la formule de la distance de Manhattan (nombre de case avec la sortie) """
        pass
