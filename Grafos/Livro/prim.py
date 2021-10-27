import heapq
from Graph import Graph, Vertex
import sys


def prim(G, start):
    pq = []
    for v in G:
        v.setDistance(sys.maxsize)
        v.setPred(None)
    start.setDistance(0)
    pq = [(v.getDistance(), v) for v in G]
    heapq.heapify(pq)
    while pq != []:
        currentVert = heapq.heappop(pq)
        for nextVert in currentVert.getConnections():
            newCost = currentVert.getWeight(nextVert)
            if nextVert in pq and newCost < nextVert.getDistance():
                nextVert.setPred(currentVert)
                nextVert.setDistance(newCost)
                pq.pop(nextVert)
                heapq.heapify(pq)
                heapq.heappush((newCost, nextVert))
