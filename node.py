# -*- coding: utf-8 -*-
class Node:
    """Represent a node"""

    def __init__(self, p=None, d=float('inf'), e=0):
        self.precursor = p
        self.distanceFromBegin = d
        self.estimatedDistance = e

    def hasPrecursor(self):
        return True if self.precursor != None else False

    def __repr__(self):
        #return "affichage"
        return " (Node: dist={} hasPrecursor={} estim={})".format(self.distanceFromBegin, self.hasPrecursor(), self.estimatedDistance)


def testClass():
    n = Node()
    print(n)

if __name__ == '__main__':
    testClass()