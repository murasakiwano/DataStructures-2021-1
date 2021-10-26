from Graph import Graph, Vertex
from queue import Queue


def bfs(g, start):
    start.setDistance(0)
    start.setPred(None)
    vertQueue = Queue()
    vertQueue.put(start)
    while (vertQueue.size() > 0):
        currentVert = vertQueue.get()
        for nbr in currentVert.getConnections():
            if (nbr.getColor() == 'white'):
                nbr.setColor('gray')
                nbr.setDistance(currentVert.getDistance() + 1)
                nbr.setPred(currentVert)
                vertQueue.put(nbr)
            currentVert.setColor('black')