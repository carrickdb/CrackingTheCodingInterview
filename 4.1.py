import queue

class Node:

    def __init__(self, val):
        self.val = val
        self.edges = []
        self.marked = 0

    def addEdges(self, edges):
        self.edges += edges

class Graph:

    def __init__(self):
        self.nodes = []

    def addNodes(self, nodes):
        self.nodes += nodes

    def findPath(self, n1, n2):
        n1.marked = 1
        n2.marked = 2
        q1 = queue.Queue()
        q1.put(n1)
        q2 = queue.Queue()
        q2.put(n2)

        def searchNextLevel(q, qMark, otherQueueMark):
            if not q.empty():
                curr = q.get()
                for node in curr.edges:
                    if not node.marked:
                        node.marked = qMark
                        q.put(node)
                    elif node.marked == otherQueueMark:
                        return True
            return False

        while not q1.empty() or not q2.empty():
            pathFound = searchNextLevel(q1, 1, 2)
            if pathFound:
                return True
            pathFound = searchNextLevel(q2, 2, 1)
            if pathFound:
                return True
        return False

nodes = []
for i in range(6):
    nodes.append(Node(i))

g = Graph()
g.addNodes(nodes)
print(g.findPath(nodes[0], nodes[-1]))

"""
n1->n2
"""
