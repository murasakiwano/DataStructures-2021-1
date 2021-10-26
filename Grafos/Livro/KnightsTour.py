from Graph import Graph, Vertex


def knightGraph(bdSize):
    ktGraph = Graph()
    for row in range(bdSize):
        for col in range(bdSize):
            nodeId = posToNodeId(row, col, bdSize)
            newPositions = genLegalMoves(row, col, bdSize)
            for e in newPositions:
                nid = posToNodeId(e[0], e[1], bdSize)
                ktGraph.addEdge(nodeId, nid)
    return ktGraph


def posToNodeId(row, column, board_size):
    return (row * board_size) + column


def genLegalMoves(x, y, bdSize):
    newMoves = []
    moveOffsets = [(-1, -2), (-1, 2), (-2, -1), (-2, 1),
                   (1, -2), (1, 2), (2, -1), (2, 1)]
    for i in moveOffsets:
        newX = x + i[0]
        newY = y + i[1]
        if legalCoord(newX, bdSize) and \
                legalCoord(newY, bdSize):
            newMoves.append((newX, newY))
    return newMoves


def legalCoord(x, bdSize):
    if x >= 0 and x < bdSize:
        return True
    else:
        return False


def knightTour(n, path, u, limit):
    """
        n: current depth in the search tree;
        path: list of vertices visited up to this point;
        u: the vertex in the graph we wish to explore;
        limit: the number of nodes in the path.
    """
    u.setColor('gray')  # visited
    path.append(u)
    if n < limit:
        # Choose a new vertex to explore and call knightTour recursively
        # nbrList = list(u.getConnections())
        nbrList = orderByAvail(n)
        i = 0
        done = False
        while i < len(nbrList) and not done:
            if nbrList[i].getColor() == 'white':
                done = knightTour(n+1, path, nbrList[i], limit)
            i = i + 1
        if not done:  # prepare to backtrack
            path.pop()
            u.setColor('white')
    else:
        done = True  # Found a successful tour
    return done  # if False, then we need to do a backtracking


def orderByAvail(n):
    resList = []
    for v in n.getConnections():
        if v.getColor() == 'white':
            c = 0
            for w in v.getConnections():
                if w.getColor() == 'white':
                    c = c + 1
            resList.append((c, v))
    resList.sort(key=lambda x: x[0])
    return [y[1] for y in resList]


def main():
    path = []
    # build the graph
    g = Graph()
    A = Vertex('A')
    B = Vertex('B')
    C = Vertex('C')
    D = Vertex('D')
    E = Vertex('E')
    F = Vertex('F')
    g.addVertex(A)
    g.addVertex(B)
    g.addVertex(C)
    g.addVertex(D)
    g.addVertex(E)
    g.addVertex(F)
    g.addEdge(A, B)
    g.addEdge(A, D)
    g.addEdge(B, C)
    g.addEdge(B, D)
    g.addEdge(D, E)
    g.addEdge(E, B)
    g.addEdge(E, F)
    g.addEdge(F, C)
    print(g)
    print(B)
    print(A)
    knightTour(0, path, A, 6)


if __name__ == '__main__':
    main()
