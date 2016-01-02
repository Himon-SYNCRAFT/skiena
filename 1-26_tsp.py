"""
Implement the two TSP heuristics of Section 1.1 (page 5). Which of them gives
better-quality solutions in practice? Can you devise a heuristic that works better
than both of them?
"""

import unittest


def nearest_neighbor(edges, start_point=0):
    visited = {start_point}
    path = [start_point]
    while edges:
        connected_edges_to_last_point = {}
        for points, distance in list(edges.items()):
            if path[len(path) - 1] in points:
                connected_edges_to_last_point[points] = distance
        if connected_edges_to_last_point:
            next_edge = min(connected_edges_to_last_point,
                            key=connected_edges_to_last_point.get)
            for point in next_edge:
                if point not in visited:
                    visited.add(point)
                    path.append(point)
            for edge in connected_edges_to_last_point.keys():
                del edges[edge]
    return path


def closest_pair(edges):
    visited = set()
    path = []
    chains = []
    min_key = min(edges, key=edges.get)
    chains.append([min_key])
    del edges[min_key]

    while edges:
        min_key = min(edges, key=edges.get)
        connection_point = None

        for chain in chains:
            if min_key[0] in chain[0]:
                chain.insert(0, min_key)
                connection_point = min_key[0]
            elif min_key[0] in chain[len(chain) - 1]:
                chain.append(min_key)
                connection_point = min_key[0]
            elif min_key[1] in chain[0]:
                chain.insert(0, min_key)
                connection_point = min_key[1]
            elif min_key[1] in chain[len(chain) - 1]:
                chain.append(min_key)
                connection_point = min_key[1]

            #print('chain', chain)
        if connection_point is None:
            chains.append([min_key])
            del edges[min_key]

        for edge in list(edges.keys()):
            if connection_point in edge:
                del edges[edge]
        print('edges', edges.keys())

    return chains


def points_to_edges():
    pass


if __name__ == "__main__":

    edges = {
        (0, 1): 2,
        (0, 2): 3,
        (0, 3): 4,
        (1, 2): 4,
        (1, 3): 3,
        (2, 3): 2
    }

    print(closest_pair(edges))
    unittest.main()
