class Arc:
    """Represent an arc"""
    def __init__(self, fromNode = None, toNode = None, cost = 0):
        self.fromNode = fromNode
        self.toNode = toNode
        self.cost = cost

    def __repr__(self):
        return "Arc - from={} to={} cost={}".format(self.fromNode, self.toNode, self.cost)