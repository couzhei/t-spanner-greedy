#!/usr/bin/env python

from __future__ import annotations
from digraph.points import Point


class SimpleEdge(object):

    def __init__(self, src, dest):
        """Assume src and dest are instances of type Point.
           Thus, our nodes(or
        """
        self.src = src    # the "from" vertex
        self.dest = dest  # the "to" vertex

    def getSource(self) -> Point:
        return self.src

    def getDestination(self) -> Point:
        return self.dest

    def __reversed__(self) -> Edge:
        src = self.getSource()
        dest = self.getDestination()
        self.src = dest
        self.dest = src
        return self

    def __str__(self) -> str:
        return f"{self.src}->{self.dest}"

    def __repr__(self) -> str:
        str(self)

    def __hash__(self) -> str:
        return hash(str(self))

    def __eq__(self, other) -> bool:
        return f"{self.src}->{self.dest}"


class Edge(SimpleEdge):
    """
    Weighted Edge!
    """
    def __init__(self, src, dest):
        """Assume src and dest are instances of type Point,
           hence our nodes(or vertices)
        """
        self.src = src    # the "from" vertex
        self.dest = dest  # the "to" vertex
        self.weight = self.src.distance(self.dest)

    def getWeight(self) -> float:
        return self.weight


class UndirectedEdge(Edge):
    """
        The only difference with its parent will be that
        edges p-q and q-p are precisely the same. But in
        order to do such a thing, we would define to set
        the smaller point as src, which hopefully will
        result a unique hash id. We don't have to be worried
        about points, since there's a __gt__ provided there
        aka a lexicographic order.
    """
    def __init__(self, src, dest):
        if src < dest:
            self.src = src
            self.dest = dest
        else:
            self.dest = src
            self.src = dest
        self.weight = self.src.distance(self.dest)
