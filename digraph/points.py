#!/usr/bin/env python

from __future__ import annotations
from dataclasses import dataclass  # A Python 3.7 feature which I always wanted to try :)


@dataclass  # see the magic
class Point(object):
    x: float
    y: float

    def distance(self, other) -> float:
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def getX(self) -> float:
        return self.x
    
    def getY(self) -> float:
        return self.y
    
    def __str__(self) -> str:
        return "({0}, {1})".format(self.x, self.y)

    def __repr__(self) -> str:
        return "({0}, {1})".format(self.x, self.y)

    def __hash__(self) -> int:
        return hash(str(self))

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y

    def __gt__(self, other) -> bool:  # comparing points in a lexicographic manner
        if self.x > other.x:
            return True
        elif self.x == other.x and self.y > other.y:
            return True
        else:
            return False

    def __lt__(self, other) -> bool:
        if self.x < other.x:
            return True
        elif self.x == other.x and self.y < other.y:
            return True
        else:
            return False
