#!/usr/bin/env python

from __future__ import annotations
from digraph.edge import Edge


class Digraph(object):

    def __init__(self, vertices=[]) -> None:
        self._vertices = vertices
        self._adjacencyList = {vertex: [] for vertex in vertices}
        self._edges = set()

    def addNode(self, vertex) -> None:
        if vertex in self._vertices:
            raise ValueError("Duplicate node!")
        else:
            self._vertices.append(vertex)
            self._adjacencyList[vertex] = []

    def addEdge(self, edge) -> None:
        """
        SimpleEdge: Make sure this is the correct form of Edge
        You're giving as input, since Edge, doesn't distinguish Edge(p,q)
        from Edge(q,p) and always picks the smaller Point first in the
        lexicographic order.
        """
        src = edge.getSource()
        dest = edge.getDestination()
        if not (src in self._vertices and dest in self._vertices):
            raise ValueError("Node not in graph!")
        else:
            self._adjacencyList[src].append(dest)
            self._edges.add(edge)

    def getNodes(self) -> set:
        return self._vertices

    def getAdjacencyList(self) -> dict:
        return self._adjacencyList

    def getEdges(self) -> set:
        return self._edges

    def __str__(self) -> str:
        result = ""
        for src in self._vertices:
            for dest in self._adjacencyList[src]:
                result += str(Edge(src, dest)) + "\n"

        return result[:-1]  # without final new line

    def __repr__(self) -> str:
        self.__str__()


class Graph(Digraph):

    def addEdge(self, edge) -> None:
        Digraph.addEdge(self, edge)
        src = edge.getSource()
        dest = edge.getDestination()
        Digraph.addEdge(self, Edge(dest, src))


class WeightedDigraph(Digraph):
    pass


class WeightedGraph(Graph):

    def __init__(self, vertices=[]) -> None:
        self._vertices = vertices
        self._adjacencyList = {vertex: [] for vertex in vertices}
        self._edges = set()
        self._weights = {}

    def addEdge(self, edge) -> None:

        super().addEdge(edge)
        weight = edge.getSource().distance(edge.getDestination())  # We simply get the distance between
        self._weights[edge] = weight                               # two ends of the edge as the weight
                                                                   # our edges are hashable types of
                                                                   # objects, thus making them a perfect
                                                                   # candidate for a dict key
        def getWeights(self):
            return self._weights
