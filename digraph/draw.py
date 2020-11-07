#!/usr/bin/env python

from __future__ import annotations
import matplotlib.pyplot as plt


def draw_graph(graph) -> None:
    """
    drawing graph taken as input by means of matplotlib library
    """
    pts = graph.getNodes()
    lines = graph.getEdges()

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xlim([-10, 10])
    ax.set_ylim([-10, 10])

    for line in lines:
        x1, x2 = line.getSource().getX(), line.getDestination().getX()
        y1, y2 = line.getSource().getY(), line.getDestination().getY()
        plt.plot([x1, x2], [y1, y2], 'go-')

    for pt in pts:
        plt.plot(pt.getX(), pt.getY(), 'ro')
        plt.axis('equal')

    plt.show()
