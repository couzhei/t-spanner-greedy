#!/usr/bin/env python

from __future__ import annotations
from digraph.edge import UndirectedEdge


def dijkstra(graph, initial) -> (dict, dict):
    visited = {initial: 0}
    path = {}

    nodes = set(graph.getNodes())
    edges = graph.getAdjacencyList()

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node

        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in edges[min_node]:
            weight = current_weight + UndirectedEdge(min_node, edge).getWeight()
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node

    return visited, path


def shortest_path(graph, origin, destination) -> float:
    visited, paths = dijkstra(graph, origin)
    # full_path = deque()
    # _destination = paths[destination]
    #
    # while _destination != origin:
    #     full_path.appendleft(_destination)
    #     _destination = paths[_destination]
    #
    # full_path.appendleft(origin)
    # full_path.append(destination)
    try:
        return visited[destination]# , list(full_path)
    except KeyError:
        return float("inf")
