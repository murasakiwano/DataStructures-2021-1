from Graph import Graph, Vertex
import heapq


def dijkstra(aGraph, start):
    start.setDistance(0)
    pq = [(v.getDistance(), v) for v in aGraph]
    heapq.heapify(pq)
    while pq != []:
        currentVert = heapq.heappop(pq)
        for nextVert in currentVert.getConnections():
            newDist = currentVert.getDistance() \
                    + currentVert.getWeight(nextVert)
            if newDist < nextVert.getDistance():
                nextVert.setDistance(newDist)
                nextVert.setPred(currentVert)
                if nextVert in pq:
                    pq.pop(nextVert)
                    heapq.heapify(pq)
                heapq.heappush((newDist, nextVert))
    